from starlette import status

from postgres import create_user_for_chat, select_all_chat_user, select_one_chat_user, delete_chat_user, \
    update_user_state, select_all_state_user


def create_users_for_chat(operator_id: str, client_id: str, state=str):
    """
    Create users from DB (Postgres)
    """
    try:
        return create_user_for_chat(operator_id, client_id, state)
    except Exception as e:
        print(e)
        return status.HTTP_400_BAD_REQUEST


def get_all_user_for_chat():
    """
    Get all users from DB (Postgres)
    """
    return select_all_chat_user()


def get_user_chat_by_id(user_id: int):
    """
    Get user by id from DB (Postgres)
    """
    return select_one_chat_user(user_id)


def delete_user_chat_by_id(user_id: int):
    """
    Delete user by id from DB (Postgres)
    """
    try:
        delete_chat_user(user_id)
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(e)
        return status.HTTP_404_NOT_FOUND


# update_user_status

def update_user_state_by_id(chat_id: int, state: str):
    """
    Update user state by id from DB (Postgres)
    """
    try:
        return update_user_state(chat_id, state)
    except Exception as e:
        print(e)
        return status.HTTP_400_BAD_REQUEST


def get_all_state_user(state: str):
    """
    Get all state user from DB (Postgres)
    """
    return select_all_state_user(state)
