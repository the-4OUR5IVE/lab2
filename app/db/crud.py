from sqlalchemy.orm import Session
from app.db import models

# --- CATEGORY CRUD ---
def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def update_category(db: Session, category_id: int, title: str):
    db_category = get_category_by_id(db, category_id)
    if db_category:
        db_category.title = title
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = get_category_by_id(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False

# --- BOOK CRUD ---
def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ""):
    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        category=category_id,
        url=url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, category_id: int = None):
    query = db.query(models.Book)
    if category_id:
        query = query.filter(models.Book.category == category_id)
    return query.all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, title: str, description: str, price: float, category_id: int, url: str):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db_book.title = title
        db_book.description = description
        db_book.price = price
        db_book.category = category_id
        db_book.url = url
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False
