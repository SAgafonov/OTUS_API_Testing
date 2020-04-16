import pytest
# import requests


@pytest.mark.parametrize("sub_url, code", [("/breeds/list/all", 200),
                                           ("/breeds/image/random", 200),
                                           ("/breeds/image/random/3", 200),
                                           ("/breed/hound/list", 200)])
def test_random_breed(get_url, sub_url, code, get_method):
    response = get_method(get_url + sub_url)
    assert response.status_code == code


# @pytest.mark.parametrize("dog, code", [("affenpinscher", 200), ("basenjd", 404)])
# def test_breeds_list(dog, code, get_method):
#     response = get_method("https://dog.ceo/api/breed/" + dog + "/images/random")
#     assert response.status_code == code
