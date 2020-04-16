import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        required=True,
        help="Request URL"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post"],
        help="Method to execute"
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
