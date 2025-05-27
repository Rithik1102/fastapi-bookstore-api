from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from main import app
from models import User, Book
from passlib.context import CryptContext


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def setup_module(module):
    Base.metadata.drop_all(bind=engine)  # Reset DB
    Base.metadata.create_all(bind=engine)  # Create tables
    
    with TestingSessionLocal() as db:
        test_user = User(
            username="testuser",
            email="test@example.com",
            hashed_password=pwd_context.hash("testpassword")
        )
        db.add(test_user)
        db.commit()




def test_register_user():
    response = client.post("/register", json={"username": "newuser", "email": "new@example.com", "password": "newpassword"})
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}


def test_login():
    response = client.post("/login", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_create_book():
    login_response = client.post("/login", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/books", headers=headers, json={"title": "My Test Book", "author": "Test Author"})
    
    assert response.status_code == 200
    assert response.json()["title"] == "My Test Book"


def test_get_books():
    login_response = client.post("/login", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/books", headers=headers)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_book():
    login_response = client.post("/login", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/books", headers=headers, json={"title": "Book to Update", "author": "Author"})
    book_id = response.json()["id"]
    
    response = client.put(f"/books/{book_id}", headers=headers, json={"title": "Updated Title", "author": "Updated Author"})
    
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_delete_book():
    login_response = client.post("/login", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/books", headers=headers, json={"title": "Book to Delete", "author": "Author"})
    book_id = response.json()["id"]

    response = client.delete(f"/books/{book_id}", headers=headers)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted successfully"}
