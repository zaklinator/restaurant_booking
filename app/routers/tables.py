from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.table import TableCreate, TableOut
from app.db.session import get_db
from app.core.logger import logger
from app.services.table_service import (
    create_table as service_create_table,
    get_all_tables as service_get_all_tables,
    delete_table as service_delete_table
)

# Создаем роутер для работы с таблицами
router = APIRouter()

# Создание новой таблицы
@router.post("/", response_model=TableOut, status_code=201)
def create_table(payload: TableCreate, db: Session = Depends(get_db)):

    # Преобразуем данные из запроса в объект модели и создаем таблицу в базе данных
    table = service_create_table(
        db,
        name=payload.name,
        seats=payload.seats,
        location=payload.location
    )

    # Логируем создание новой таблицы
    logger.info(f"Created table {table.name}")

    return table  # Возвращаем объект таблицы после создания

# Получить все таблицы
@router.get("/", response_model=list[TableOut])
def read_tables(db: Session = Depends(get_db)):

    # Вызов сервиса для получения всех таблиц из базы данных
    return service_get_all_tables(db)

# Удалить таблицу по ID
@router.delete("/{table_id}")
def delete_table(table_id: int, db: Session = Depends(get_db)):

    # Вызов сервиса для удаления таблицы по её ID
    service_delete_table(db, table_id)

    # Логируем успешное удаление
    logger.info(f"Deleted table {table_id}")

    return {"ok": True}  # Возвращаем успешный ответ