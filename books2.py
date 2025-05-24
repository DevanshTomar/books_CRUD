from fastapi import FastAPI, Body, Path, Query, HTTPException          
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn
from starlette import status

app = FastAPI()

class Book():
    id: Optional[int] = None
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)
    
    model_config = {
        "json_schema_extra" : {
            "example": {
                "title": "A new book",
                "author": "The author",
                "description": "The description",
                "rating": 5, 
                "published_date": 2012
            }
        }
    }
        
BOOKS = [
    Book(
        id=1,
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        description="The Catcher in the Rye, written by J.D. Salinger, is a classic coming-of-age story",
        rating=5,
        published_date=1951
    ),
    Book(
        id=2,
        title="To Kill a Mockingbird",
        author="Harper Lee",
        description="To Kill a Mockingbird, written by Harper Lee, is a Pulitzer Prize-winning novel",
        rating=4,
        published_date=1960
    ),
    Book(
        id=3,
        title="1984",
        author="George Orwell",
        description="1984 is a dystopian novel written by George Orwell",
        rating=3,
        published_date=1949
    ),
    Book(
        id=4,
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="The Great Gatsby, written by F. Scott Fitzgerald, is a classic novel set in the roaring twenties",
        rating=2,
        published_date=1925
    ),
    Book(
        id=5,
        title="The Picture of Dorian Gray",
        author="Oscar Wilde",
        description="The Picture of Dorian Gray is a philosophical novel written by Oscar Wilde",
        rating=1,
        published_date=1890
    ),
]

@app.get("/books", status_code=status.HTTP_200_OK)
def read_all_books():
    return BOOKS

@app.get("/books/by_rating/", status_code=status.HTTP_200_OK)
def find_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = [book for book in BOOKS if book.rating == book_rating]
    return books_to_return
    
@app.get("/books/id/{book_id}", status_code=status.HTTP_200_OK)
def find_by_book_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/by_published_date/", status_code=status.HTTP_200_OK)
def find_book_by_published_date(published_date: int = Query(gt=1700, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return
    
@app.post("/create-book", status_code=status.HTTP_201_CREATED)
def create_book(book_request : BookRequest):
    book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(book))
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
def update_book(book: BookRequest):
    book_changes = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = Book(**book.model_dump())
            book_changes = True
        
    if not book_changes:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return book


@app.delete("/book/delete_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
        
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"data": "Item deleted"}
        

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)