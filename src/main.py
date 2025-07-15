from fastapi import FastAPI
from database import Base, engine
from api.routes import router as credit_router
from api.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from autoupdate import start_scheduler, add_daily_credits
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
import os

load_dotenv()


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_ORIGIN", "*")], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key="super-secret-key") # you can change super-secret-key according to you

app.include_router(credit_router)
app.include_router(auth_router)

# manually test the autoupdate functionality
# add_daily_credits()

start_scheduler() # auto run the add_daily_credits function every 24 hours




