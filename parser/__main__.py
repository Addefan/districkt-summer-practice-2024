from datetime import datetime

from dateutil.relativedelta import relativedelta

from parser.api import get_events


def main(from_date: datetime | None = None, to_date: datetime | None = None,
         user_id: int | None = None, event_id: int | None = None):
    if from_date is None:
        from_date = datetime.now()

    if to_date is None:
        to_date = from_date + relativedelta(years=1)

    response = get_events(from_date, to_date, user_id, event_id)

    if response.status_code == 401:
        raise Exception("Не передан токен в хэдере x-auth-token.")

    if response.status_code == 404:
        print("За указанный период не найдено ни одного мероприятия.")
        return

    events = response.json()
