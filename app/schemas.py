from pydantic import BaseModel, ConfigDict
from typing import Optional

# --- CATEGORY SCHEMAS ---
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    
    # Включаем чтение объектов SQLAlchemy ORM (замена старого orm_mode в Pydantic v2)
    model_config = ConfigDict(from_attributes=True)


# --- BOOK SCHEMAS ---
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    url: Optional[str] = ""
    category: int  # Идентификатор категории

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
