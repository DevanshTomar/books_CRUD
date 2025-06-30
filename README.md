# Books CRUD API

A simple CRUD (Create, Read, Update, Delete) API for managing books built with FastAPI. This project contains two versions of the API implementation - a basic version and an advanced version with proper data validation and error handling.

## Features

- **Full CRUD Operations**: Create, read, update, and delete books
- **Search Functionality**: Find books by title, author, category, rating, and publication date
- **Data Validation**: Input validation using Pydantic models
- **Error Handling**: Proper HTTP status codes and error responses
- **Interactive API Documentation**: Automatic OpenAPI/Swagger documentation

## Project Structure

```
books_CRUD/
├── books.py          # Basic version of the API
├── books2.py         # Advanced version with validation and error handling
├── fastapienv/       # Virtual environment
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## API Versions

### books.py (Basic Version)
Simple implementation with basic CRUD operations:
- Uses a list of dictionaries for data storage
- Basic endpoint functionality
- Minimal error handling

### books2.py (Advanced Version)
Enhanced implementation with:
- Pydantic models for data validation
- Proper HTTP status codes
- Comprehensive error handling
- Enhanced query parameters with validation
- Auto-generated unique IDs

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DevanshTomar/books_CRUD.git
   cd books_CRUD
   ```

2. **Activate the virtual environment:**
   ```bash
   source fastapienv/bin/activate  # On macOS/Linux
   # or
   fastapienv\Scripts\activate     # On Windows
   ```

3. **Install dependencies (if needed):**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

## Running the Application

### Option 1: Run the basic version
```bash
uvicorn books:app --reload
```

### Option 2: Run the advanced version
```bash
python books2.py
```
or
```bash
uvicorn books2:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- **Interactive API Documentation**: `http://localhost:8000/docs`
- **Alternative Documentation**: `http://localhost:8000/redoc`

## API Endpoints

### Basic Version (books.py)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/all` | Get all books |
| GET | `/books/{book_title}` | Get book by title |
| GET | `/books/?category={category}` | Get books by category |
| GET | `/books/author/{book_author}?category={category}` | Get books by author and category |
| GET | `/books/by_author/{book_author}` | Get books by author |
| POST | `/books/create_book` | Create a new book |
| PUT | `/books/update_book` | Update an existing book |
| DELETE | `/books/delete_book/{book_title}` | Delete a book by title |

### Advanced Version (books2.py)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Get all books |
| GET | `/books/id/{book_id}` | Get book by ID |
| GET | `/books/by_rating/?book_rating={rating}` | Get books by rating (1-5) |
| GET | `/books/by_published_date/?published_date={year}` | Get books by publication year |
| POST | `/create-book` | Create a new book |
| PUT | `/books/update_book` | Update an existing book |
| DELETE | `/book/delete_book/{book_id}` | Delete a book by ID |

## Data Models

### Basic Version
Books are stored as dictionaries with:
- `title`: Book title
- `author`: Book author
- `category`: Book category

### Advanced Version
Books use a Pydantic model with validation:
- `id`: Unique identifier (auto-generated)
- `title`: Book title (min 3 characters)
- `author`: Book author (min 1 character)
- `description`: Book description (1-100 characters)
- `rating`: Book rating (1-5)
- `published_date`: Publication year (2000-2030)

## Example Usage

### Creating a Book (Advanced Version)
```bash
curl -X POST "http://localhost:8000/create-book" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Great Book",
    "author": "Amazing Author",
    "description": "An incredible story about adventures",
    "rating": 5,
    "published_date": 2023
  }'
```

### Getting All Books
```bash
curl -X GET "http://localhost:8000/books"
```

### Getting Books by Rating
```bash
curl -X GET "http://localhost:8000/books/by_rating/?book_rating=5"
```

## Sample Data

The application comes pre-loaded with sample books including:
- The Catcher in the Rye by J.D. Salinger
- To Kill a Mockingbird by Harper Lee
- 1984 by George Orwell
- The Great Gatsby by F. Scott Fitzgerald
- The Picture of Dorian Gray by Oscar Wilde

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for running the application
- **Python 3.12**: Programming language

## Development

### Virtual Environment
The project includes a virtual environment (`fastapienv`) with all necessary dependencies pre-installed.
