# LawVriksh Backend Intern Assignment – Credit Management API

This project is part of the LawVriksh Backend Internship assignment.
It implements a FastAPI-based backend with PostgreSQL for tracking user credits for platform activities.

---

## 🚀 Features

* RESTful API using **FastAPI**
* Persistent storage with **PostgreSQL**
* Daily background job to add 5 credits to all users at **UTC midnight**
* Endpoints to **add**, **deduct**, **reset**, and **fetch** credits
* Schema file for easy table creation

---

## 🛠️ Tech Stack

* **Language**: Python 3.12+
* **Framework**: FastAPI
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Scheduler**: APScheduler

---

## 🧑‍💻 Setup Instructions

### 🧪 Virtual Environment

#### On Linux/macOS:

```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:

```cmd
python -m venv env
env\Scripts\activate
```

### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### 🐘 Setup PostgreSQL Database

```bash
# Create the database
sudo -u postgres createdb creditdb

# Copy schema file to temporary directory
cp /home/hp/workspace/backend-intern-credits/src/schema.sql /tmp/schema.sql

# Create the tables from the schema
sudo -u postgres psql -d creditdb -f /tmp/schema.sql
```

### 🔐 Create .env File

Create a `.env` file in your `src/` directory with the following content:

```ini
GOOGLE_CLIENT_ID=YOUR_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_GOOGLE_CLIENT_SECRET
SECRET_KEY=YOUR_SECRET_KEY
DATABASE_URL=postgresql://USERNAME:PASSWORD@DATABASE_ADDRESS/DATABASE_NAME
CORS_ORIGINS=ALLOWED_ORIGINS
```

### ▶️ Run the App

```bash
cd src
uvicorn main:app --reload
```

> **Note:** `main.py` should have `APScheduler` job initialized.

---

## 🧪 API Endpoints & CURL Requests
### 'GET /auth/google - Oauth authentication 
Go to browers and login using any google account
Copy Access Token 
![Alt Text](images/auth_google.png)

## After Login copy access token
![Alt Text](images/accesstoken.png)


### `GET /api/credits/{user_id}` – Get User Credits

### `POST /api/credits/{user_id}/add` – Add Credits

### `POST /api/credits/{user_id}/deduct` – Deduct Credits

### `PATCH /api/credits/{user_id}/reset` – Reset Credits

### `POST /api/schema/update` – Update Schema (optional)

---

---
### API Testing
## Swagger UI 
```
http://localhost:8000/docs
```

---

## ⏰ Scheduled Task

* A background job runs daily at **midnight UTC**
* It adds **5 credits to all users**
* Updates `last_updated` column accordingly

---

## 📂 Project Structure

```
backend-intern-credits/
├── src/
|   |─────api/
|   |      |── auth.py
|   |      └── routes.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── autoupdate.py
│   ├── utils.py
│   ├── LawVriksh_Credit_API.postman_collection.json
│   ├── requirements.txt
│   └── schema.sql
|── .gitignore
└── README.md
```

---

## ✅ Deliverables

* `src/` folder with all source code
* `schema.sql` for DB setup
* Postman Collection (manually test endpoints and export collection)
* Report (optional PDF or markdown)

---

## 📌 Author

Apurva singh
apurvanaruka1@gmail.com

---

