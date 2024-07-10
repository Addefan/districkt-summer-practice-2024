from src.database import get_engine
from src.models import Base


def main():
    Base.metadata.drop_all(get_engine())
    print("Таблицы успешно удалены.")


if __name__ == "__main__":
    main()
