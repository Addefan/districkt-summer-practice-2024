from sqlalchemy import create_engine

from src.models import Base
from src.settings import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
    print("Таблицы успешно удалены.")


if __name__ == "__main__":
    main()
