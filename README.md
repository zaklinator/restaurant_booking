# Restaurant Booking API

API для бронирования столиков в ресторане. Проект реализован с использованием **FastAPI**, **SQLAlchemy**, **PostgreSQL**, **Alembic** и упакован в **Docker-контейнер** с помощью **docker-compose**.

## Функциональность

- **Модели:**
  - **Table** – столик в ресторане:
    - id: int
    - name: str (например, "Table 1")
    - seats: int (количество мест)
    - location: str (например, "зал у окна", "терраса")
  - **Reservation** – бронь:
    - id: int
    - customer_name: str
    - table_id: int (внешний ключ к Table)
    - reservation_time: datetime
    - duration_minutes: int


- **Эндпоинты API:**
  - **Столики:**
    - `GET /tables/` — получить список всех столиков
    - `POST /tables/` — создать новый столик
    - `DELETE /tables/{id}` — удалить столик по ID
  - **Бронирования:**
    - `GET /reservations/` — получить список всех броней
    - `POST /reservations/` — создать новую бронь
    - `DELETE /reservations/{id}` — удалить бронь по ID


- **Логика бронирования:**
  - Не допускается создание брони, если указанный столик уже забронирован на заданный временной слот.

## Технический стек

- **Backend:** FastAPI, SQLAlchemy 
- **База данных:** PostgreSQL  
- **Миграции:** Alembic  
- **Контейнеризация:** Docker и docker-compose  
- **Тестирование:** pytest

## Структура проекта

- **restaurant_booking:**
  - **app:** – основное приложение
    - **main.py:** – точка входа в FastAPI-приложение
    - **core:** – базовая конфигурация
      - `config.py` – настройки подключения к БД и другие конфигурации
      - `logger.py` – логирование
    - **models:** – модели базы данных
      - `__init__.py`
      - `table.py` – модель столика
      - `reservation.py` – модель бронирования
    - **schemas** – Pydantic-схемы
      - `__init__.py`
      - `table.py` – схемы для операций со столиками
      - `reservation.py` – схемы для операций с бронированиями
    - **routers:** – маршруты API
      - `__init__.py`
      - `tables.py` – эндпоинты для столиков
      - `reservations.py` – эндпоинты для бронирований
    - **services:** – бизнес-логика
      - `__init__.py`
      - `table_service.py` – логика управления столиками
      - `reservation_service.py` – логика бронирований
    - **db:** – база данных
      - `base.py` – декларативная база SQLAlchemy
      - `session.py` – подключение и сессия к БД
  - **alembic:** – миграции базы данных
    - `env.py- `
    - `script.py.mako- `
    - **versions:** – директория с версиями миграций
  - **tests:** – автоматические тесты
    - `conftest.py` – фикстуры для тестирования
    - `test_tables.py` – тесты API столиков
    - `test_reservations.py` – тесты API бронирований
  - **Dockerfile:** – описание Docker-образа
  - **docker-compose.yml:** – конфигурация контейнеров
  - **requirements.txt:** – список зависимостей проекта
  - **README.md:** – документация проекта

## Установка и запуск

### Локально (без Docker)

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/your_username/restaurant_booking.git
   cd restaurant_booking
   ```
2. **Создайте и активируйте виртуальное окружение:**
  - **Для Windows:**
   ```bash
    python -m venv venv
    .\venv\Scripts\activate 
   ```
  - **Для Linux/macOS:**
   ```bash
    python3 -m venv venv
    source venv/bin/activate 
   ```
3. **Установите зависимости:**
   ```bash
    pip install -r requirements.txt 
   ```
4. **Настройте базу данных:**
   **Убедитесь, что у вас установлен PostgreSQL и настроено подключение к базе данных в файле app/core/config.py.**


5. **После настройки базы данных выполните миграции:**
   ```bash
    alembic upgrade head 
   ```
   
6. **Запустите приложение:** **Для локального запуска используйте Uvicorn:**
   ```bash
    uvicorn app.main:app --reload 
   ```
   **Запуск сервера на http://127.0.0.1:8000.**

### Запуск с Docker

1. **Создайте и запустите контейнеры с помощью docker-compose:**
   ```bash
   docker-compose up --buildg
   ```
2. **Доступ к API: После запуска приложение будет доступно на http://localhost:8000.**

### Тестирование

**Для тестирования используйте pytest:**
   ```bash
   pytest
   ```

### Пример использования API

**Создать столик (POST /tables/)**
 ```bash
   {
  "name": "Table 1",
  "seats": 4,
  "location": "зал у окна"
}
   ```

**Создать бронь (POST /reservations/)**
 ```bash
   {
  "customer_name": "John Doe",
  "table_id": 1,
  "reservation_time": "2025-04-20T19:00:00",
  "duration_minutes": 60
}
   ```
