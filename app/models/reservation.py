from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

# Бронь Столика
class Reservation(Base):
    __tablename__ = "reservations"

    # Уникальный идентификатор брони
    id = Column(Integer, primary_key=True, index=True)

    # Имя клиента, который сделал бронь
    customer_name = Column(String, nullable=False)

    # Внешний ключ на таблицу "tables" — связывает бронь с конкретным столиком
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)

    # Время начала бронирования
    reservation_time = Column(DateTime, nullable=False)

    # Продолжительность бронирования в минутах
    duration_minutes = Column(Integer, nullable=False)

    # Связь с моделью Table — позволяет обращаться к столу из брони: reservation.table.name и тд
    table = relationship("Table")