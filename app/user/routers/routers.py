from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from app.auth.view.view import get_current_user
from app.user.models.models import HumanDetails, EmailPasswordDetails
from app.user.view.view import get_user_by_id, delete_user_by_id, create_users, update_user_age, \
    update_user_info, get_all_user
from postgres import get_user_by_email

user_router = APIRouter()


# templates = Jinja2Templates(directory="app/templates")


@user_router.get("/", response_model=List[HumanDetails])
def get_all_users(current_user: HumanDetails = Depends(get_current_user)):
    users = get_all_user()
    return users


@user_router.get("/{user_id}", response_model=HumanDetails)
def get_user_id(user_id: int, current_user: HumanDetails = Depends(get_current_user)):
    return get_user_by_id(user_id)


@user_router.post("/create", response_model=HumanDetails)
def create_user(data=Body(...)):
    user = get_user_by_email(data.get("email"))
    if user and user.email == data.get("email"):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    else:
        return create_users(name=data["name"], lastname=data["lastname"], password=data['password'],
                            email=data["email"],
                            age=data["age"], is_married=data["is_married"], role=data["role"], tg_id=data["tg_id"])


@user_router.post("/update/age/{user_id}", response_model=HumanDetails)
def update_user_age_by_id(user_id, data=Body(...), current_user: HumanDetails = Depends(get_current_user)):
    return update_user_age(user_id, data.get("age"))


@user_router.post("/email", response_model=EmailPasswordDetails)
def get_email(data=Body(...), current_user: HumanDetails = Depends(get_current_user)):
    return get_user_by_email(data.get("email"))


@user_router.post("/update/info/{user_id}", response_model=HumanDetails)
def update_users(user_id: int, data=Body(...), current_user: HumanDetails = Depends(get_current_user)):
    return update_user_info(user_id, data.get("name"), data.get("lastname"))


@user_router.delete("/delete/{user_id}")
def delete_user_id(user_id: int, current_user: HumanDetails = Depends(get_current_user)):
    return delete_user_by_id(user_id)
