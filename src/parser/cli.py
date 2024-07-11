import argparse

from src.parser.utils import string_to_datetime


def parse_args():
    description = "Автоматический парсинг мероприятий МТС Линк с заданной периодичностью"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("periodicity_unit",
                        choices=("секунда", "минута", "час", "день", "неделя", "месяц", "год"),
                        help="единица измерения периодичности, например, час")

    parser.add_argument("periodicity_value",
                        type=int,
                        help="количество единиц времени, например, 3")

    parser.add_argument("from",
                        type=string_to_datetime,
                        nargs="?",
                        help="дата начала периода выборки, формат: ДД.ММ.ГГГГ ЧЧ:ММ:СС"
                             " (по умолчанию текущая дата и время)")

    parser.add_argument("to",
                        type=string_to_datetime,
                        nargs="?",
                        help="дата окончания периода выборки, формат: ДД.ММ.ГГГГ ЧЧ:ММ:СС"
                             " (по умолчанию from + 1 год)")

    parser.add_argument("-uid", "--user_id",
                        type=int,
                        help="идентификатор сотрудника организации,"
                             " которым нужно ограничить выборку")

    parser.add_argument("-eid", "--event_id",
                        type=int,
                        help="идентификатор мепроприятия,"
                             " о котором нужно получать информацию")

    return parser.parse_args()
