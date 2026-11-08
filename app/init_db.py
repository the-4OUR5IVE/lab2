import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import engine, Base, SessionLocal
from app.db import crud

def init():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        cat_fiction = crud.create_category(db, title="Фантастика")
        cat_science = crud.create_category(db, title="Наука и IT")
        
        crud.create_book(db, "Дюна", "Культовая космоопера Фрэнка Герберта", 850.00, cat_fiction.id)
        crud.create_book(db, "Основание", "Классика от Айзека Азимова", 720.50, cat_fiction.id)
        
        crud.create_book(db, "Грокаем алгоритмы", "Иллюстрированное пособие для программистов", 1200.00, cat_science.id)
        crud.create_book(db, "Чистый код", "Создание, анализ и рефакторинг кода", 1500.00, cat_science.id)
        
        print("База данных успешно инициализирована тестовыми данными!")
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init()
