from app.core.config import settings
from fastapi import FastAPI
from app.routers import tables, reservations
from app.db.session import engine
from app.db.base import Base

# Для отладки — выводим текущий адрес подключения к базе данных
print("DEBUG DATABASE_URL:", repr(settings.DATABASE_URL))

# Автоматически создаём все таблицы в базе данных при запуске
Base.metadata.create_all(bind=engine)

# Создаём экземпляр FastAPI-приложения
app = FastAPI(title="Restaurant Booking API")

# Подключаем маршруты с префиксами:
# /tables - обрабатывает все действия со столами (создание, удаление)
# /reservations - обрабатывает бронирования (создание, удаление)
app.include_router(tables.router, prefix="/tables", tags=["Tables"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])

# Корневой маршрут для проверки, что API работает
@app.get("/")
async def root():
    return {"message": "Running"}