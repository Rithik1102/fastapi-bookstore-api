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

## **📥 Installation**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/ohangbon/fastapi-bookstore-api.git
cd fastapi-bookstore-api

Set Up a Virtual Environment
For Windows CMD/powershell
   python -m venv venv
   venv\Scripts\activate


For Linux/macOS:
   python3 -m venv venv
   source venv/bin/activate


Install Dependencies
   pip install -r requirements.txt

run it
   uvicorn main:app --reload
