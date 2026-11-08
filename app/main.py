import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    try:
        print("=== СПИСОК КАТЕГОРИЙ ===")
        categories = crud.get_categories(db)
        for cat in categories:
            print(f"ID: {cat.id} | Название: {cat.title}")
            
        print("\n=== СПИСОК КНИГ В БАЗЕ ДАННЫХ ===")
        books = crud.get_books(db)
        for book in books:
            print(f"Книга: '{book.title}' | Цена: {book.price} руб. | Категория ID: {book.category}")
            print(f"Описание: {book.description}\n" + "-"*40)
            
    except Exception as e:
        print(f"Произошла ошибка при чтении: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
