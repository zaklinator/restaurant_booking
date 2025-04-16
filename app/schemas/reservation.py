from pydantic import BaseModel
from datetime import datetime

# Модель для создания бронирования
class ReservationCreate(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

# Модель для вывода данных о бронировании
class ReservationOut(ReservationCreate):
    id: int

    class Config:
        orm_mode = True