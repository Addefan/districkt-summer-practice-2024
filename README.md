# МТС Линк API

## [Статистика по мероприятиям](https://help.mts-link.ru/ru/articles/3149503-%D0%B2%D1%8B%D0%B3%D1%80%D1%83%D0%B7%D0%B8%D1%82%D1%8C-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D1%83-%D0%BF%D0%BE-%D0%BC%D0%B5%D1%80%D0%BE%D0%BF%D1%80%D0%B8%D1%8F%D1%82%D0%B8%D1%8F%D0%BC)

### Описание
Автоматический периодический парсинг статистики по мероприятиям, её сохранение в базу данных PostgreSQL.

### Запуск

**Примечание.** Для работы требуется **[Python](https://www.python.org/downloads/) (не ниже 3.10)** и **[Poetry](https://python-poetry.org/docs/)**.

0. Добавить переменную `API_TOKEN` в файл `.env` в корне проекта
1. Активировать виртуальное откружение - `poety shell`
2. Установить зависимости - `poetry install`
3. Поднять базу данных - `docker compose up -d`
4. Создать таблицы в базе данных - `python -m src.database.createtables`
5. Запустить скрипт - `python -m src.parser [-uid USER_ID] [-eid EVENT_ID] {секунда,минута,час,день,неделя,месяц,год} periodicity_value [from] [to]`

Вызов справки по параметрам скрипта: `python -m src.parser -h` или `python -m src.parser --help`  
Пример запуска: `python -m src.parser час 3 "01.01.2024 00:00:00"`

#### [Дашборд в Yandex DataLens с некоторой статистикой на основании данных с API от 01.01.2024 00:00:00 до 10.07.2024 00:00:00](https://datalens.yandex/ulx5vdyex5cuh)