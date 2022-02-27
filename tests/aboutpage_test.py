"""This test the aboutpage"""


def test_request_example(client):
    """This makes the about page"""
    response = client.get("/")
    assert b"About me" in response.data
