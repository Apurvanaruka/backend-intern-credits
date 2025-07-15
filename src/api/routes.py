from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from schemas import CreditChange, CreditInfo, SchemaUpdate, UserCreate, UserInfo
from models import Credit, User
from sqlalchemy import text
from datetime import datetime
from utils import get_db, get_current_user
from fastapi import  HTTPException, Depends


router = APIRouter(prefix="/api", tags=["credits"])



@router.post("/users", response_model=UserInfo)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
   
    if existing_user:

        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(email=user.email, name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    new_credit = Credit(user_id=new_user.user_id, credits=0)
    db.add(new_credit)
    db.commit()

    return new_user



@router.get("/credits/{user_id}", response_model=CreditInfo)
def get_credits(user_id: int = Path(...), db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    
    credit = db.query(Credit).filter(Credit.user_id == user_id).first()
    if not credit:
        raise HTTPException(status_code=404, detail="User not found")
    return credit



@router.post("/credits/{user_id}/add")
def add_credits(user_id: int, data: CreditChange, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    credit = db.query(Credit).filter(Credit.user_id == user_id).first()
    if not credit:
        raise HTTPException(status_code=404, detail="User not found!!!")
    credit.credits += data.amount
    credit.last_updated = datetime.utcnow()
    db.commit()
    return {"message": "Credits added", "new_balance": credit.credits}



@router.post("/credits/{user_id}/deduct")
def deduct_credits(user_id: int, data: CreditChange, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    credit = db.query(Credit).filter(Credit.user_id == user_id).first()
    if not credit or credit.credits < data.amount:
        raise HTTPException(status_code=400, detail="Insufficient credits or user not found")
    credit.credits -= data.amount
    credit.last_updated = datetime.utcnow()
    db.commit()
    return {"message": "Credits deducted", "new_balance": credit.credits}



@router.patch("/credits/{user_id}/reset")
def reset_credits(user_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    credit = db.query(Credit).filter(Credit.user_id == user_id).first()
    if not credit:
        raise HTTPException(status_code=404, detail="User not found")
    credit.credits = 0
    credit.last_updated = datetime.utcnow()
    db.commit()
    return {"message": "Credits reset to zero"}

@router.post("/schema/update")
def update_schema(schema: SchemaUpdate, db: Session = Depends(get_db)):
    try:
        db.execute(text(schema.sql))
        db.commit()
        return {"message": "Schema updated"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
