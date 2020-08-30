
# pytest automatically injects fixtures
# that are defined in conftest.py
# in this case, client is injected
def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["result"]["content"] == "hello world!"


def test_mirror(client):
    res = client.get("/mirror/Tim")
    assert res.status_code == 200
    assert res.json["result"]["name"] == "Tim"


def test_get_restaurants(client):
    res = client.get("/restaurants")
    assert res.status_code == 200

    res_restaurants = res.json["result"]["restaurants"]
    assert len(res_restaurants) == 3
    assert res_restaurants[0]["name"] == "Golden Harbor"


def tests_get_restaurants_with_rating(client):
    res = client.get("/restaurants?minRating=8")
    assert res.status_code == 200

    res_restaurants = res.json["result"]["restaurants"]
    assert len(res_restaurants) == 2
    assert res_restaurants[1]["name"] == "Noodles and Company"


def test_get_restaurant_id(client):
    res = client.get("/restaurants/1")
    assert res.status_code == 200

    res_restaurant = res.json["result"]
    assert res_restaurant["name"] == "Golden Harbor"
    assert res_restaurant["rating"] == 10
