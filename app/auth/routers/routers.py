from datetime import timedelta
from fastapi import APIRouter, HTTPException, status, Body
import hashlib

from app.auth.models.models import Token
from app.auth.view.view import create_access_token
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from postgres import get_user_by_email

auth_router = APIRouter()


@auth_router.post("/login")
def login(data=Body(...)):
    user = get_user_by_email(data.get("email"))
    if user.password == hashlib.md5(data["password"].encode()).hexdigest():
        access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

