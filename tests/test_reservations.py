from fastapi import status
from datetime import datetime, timezone
import uuid

# Проверка логики предотвращения конфликтов при бронировании столика
def test_reservation_conflict(client):
    unique_name = f"T2-{uuid.uuid4()}"
    response = client.post("/tables/", json={"name": unique_name, "seats": 2, "location": "Patio"})
    assert response.status_code == status.HTTP_201_CREATED
    table_id = response.json()["id"]

    start = datetime.now(timezone.utc).isoformat()

    resp1 = client.post("/reservations/", json={
        "customer_name": "Alice",
        "table_id": table_id,
        "reservation_time": start,
        "duration_minutes": 60
    })
    assert resp1.status_code == status.HTTP_200_OK

    resp2 = client.post("/reservations/", json={
        "customer_name": "Bob",
        "table_id": table_id,
        "reservation_time": start,
        "duration_minutes": 30
    })
    assert resp2.status_code == status.HTTP_400_BAD_REQUEST