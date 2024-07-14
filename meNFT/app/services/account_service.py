
from sqlalchemy.orm import Session
from app.schemas.account import AccountCreate,AccountInDB
from app.db.repositories import account_repository
import random
import hashlib
class AccountService:
    def __init__(self, db: Session):
        self.db = db


    def generate_salt(self):
        sign = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        salt = "".join(random.choice(sign) for i in range(8))
        return salt
    def hash_password(self, password, salt):
        hashed_password = hashlib.sha256((password+salt).encode()).hexdigest()
        return hashed_password

    def create_account(self, account: AccountCreate):
        salt = self.generate_salt()
        hashed_password = self.hash_password(account.password, salt)
        account.password.set_secret_value(hashed_password)
        db_account = AccountInDB(**account.dict())
        db_account.password = account.password.get_secret_value()
        # create account in database

        account_repository.create_account(db=self.db, account=db_account)