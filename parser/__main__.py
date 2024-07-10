from datetime import datetime

from dateutil.relativedelta import relativedelta

from parser.api import get_events


def handle_empty_args(from_date, to_date, user_id, event_id):
    if from_date is None:
        from_date = datetime.now()

    if to_date is None:
        to_date = from_date + relativedelta(years=1)

    return from_date, to_date, user_id, event_id


def main(from_date: datetime | None = None, to_date: datetime | None = None,
         user_id: int | None = None, event_id: int | None = None):
    from_date, to_date, user_id, event_id = handle_empty_args(from_date, to_date, user_id, event_id)
    events = get_events(from_date, to_date, user_id, event_id)


if __name__ == "__main__":
    main()
