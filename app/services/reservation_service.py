from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import timedelta
from ..models.reservation import Reservation

# Функция проверяет доступность временного слота для бронирования столика
def is_slot_available(db: Session, table_id: int, start_time, duration: int):
    # Вычисляем конечное время бронирования
    end_time = start_time + timedelta(minutes=duration)

    # Запрос на проверку конфликта с другими бронированиями
    # Условия:
    # - совпадает table_id
    # - новое бронирование начинается до окончания существующего
    # - и заканчивается после начала существующего
    conflict_query = db.query(Reservation).filter(
        and_(
            Reservation.table_id == table_id,                           # тот же столик
            Reservation.reservation_time < end_time,                    # начинается до окончания нового
            (Reservation.reservation_time + timedelta(minutes=Reservation.duration_minutes)) > start_time  # заканчивается после начала нового
        )
    ).first()  # Получаем первую запись, если есть конфликт

    # Если ничего не найдено, то слот свободен
    return conflict_query is None