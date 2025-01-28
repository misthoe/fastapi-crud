from conftest import client


def test_create_student(test_db):
    response = client.post("/student/", json={"name": "John", "last_name": "Doe", "major": "math", "age": 30,
                                              "doctoral_candidate": "false"})
    assert response.status_code == 200
    assert response.json()["name"] == "John"
    assert response.json()["last_name"] == "Doe"
    assert response.json()["major"] == "math"
    assert response.json()["age"] == 30
    assert response.json()["doctoral_candidate"] == False
