# fastapi-bookstore-api
A **RESTful API** for managing a book collection using **FastAPI**, **SQLite**, and **SQLAlchemy**.  
It includes **user authentication**, **book CRUD operations**, and **JWT-based authentication**.

## **📌 Features**
- ✅ **User authentication** (Register & Login)  
- ✅ **Create, read, update, and delete (CRUD) books**  
- ✅ **Token-based authentication (JWT)**  
- ✅ **SQLite** for local development (easily extendable to **PostgreSQL** or **MySQL**)  
- ✅ **Test suite using pytest**  

---

## 📥 Installation

### 1️⃣Install Python and pip  
Before proceeding, ensure Python and pip are installed.  

#### **Windows**  
1. Download and install Python from [python.org](https://www.python.org/downloads/).  
2. Verify the installation:  (open terminal)
   python --version
   pip --version

   
#### Linux/macOS

```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# macOS (Homebrew)
brew install python


#Verify the installation
  python3 --version
  pip3 --version


#Clone the Repository
  git clone https://github.com/ohangbonfastapi-bookstore-api.git
  cd fastapi-bookstore-api


#Set Up a Virtual Environment
#For Windows CMD/powershell
   python -m venv venv
   venv\Scripts\activate


#For Linux/macOS: Terminal
   python3 -m venv venv
   source venv/bin/activate


#Install Dependencies
   pip install -r requirements.txt


#Create a .env File
#After cloning the project, create a .env file in the root directory and add the following environment variables:
    SECRET_KEY=yC3j8p9aL2xR7v1qF5zK0m6eH4bI9uW1gT8sO2dJ6nQ3rA7kE5iX1fP4lZ9hV2
    ACCESS_TOKEN_EXPIRE_MINUTES=30


#then to run the project run this command in either CMD/powershell/Terminal
   uvicorn main:app --reload



#API Usage
🔹 Register a new user
curl -X 'POST' 'http://127.0.0.1:8000/register' \
  -H 'Content-Type: application/json' \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpass"}'


🔹 Login and get a JWT token
curl -X 'POST' 'http://127.0.0.1:8000/login' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=testuser&password=testpass'


🔹 Create a new book (replace your_generated_jwt_token with the actual token)
curl -X 'POST' 'http://127.0.0.1:8000/books' \
  -H 'Authorization: Bearer your_generated_jwt_token' \
  -H 'Content-Type: application/json' \
  -d '{"title": "My First Book", "author": "John Doe"}'


🔹 Get all books
curl -X 'GET' 'http://127.0.0.1:8000/books' \
  -H 'Authorization: Bearer your_generated_jwt_token'

  
🔹 Get a specific book
curl -X 'GET' 'http://127.0.0.1:8000/books/1' \
  -H 'Authorization: Bearer your_generated_jwt_token'


🔹 Update a book
curl -X 'PUT' 'http://127.0.0.1:8000/books/1' \
  -H 'Authorization: Bearer your_generated_jwt_token' \
  -H 'Content-Type: application/json' \
  -d '{"title": "Updated Book Title", "author": "Jane Doe"}'



🔹 Delete a book
curl -X 'DELETE' 'http://127.0.0.1:8000/books/1' \
  -H 'Authorization: Bearer your_generated_jwt_token'




