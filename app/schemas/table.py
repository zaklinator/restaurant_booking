from pydantic import BaseModel, ConfigDict

# Модель для создания нового столика
class TableCreate(BaseModel):
    name: str
    seats: int
    location: str

# Модель для вывода информации о столике, включает id и унаследует все поля из TableCreate
class TableOut(TableCreate):
    id: int

    # Конфигурация для работы с SQLAlchemy (чтобы модель могла работать с ORM)
    class Config:
        orm_mode = True

# Модель для простого отображения информации о столике (например, в списках)
class TableSchema(BaseModel):
    id: int
    name: str

# Конфигурация модели для использования атрибутов модели при её создании
model_config = ConfigDict(from_attributes=True)