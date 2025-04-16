from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Загружаем переменные из .env
load_dotenv()


# Класс конфигурации проекта.
class Settings(BaseSettings):

    DATABASE_URL: str                          # строка подключения к базе данных
    APP_PORT: int = 8000                       # порт, на котором будет работать сервер
    LOG_LEVEL: str = "INFO"                    # уровень логирования

    # Конфигурация через model_config
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


# Создаем глобальный объект настроек
settings = Settings()

# Получаем и обрезаем пробелы у DATABASE_URL
DATABASE_URL = settings.DATABASE_URL.strip()