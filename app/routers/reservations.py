from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from app.schemas.reservation import ReservationCreate, ReservationOut
from app.models.reservation import Reservation
from app.db.session import get_db
from app.core.logger import logger
from sqlalchemy import and_
from sqlalchemy.sql import text

# Создаем роутер для бронирований
router = APIRouter()

# Вспомогательная функция для проверки конфликтов по времени
def has_conflict(db: Session, table_id: int, start, duration: int):
    end = start + timedelta(minutes=duration)  # Вычисляем окончание бронирования

    # Проверяем, пересекается ли новое бронирование с существующими:
    # - по тому же столику (table_id)
    # - есть ли бронирования, начинающиеся до окончания нового
    # - и заканчивающиеся после начала нового
    return db.query(Reservation).filter(
        and_(
            Reservation.table_id == table_id,
            Reservation.reservation_time < end,
            (Reservation.reservation_time + (Reservation.duration_minutes * text("INTERVAL '1 minute'"))) > start
        )
    ).first() is not None


# Получить все бронирования
@router.get("/", response_model=list[ReservationOut])
def read_reservations(db: Session = Depends(get_db)):
    return db.query(Reservation).all()


# Создать новое бронирование
@router.post("/", response_model=ReservationOut)
def create_reservation(payload: ReservationCreate, db: Session = Depends(get_db)):
    # Проверка на конфликт времени бронирования
    if has_conflict(db, payload.table_id, payload.reservation_time, payload.duration_minutes):
        raise HTTPException(400, "Time slot conflict")

    # Преобразуем Pydantic-модель в dict через model_dump()
    res = Reservation(**payload.model_dump())

    # Добавляем и сохраняем бронирование в базе
    db.add(res)
    db.commit()
    db.refresh(res)

    # Логируем событие
    logger.info(f"Created reservation {res.id}")
    return res


# Удалить бронирование по ID
@router.delete("/{res_id}")
def delete_reservation(res_id: int, db: Session = Depends(get_db)):
    # Получаем бронирование по ID
    res = db.get(Reservation, res_id)
    if not res:
        raise HTTPException(404, "Reservation not found")

    # Удаляем и сохраняем изменения
    db.delete(res)
    db.commit()

    # Логируем удаление
    logger.info(f"Deleted reservation {res_id}")
    return {"ok": True}