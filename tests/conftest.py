import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        required=False,
        help="Request URL"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post"],
        required=False,
        help="Method to execute"
    )

    parser.addoption(
        "--status_code",
        default="200",
        required=False,
        help="Response status code"
    )


@pytest.fixture
def get_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def get_method(request):
    m = request.config.getoption("--method")
    if m == "get":
        return requests.get
    elif m == "post":
        return requests.post


@pytest.fixture
def get_status(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def url_dog_api_list_of_breeds():
    return "https://dog.ceo/api/breeds"


@pytest.fixture
def url_dog_api_one_breed():
    return "https://dog.ceo/api/breed"


@pytest.fixture
def url_for_breweries():
    return "https://api.openbrewerydb.org/breweries"


@pytest.fixture
def url_for_jsonplaceholder():
    return "https://jsonplaceholder.typicode.com/posts"


@pytest.fixture
def body_for_jsonplaceholder():
    return {
      "title": "foo",
      "body": "bar",
      "userId": 1
    }
