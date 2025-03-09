from pydantic import BaseModel, ConfigDict

# User Schema
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Book Schema
class BookCreate(BaseModel):
    title: str
    author: str

class BookResponse(BookCreate):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True) 
