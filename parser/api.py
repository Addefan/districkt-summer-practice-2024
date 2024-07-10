import requests

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

    return requests.get(url, headers=headers, params=params)


