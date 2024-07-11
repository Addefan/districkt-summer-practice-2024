import requests

from src.parser.errors import handle_errors
from src.settings import API_TOKEN


def get_events(from_date, to_date, user_id, event_id):
    url = "https://userapi.mts-link.ru/v3/stats/events"

    params = {
        "from": from_date.strftime("%Y-%m-%d+%H:%M:%S"),
        "to": to_date.strftime("%Y-%m-%d+%H:%M:%S"),
        "userId": user_id,
        "eventId": event_id,
    }

    headers = {
        "x-auth-token": API_TOKEN,
    }

    response = requests.get(url, headers=headers, params=params)
    has_error = handle_errors(response.status_code)

    return [] if has_error else response.json()
