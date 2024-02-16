import hashlib
from datetime import datetime
from sqlalchemy import MetaData, select

from app.chat.models.models import Chats, ChatsDetails
from app.user.models.models import Human, HumanDetails, EmailPasswordDetails
from database import engine, session_factory, Base

metadata_obj = MetaData()


def create_table():
    engine.echo = False
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine, tables=[Human.__table__, Chats.__table__])
    engine.echo = True


# CRUD User


def create_human(name: str, lastname: str, password: str, email: str, age: int, is_married: bool, role: str,
                 tg_id: str):
    with session_factory() as session:
        humans = Human(name=name, lastname=lastname, password=hashlib.md5(password.encode()).hexdigest(), email=email,
                       age=age,
                       is_married=is_married,
                       role=role, register_date=datetime.now(), tg_id=tg_id)
        session.add(humans)
        session.commit()
        human_details = HumanDetails(
            id=humans.id,
            name=humans.name,
            lastname=humans.lastname,
            email=humans.email,
            password=humans.password,
            age=humans.age,
            is_married=humans.is_married,
            role=humans.role,
            register_date=humans.register_date,
            tg_id=humans.tg_id
        )

        return human_details


def select_all_human():
    with session_factory() as session:
        query = select(Human)
        result = session.execute(query)
        humans = result.scalars().all()

        human_details = [
            HumanDetails(
                id=human.id,
                name=human.name,
                lastname=human.lastname,
                password=human.password,
                email=human.email,
                age=human.age,
                is_married=human.is_married,
                role=human.role,
                register_date=human.register_date,
                tg_id=human.tg_id
            )
            for human in humans
        ]

        return human_details


def get_user_by_email(user_email):
    with session_factory() as session:
        human_info = session.query(Human).filter(Human.email == user_email).first()
        if not human_info:
            return None

        email_details = EmailPasswordDetails(
            email=human_info.email,
            password=human_info.password,
        )

        return email_details


def select_one_human(user_id):
    with session_factory() as session:
        human_info = session.get(Human, user_id)

        if not human_info:
            return None

        user_details = HumanDetails(
            id=human_info.id,
            name=human_info.name,
            lastname=human_info.lastname,
            password=human_info.password,
            email=human_info.email,
            age=human_info.age,
            is_married=human_info.is_married,
            role=human_info.role,
            register_date=human_info.register_date,
            tg_id=human_info.tg_id
        )

        return user_details


def delete_human(user_id: int):
    with session_factory() as session:
        db_info = session.get(Human, user_id)
        session.delete(db_info)
        session.commit()


def update_human_age(user_id=int, new_age=int):
    with session_factory() as session:
        human_info = session.get(Human, user_id)
        human_info.age = new_age
        session.commit()
        human_details = HumanDetails(
            id=human_info.id,
            name=human_info.name,
            lastname=human_info.lastname,
            password=human_info.password,
            email=human_info.email,
            age=human_info.age,
            is_married=human_info.is_married,
            role=human_info.role,
            register_date=human_info.register_date,
            tg_id=human_info.tg_id
        )

        return human_details


def update_human(user_id: int, new_name: str = None, new_lastname: str = None):
    with session_factory() as session:
        human_info = session.get(Human, user_id)

        if new_name is not None:
            human_info.name = new_name
        if new_lastname is not None:
            human_info.lastname = new_lastname

        session.commit()

        human_details = HumanDetails(
            id=human_info.id,
            name=human_info.name,
            lastname=human_info.lastname,
            password=human_info.password,
            email=human_info.email,
            age=human_info.age,
            is_married=human_info.is_married,
            role=human_info.role,
            register_date=human_info.register_date,
            tg_id=human_info.tg_id
        )

        return human_details


#                                   ----------CRUD Chat----------

def create_user_for_chat(operator_id=str, client_id=str, state=str):
    with session_factory() as session:
        chats = Chats(client_id=client_id, operator_id=operator_id, state=state, open_date=datetime.now(),
                      close_date=datetime.now())
        session.add(chats)
        session.commit()
        chat_details = ChatsDetails(
            chat_id=chats.chat_id,
            operator_id=chats.operator_id,
            client_id=chats.client_id,
            state=chats.state,
            open_date=chats.open_date,
            close_date=chats.close_date
        )

        return chat_details


def select_all_chat_user():
    with session_factory() as session:
        query = select(Chats)
        result = session.execute(query)
        chats = result.scalars().all()

        chat_details = [
            ChatsDetails(
                chat_id=chat.chat_id,
                operator_id=chat.operator_id,
                client_id=chat.client_id,
                state=chat.state,
                open_date=chat.open_date,
                close_date=chat.close_date
            )
            for chat in chats
        ]

        return chat_details


def select_one_chat_user(chat_id):
    with session_factory() as session:
        chat_info = session.get(Chats, chat_id)

        if not chat_info:
            return None

        chat_details = ChatsDetails(
            chat_id=chat_info.chat_id,
            operator_id=chat_info.operator_id,
            client_id=chat_info.client_id,
            state=chat_info.state,
            open_date=chat_info.open_date,
            close_date=chat_info.close_date
        )

        return chat_details


def update_user_state(user_id: int, new_state: str):
    with session_factory() as session:
        chat_info = session.get(Chats, user_id)

        if not chat_info:
            return None

        chat_info.state = new_state

        chat_details = ChatsDetails(
            chat_id=chat_info.chat_id,
            operator_id=chat_info.operator_id,
            client_id=chat_info.client_id,
            state=chat_info.state,
            open_date=chat_info.open_date,
            close_date=chat_info.close_date
        )

        return chat_details


def select_all_state_user(state: str):
    with session_factory() as session:
        chats_info = session.query(Chats).filter_by(state=state).all()

        chat_details = [
            ChatsDetails(
                chat_id=chat_info.chat_id,
                operator_id=chat_info.operator_id,
                client_id=chat_info.client_id,
                state=chat_info.state,
                open_date=chat_info.open_date,
                close_date=chat_info.close_date
            )
            for chat_info in chats_info
        ]

        return chat_details


def delete_chat_user(user_id: int):
    with session_factory() as session:
        chat_info = session.get(Chats, user_id)
        session.delete(chat_info)
        session.commit()
