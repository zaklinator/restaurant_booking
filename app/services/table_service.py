from sqlalchemy import select, exists
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.table import Table
from app.models.reservation import Reservation


# Получение всех столов
def get_all_tables(db: Session):
    return db.query(Table).all()


# Создание нового стола
def create_table(db: Session, name: str, seats: int, location: str):
    # Проверка на существование стола с таким именем
    stmt = select(exists().where(Table.name == name))
    table_exists = db.execute(stmt).scalar()

    if table_exists:
        raise HTTPException(status_code=400, detail="Table with this name already exists")

    new_table = Table(name=name, seats=seats, location=location)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table


# Удаление стола
def delete_table(db: Session, table_id: int):
    tbl = db.get(Table, table_id)
    if tbl is None:
        raise HTTPException(status_code=404, detail="Table not found")

    # Проверка на наличие бронирований
    stmt = select(exists().where(Reservation.table_id == table_id))
    has_reservations = db.execute(stmt).scalar()

    if has_reservations:
        raise HTTPException(status_code=400, detail="Cannot delete table with existing reservations")

    db.delete(tbl)
    db.commit()