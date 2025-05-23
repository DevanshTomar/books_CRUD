from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books/all")
def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
def read_book(book_title: str):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            return book
    return {"data": "Book not found"}

@app.get("/books/")
def read_category_by_querry(category: str):
    books_to_return = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/author/{book_author}")
def read_author_category(book_author: str, category: str):
    books_to_return = []

    for book in BOOKS:
        if book["author"].casefold() == book_author.casefold() and book["category"].casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

@app.post("/books/create_book")
def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book

@app.put("/books/update_book")
def update_book(udated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == udated_book['title'].casefold():
            BOOKS[i] = udated_book
            return udated_book

@app.delete("/books/delete_book/{book_title}")
def delete_book(book_title: str):
    for i, book in enumerate(BOOKS):
        if book['title'].casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"data": "Book deleted"}

@app.get("/books/author/all/{book_author}")
def get_book_by_author(book_author: str):
    books_with_author = []

    for book in BOOKS:
        if book['author'].casefold() == book_author.casefold():
            books_with_author.append(book)
    
    return books_with_author
