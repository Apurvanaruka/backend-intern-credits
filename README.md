
# 📚 LawVriksh Backend Intern Assignment – Credit Management API

This project is part of the LawVriksh Backend Internship assignment.  
It implements a **FastAPI** backend with **PostgreSQL** for managing user credits based on platform activities.

---

## 🚀 Features

- RESTful API using **FastAPI**
- Persistent storage with **PostgreSQL**
- Daily background job to **add 5 credits** to all users at **UTC midnight**
- Endpoints to **add**, **deduct**, **reset**, and **fetch** credits
- Provided **schema file** for easy DB setup

---

## 🛠️ Tech Stack

- **Language**: Python 3.12+
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Scheduler**: APScheduler



## 🧑‍💻 Setup Instructions

### 1️⃣ Virtual Environment

**Linux/macOS:**

```bash
python3 -m venv env
source env/bin/activate
````

**Windows:**

```cmd
python -m venv env
env\Scripts\activate


### 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```



### 3️⃣ Setup PostgreSQL Database

```bash
# Create the database
sudo -u postgres createdb creditdb

# Copy schema file to temporary directory
cp /home/hp/workspace/backend-intern-credits/src/schema.sql /tmp/schema.sql

# Create the tables from the schema
sudo -u postgres psql -d creditdb -f /tmp/schema.sql
```

---

### 4️⃣ Create `.env` File

Create a `.env` file in your `src/` directory with the following content:

```ini
GOOGLE_CLIENT_ID=YOUR_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_GOOGLE_CLIENT_SECRET
SECRET_KEY=YOUR_SECRET_KEY
DATABASE_URL=postgresql://USERNAME:PASSWORD@DATABASE_ADDRESS/DATABASE_NAME
CORS_ORIGINS=ALLOWED_ORIGINS
```

---

### 5️⃣ Run the App

```bash
cd src
uvicorn main:app --reload
```

> **Note:** `main.py` should have the `APScheduler` job initialized.

---

## 🧪 API Endpoints & Screenshots

### `GET /auth/google` — OAuth Authentication

1️⃣ Open in your browser and log in with a Google account.
2️⃣ Copy the generated Access Token.

![Login Screen](images/auth_google.png)

### After Login — Copy Access Token

![Access Token](images/accesstoken.png)

---

### Main Endpoints

* **`GET /api/credits/{user_id}`** — Get User Credits
* **`POST /api/credits/{user_id}/add`** — Add Credits
* **`POST /api/credits/{user_id}/deduct`** — Deduct Credits
* **`PATCH /api/credits/{user_id}/reset`** — Reset Credits
* **`POST /api/schema/update`** — Update Schema (optional)

---

## ⚙️ API Testing (Swagger UI)

Test the API directly using the **Swagger UI**:

```
http://localhost:8000/docs
```

---

## 🗂️ Architecture Diagram

```mermaid
graph TD
  A[Client (Browser / Postman)] -->|HTTP Requests| B[FastAPI Backend]
  B --> C[Google OAuth (Auth)]
  B --> D[PostgreSQL Database]
  B --> E[APScheduler (Daily Job)]
  E --> D
```

---

## 🔄 Flow Diagram

```mermaid
flowchart TD
    A[User] --> B[Google OAuth]
    B --> C[Access Token]
    C --> D[API Request]
    D --> E[FastAPI Handles Request]
    E --> F[PostgreSQL DB]
    F --> G[Response]
```

---

## ⏰ Scheduled Task

* Runs daily at **midnight UTC**
* Adds **5 credits** to every user
* Updates the `last_updated` column accordingly

---

## 📂 Project Structure

```
backend-intern-credits/
├── src/
│   ├── api/
│   │   ├── auth.py
│   │   └── routes.py
│   ├── autoupdate.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── utils.py
│   ├── LawVriksh_Credit_API.postman_collection.json
│   ├── requirements.txt
│   └── schema.sql
├── images/
│   ├── auth_google.png
│   ├── accesstoken.png
├── .gitignore
└── README.md
```

---

## ✅ Deliverables

* `src/` folder with complete source code
* `schema.sql` for easy DB setup
* Postman Collection for endpoint testing

---

## ✍️ Author

**Apurva Singh**
📧 [apurvanaruka1@gmail.com](mailto:apurvanaruka1@gmail.com)

---
