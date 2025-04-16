import uuid
from fastapi import status

#  Проверка успешно ли создание столика в ресторане
def test_create_table(client):
    unique_name = f"Table-{uuid.uuid4()}"
    response = client.post("/tables/", json={"name": unique_name, "seats": 4, "location": "Window"})
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == unique_name
    assert data["seats"] == 4
    assert data["location"] == "Window"
