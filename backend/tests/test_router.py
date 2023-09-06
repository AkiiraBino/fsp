from tests.conftest import client


def test_boundary_case():
    response = client.get("api/v1/cities/?started_city=Renton&target_city=Renton")
    assert response.status_code == 200
    assert response.json() == {
        "city": "Renton",
        "result": {"target_city": "Renton", "distance": 0},
    }


def test_normal_case():
    response = client.get("api/v1/cities/?started_city=Bellevue&target_city=Issaquah")
    assert response.status_code == 200
    assert response.json() == {
        "city": "Bellevue",
        "result": {"target_city": "Issaquah", "distance": 12},
    }


def test_non_existent_city():
    response = client.get("api/v1/cities/?started_city=Bellevue&target_city=Pupa")
    assert response.status_code == 404
    assert response.json() == {"detail": "start city or end city not found"}


def test_difference():
    response = client.get("/api/v1/cities/difference?city=Renton")
    assert response.status_code == 200
    assert response.json() == [
        {
            "city": "Renton",
            "target_city": "Factoria",
            "distance": 8,
            "difference_with_next": 4,
        },
        {
            "city": "Renton",
            "target_city": "Issaquah",
            "distance": 12,
            "difference_with_next": 0,
        },
        {
            "city": "Renton",
            "target_city": "SoDo",
            "distance": 12,
            "difference_with_next": None,
        },
    ]
