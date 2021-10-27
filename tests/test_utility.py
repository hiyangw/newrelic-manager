from lib.utility.utility import check_api_key, check_function, check_api, check_id

API_KEY = "xxx"


def test_check_api_key_is_set(monkeypatch):
    monkeypatch.setenv("NEW_RELIC_API_KEY", API_KEY)
    api_key = check_api_key()
    assert api_key == API_KEY


def test_check_function():
    assert check_function("dashboards", "list") == "list"


def test_check_api():
    assert check_api("dashboards") == "dashboards"


def test_check_id():
    parameters = {
        "id": "123,123"
    }
    assert check_id(parameters) == list(["123", "123"])
