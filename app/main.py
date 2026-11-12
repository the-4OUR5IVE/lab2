from fastapi import FastAPI
from app.db.db import engine, Base
from app.api import categories, books

# Автоматически создаем таблицы в PostgreSQL при старте, если они ещё не созданы
Base.metadata.create_all(bind=engine)

# Создаем экземпляр приложения FastAPI — именно его ищет Uvicorn!
app = FastAPI(
    title="Octagon Book API",
    description="Интеграционный модуль работы с БД книг и категорий",
    version="1.0.0"
)

# Простой эндпоинт проверки работоспособности (Шаг 8)
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "alive", "database": "connected"}

# Подключаем роутеры из папки app/api (Шаг 8)
app.include_router(categories.router)
app.include_router(books.router)
