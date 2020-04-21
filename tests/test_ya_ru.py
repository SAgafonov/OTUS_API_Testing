
def test_with_params(get_url, get_method, get_status):
    response = get_method(get_url)
    assert str(response.status_code) == get_status
