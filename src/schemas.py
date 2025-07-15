from pydantic import BaseModel
from datetime import datetime

class CreditChange(BaseModel):
    amount: int

class CreditInfo(BaseModel):
    user_id: int
    credits: int
    last_updated: datetime

class SchemaUpdate(BaseModel):
    sql: str


class UserCreate(BaseModel):
    email: str
    name: str

class UserInfo(BaseModel):
    user_id: int
    email: str
    name: str

    class Config:
        orm_mode = True