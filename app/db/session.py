from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Создание движка SQLAlchemy.
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

# Создание SessionLocal — фабрика сессий
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Зависимость для FastAPI — получение и автоматическое закрытие сессии
def get_db():
    db = SessionLocal()  # создаём новую сессию
    try:
        yield db          # передаём её вызывающему коду
    finally:
        db.close()        # сессия закрывается после завершения запроса