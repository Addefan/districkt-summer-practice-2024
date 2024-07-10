from sqlalchemy import create_engine

from src.settings import DATABASE_URL


def get_engine():
    return create_engine(DATABASE_URL)
