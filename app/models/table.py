from sqlalchemy import Column, Integer, String
from app.db.base import Base

# Столик в ресторане
class Table(Base):
    # Название таблицы в базе данных
    __tablename__ = "tables"

    # Уникальный идентификатор столика
    id = Column(Integer, primary_key=True, index=True)

    # Название столика
    name = Column(String, unique=True, index=True, nullable=False)

    # Количество посадочных мест за столиком
    seats = Column(Integer, nullable=False)

    # Местоположение столика
    location = Column(String, nullable=False)