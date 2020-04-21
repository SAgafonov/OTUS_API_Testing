import cerberus
import pytest
import requests


def get_brewery_id(url_for_breweries) -> str:
    """
    Returns ID of the first brewery
    :param url_for_breweries: str
    :return: str
    """
    response = requests.get(url_for_breweries)
    brewery_id = response.json()[0]["id"]
    return str(brewery_id)


@pytest.mark.parametrize("param, value, code", [(None, None, 200),
                                                ("by_city", "san_diego", 200),
                                                ("by_city", "san%20diego", 200),
                                                ("by_name", "modern%20times", 200),
                                                ("by_state", "new%20mexico", 200),
                                                ("by_postal", "44107_4020", 200),
                                                ("by_tags", "patio,dog-friendly", 200)])
def test_list_breweries(url_for_breweries, param, value, code):
    response = requests.get(url_for_breweries, params={param: value})
    assert response.status_code == code


def test_get_brewery_by_id(url_for_breweries):
    schema = {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "tag_list": {"type": "list"},
    }
    v = cerberus.Validator()
    brewery_id = get_brewery_id(url_for_breweries)
    response = requests.get(url_for_breweries + "/" + brewery_id)
    assert response.status_code == 200
    assert v.validate(response.json(), schema)
    # TODO сделать проверку схемы


@pytest.mark.parametrize("query, code", [("dog", 200),
                                         ("dog%20brew", 200),
                                         ("%60", 200)])
def test_search_brewery(url_for_breweries, query, code):
    response = requests.get(url_for_breweries + "/search", params={"query": query})
    assert response.status_code == code
