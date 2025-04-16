import logging

# Импортируем настройки приложения
from app.core.config import settings

# Базовая конфигурация логирования
logging.basicConfig(
    level=settings.LOG_LEVEL,  # Уровень логирования (DEBUG, INFO и тд )
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"  # Шаблон форматирования сообщений
)

# Создаем именованный логгер
logger = logging.getLogger("restaurant_booking")

# Тестовое сообщение
logger.debug("Logger initialized")