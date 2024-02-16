from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Body, Query, Depends

from app.auth.view.view import get_current_user
from app.chat.models.models import ChatsDetails
from app.chat.view.view import create_users_for_chat, get_all_user_for_chat, get_user_chat_by_id, \
    delete_user_chat_by_id, update_user_state_by_id, get_all_state_user

chat_router = APIRouter()


@chat_router.post("/create", response_model=ChatsDetails)
def create_chat(data=Body(...), current_user: ChatsDetails = Depends(get_current_user)):
    return create_users_for_chat(operator_id=data["operator_id"], client_id=data["client_id"], state=data["state"])


@chat_router.get("/", response_model=List[ChatsDetails])
def get_all_users(current_user: ChatsDetails = Depends(get_current_user)):
    users = get_all_user_for_chat()
    return users


@chat_router.get("/{user_id}", response_model=ChatsDetails)
def get_users_chat_by_id(user_id: int, current_user: ChatsDetails = Depends(get_current_user)):
    return get_user_chat_by_id(user_id)


@chat_router.get("/info/", response_model=List[ChatsDetails])
def get_all_state_users(state: str = Query(...), current_user: ChatsDetails = Depends(get_current_user)):
    return get_all_state_user(state)


@chat_router.post("/update/state/{user_id}", response_model=ChatsDetails)
def update_users_state_by_id(user_id, data=Body(...), current_user: ChatsDetails = Depends(get_current_user)):
    # print( update_user_state_by_id(user_id, data.get("state")))
    return update_user_state_by_id(user_id, data.get("state"))


@chat_router.delete("/delete/{user_id}")
def delete_users_chat_by_id(user_id: int, current_user: ChatsDetails = Depends(get_current_user)):
    return delete_user_chat_by_id(user_id)
