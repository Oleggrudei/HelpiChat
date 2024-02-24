from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.auth.routers.routers import auth_router
from app.chat.routers.routers import chat_router
from app.user.routers.routers import user_router
from app.websocket.routers.routers import web_router

# from postgres import create_table

app = FastAPI()

# create_table()

templates = Jinja2Templates(directory="app/templates")

app.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(chat_router, prefix='/chat', tags=['chat'])
app.include_router(auth_router, prefix='/auth', tags=['auth'])
app.include_router(web_router, prefix='/web', tags=['web'])
