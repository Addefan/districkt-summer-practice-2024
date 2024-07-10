from src.database import get_engine
from src.models import Base


def main():
    Base.metadata.create_all(get_engine())
    print("Таблицы успешно созданы.")


if __name__ == "__main__":
    main()
