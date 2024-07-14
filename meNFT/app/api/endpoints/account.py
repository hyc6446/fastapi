from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.account import AccountCreate, Account
from app.db.repositories import account_repository

router = APIRouter()


@router.get("/")
async def get_accounts(db: Session = Depends(get_db)):
    """
    Get all accounts
    """
    accounts = account_repository.get_accounts(db)
    return accounts


@router.get("/{user_id}")
async def get_account(user_id: int, db: Session = Depends(get_db)):
    """
    Get account by id
    """
    account = account_repository.get_account(db, user_id)
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")
    return account
@router.post("/")
async def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    """
    Create a new account
    """
    new_account = account_repository.create_account(db, account)

