from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import crud
from app.db.db import get_db
from app.schemas import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Валидация: проверяем, существует ли указанная категория в БД
    db_category = crud.get_category_by_id(db, category_id=book.category)
    if not db_category:
        raise HTTPException(
            status_code=400, 
            detail=f"Категория с ID {book.category} не существует. Сначала создайте её."
        )
    return crud.create_book(
        db=db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category,
        url=book.url
    )

@router.get("/", response_model=List[BookResponse])
def read_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    # Возвращает все книги или фильтрует по ?category_id=
    return crud.get_books(db, category_id=category_id)

@router.get("/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    # Проверяем, существует ли категория, на которую меняем
    db_category = crud.get_category_by_id(db, category_id=book.category)
    if not db_category:
        raise HTTPException(status_code=400, detail="Указанная категория не существует")
        
    db_book = crud.update_book(
        db, book_id,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category,
        url=book.url
    )
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return db_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"detail": "Книга успешно удалена"}
