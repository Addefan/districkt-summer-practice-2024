class RequestError(Exception):
    """Raise for errors in requests to the MTS Link API."""


def handle_errors(status_code):
    if status_code == 400:
        print("Один или несколько параметров переданы в неверном формате.")
        return 1

    if status_code == 401:
        raise RequestError("Не передан токен в хэдере x-auth-token.")

    if status_code == 403:
        raise RequestError("Передан неправильный или неактивный токен.")

    if status_code == 404:
        print("За указанный период не найдено ни одного мероприятия.")
        return 1

    return 0
