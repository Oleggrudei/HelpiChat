from fastapi import status

from postgres import select_one_human, select_all_human, delete_human, create_human, update_human_age, \
    update_human


# templates = Jinja2Templates(directory="app/templates")

def create_users(name: str, lastname: str, password: str, email: str, age: int, is_married: bool, role: str, tg_id: str):
    """
    Create user from DB (Postgres)
    """
    try:
        return create_human(name, lastname, password, email, age, is_married, role, tg_id)
    except Exception as e:
        print(e)
        return status.HTTP_400_BAD_REQUEST


def get_all_user():
    """
    Get all users from DB (Postgres)
    """
    return select_all_human()


def get_user_by_id(user_id: int):
    """
    Get user by id from DB (Postgres)
    """
    return select_one_human(user_id)


def delete_user_by_id(user_id: int):
    """
    Delete user by id from DB (Postgres)
    """
    try:
        delete_human(user_id=user_id)
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(e)
        return status.HTTP_404_NOT_FOUND


def update_user_age(user_id: int, age: int):
    """
    Update user age by id from DB (Postgres)
    """
    try:
        return update_human_age(user_id, age)
    except Exception as e:
        print(e)
        return status.HTTP_400_BAD_REQUEST


def update_user_info(user_id: int, name: str, lastname: str):
    """
    Update user info by id from DB (Postgres)
    """
    try:
        return update_human(user_id, name, lastname)
    except Exception as e:
        print(e)
        return status.HTTP_400_BAD_REQUEST
