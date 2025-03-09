import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Check if we are running tests
if "pytest" in sys.modules or any("test" in arg for arg in sys.argv):
    DATABASE_URL = "sqlite:///./test.db"
else:
    DATABASE_URL = "sqlite:///./dev.db"

# Create the engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
