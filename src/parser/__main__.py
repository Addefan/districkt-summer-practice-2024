import time
from datetime import datetime, timedelta
from functools import partial

import schedule
from dateutil.relativedelta import relativedelta
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.parser.api import get_events
from src.database import get_engine
from src.models import User, AttendanceStatistic, PlatformStatistic, Event
from src.parser.cli import parse_args
from src.parser.utils import get_seconds_from_periodicity


def handle_empty_args(from_date, to_date, user_id, event_id):
    if from_date is None:
        from_date = datetime.now()

    if to_date is None:
        to_date = from_date + relativedelta(years=1)

    return from_date, to_date, user_id, event_id


def create_events(api_events):
    users, attendance_statistics, platform_statistics, events = [], [], [], []

    for api_event in api_events:
        user = {
            "id": api_event["createUser"]["id"],
            "name": api_event["createUser"]["name"],
            "second_name": api_event["createUser"]["secondName"],
            "email": api_event["createUser"]["email"],
        }
        users.append(user)

        attendance_statistic = {
            "event_id": api_event["id"],
            "new": api_event["attendance"]["NEW"],
            "other": api_event["attendance"]["OTHER"],
            "regular": api_event["attendance"]["REGULAR"],
        }
        attendance_statistics.append(attendance_statistic)

        platform_statistic = {
            "event_id": api_event["id"],
            "android": api_event["platform"]["Android"],
            "web": api_event["platform"]["Web"],
            "ios": api_event["platform"]["iOs"],
        }
        platform_statistics.append(platform_statistic)

        event = {
            "id": api_event["id"],
            "name": api_event["name"],
            "starts_at": datetime.fromisoformat(api_event["startsAt"]),
            "ends_at": datetime.fromisoformat(api_event["endsAt"]),
            "duration": timedelta(seconds=api_event["duration"]),
            "invited_count": api_event["invitedCount"],
            "invited_visited_count": api_event["invitedVisitedCount"],
            "registered_count": api_event["registeredCount"],
            "registered_visited_count": api_event["registeredVisitedCount"],
            "country": api_event["country"],
            "utms": api_event["utms"],
            "create_user_id": user["id"],
            "referrer": api_event["referrer"],
            "context": api_event["context"],
        }
        events.append(event)

    with Session(get_engine()) as session:
        session.execute(insert(User).values(users).on_conflict_do_nothing())
        session.execute(insert(Event).values(events).on_conflict_do_nothing())
        session.execute(insert(AttendanceStatistic).values(attendance_statistics).on_conflict_do_nothing())
        session.execute(insert(PlatformStatistic).values(platform_statistics).on_conflict_do_nothing())
        session.commit()


def parse_events(from_date: datetime | None = None, to_date: datetime | None = None,
                 user_id: int | None = None, event_id: int | None = None):
    from_date, to_date, user_id, event_id = handle_empty_args(from_date, to_date, user_id, event_id)
    events = get_events(from_date, to_date, user_id, event_id)
    create_events(events)


def main():
    args = parse_args()

    periodicity = get_seconds_from_periodicity(args.periodicity_unit, args.periodicity_value)
    parse_concrete_events = partial(parse_events, getattr(args, "from"), args.to, args.user_id, args.event_id)

    schedule.every(periodicity).seconds.do(parse_concrete_events)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
