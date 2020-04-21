import cerberus
import pytest
import requests


@pytest.mark.parametrize("sub_url, code", [("/list/all", 200),
                                           ("/image/random", 200),
                                           ("/image/random/3", 200)])
def test_check_breeds_urls(url_dog_api_list_of_breeds, sub_url, code):
    response = requests.get(url_dog_api_list_of_breeds + sub_url)
    assert response.status_code == code


@pytest.mark.parametrize("sub_url, code", [("/hound/images", 200),
                                           ("/hound/images/random", 200),
                                           ("/hound/images/random/3", 200),
                                           ("/hound/list", 200),
                                           ("/hound/afghan/images", 200),
                                           ("/hound/afghan/images/random", 200),
                                           ("/hound/afghan/images/random/3", 200)])
def test_check_breed_urls(url_dog_api_one_breed, sub_url, code):
    response = requests.get(url_dog_api_one_breed + sub_url)
    assert response.status_code == code


def test_list_all_breeds(url_dog_api_one_breed):
    schema = {
        "message": {"type": "list"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    response = requests.get(url_dog_api_one_breed + "/hound/images")
    assert v.validate(response.json(), schema)


@pytest.mark.parametrize("dog, code", [("/affenpinscher", 200), ("/basenjd", 404)])
def test_breeds_list(url_dog_api_one_breed, dog, code):
    response = requests.get(url_dog_api_one_breed + dog + "/images/random")
    assert response.status_code == code

