# МТС Линк API

## [Статистика по мероприятиям](https://help.mts-link.ru/ru/articles/3149503-%D0%B2%D1%8B%D0%B3%D1%80%D1%83%D0%B7%D0%B8%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D1%83-%D0%BF%D0%BE-%D0%BC%D0%B5%D1%80%D0%BE%D0%BF%D1%80%D0%B8%D1%8F%D1%82%D0%B8%D1%8F%D0%BC)

### Описание
Автоматический периодический парсинг статистики по мероприятиям, её сохранение в базу данных PostgreSQL.

### Запуск

**Примечание.** Для работы требуется **[Python](https://www.python.org/downloads/)** и **[Poetry](https://python-poetry.org/docs/)**.

1. Активировать виртуальное откружение - `poety shell`
2. Установить зависимости - `poetry install`
3. Поднять базу данных - `docker compose up -d`
4. 
