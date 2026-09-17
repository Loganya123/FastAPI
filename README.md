# Library API

A simple RESTful API for managing a library's book collection, built with **FastAPI** and **Pydantic**. It supports full CRUD operations (Create, Read, Update, Delete) on an in-memory list of books.

## Features

- List all books in the library
- Retrieve a single book by ID
- Add a new book
- Update an existing book's details
- Delete a book from the library
- Automatic request/response validation via Pydantic
- Interactive API documentation (Swagger UI & ReDoc) generated automatically by FastAPI

## Tech Stack

- **Python 3**
- **FastAPI** — web framework for building the API
- **Pydantic** — data validation and modeling
- **Uvicorn** — ASGI server used to run the app

## Project Structure

```
.
├── main.py        # Application entry point: models, in-memory data, and routes
└── README.md       # Project documentation
```

## Data Model

Each book is represented by the `Book` model:

| Field       | Type    | Description                          |
|-------------|---------|---------------------------------------|
| `id`        | int     | Unique identifier for the book        |
| `title`     | str     | Title of the book                     |
| `author`    | str     | Author of the book                    |
| `price`     | float   | Price of the book                     |
| `category`  | str     | Genre/category (e.g. Fiction, Fantasy)|
| `available` | bool    | Whether the book is currently available |

The application starts with a preloaded list of 10 sample books stored in memory (the `library` list). Since storage is in-memory, all data resets whenever the server restarts.

## Installation

1. **Clone or download the project files.**

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application

Start the development server with Uvicorn:

```bash
uvicorn main:app --reload
```

- `main` refers to the `main.py` file.
- `app` refers to the `FastAPI()` instance created inside it.
- `--reload` enables auto-reloading when code changes (useful during development).

By default, the API will be available at:

```
http://127.0.0.1:8000
```

## Interactive API Documentation

FastAPI automatically generates interactive docs. Once the server is running, visit:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

These let you explore and test every endpoint directly from the browser.

## API Endpoints

### 1. Get All Books
```
GET /books
```
Returns the full list of books currently in the library.

**Example response:**
```json
[
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 10.99,
    "category": "Fiction",
    "available": true
  },
  ...
]
```

### 2. Get a Book by ID
```
GET /books/{book_id}
```
Returns a single book matching the given `book_id`.

**Example:** `GET /books/1`

**Response if found:**
```json
{
  "message": "Book found",
  "book": { "id": 1, "title": "The Great Gatsby", ... }
}
```

**Response if not found:**
```json
{ "message": "Book not found in library" }
```

### 3. Add a New Book
```
POST /books
```
Adds a new book to the library. The request body must match the `Book` model.

**Example request body:**
```json
{
  "id": 11,
  "title": "Brave New World",
  "author": "Aldous Huxley",
  "price": 13.50,
  "category": "Dystopian",
  "available": true
}
```

**Response:**
```json
{
  "message": "Book added successfully",
  "book": { "id": 11, "title": "Brave New World", ... }
}
```

### 4. Update a Book
```
PUT /books/{book_id}
```
Replaces the book matching `book_id` with the new data provided in the request body (full replacement, not a partial update).

**Example:** `PUT /books/1` with an updated `Book` payload.

**Response if found:**
```json
{
  "message": "Book updated successfully",
  "book": { ...updated book data... }
}
```

**Response if not found:**
```json
{ "message": "Book not found in library" }
```

### 5. Delete a Book
```
DELETE /books/{book_id}
```
Removes the book matching `book_id` from the library.

**Response if found:**
```json
{
  "message": "Book deleted successfully",
  "book": { ...deleted book data... }
}
```

**Response if not found:**
```json
{ "message": "Book not found in library" }
```

## Example Usage with cURL

```bash
# Get all books
curl http://127.0.0.1:8000/books

# Get a single book
curl http://127.0.0.1:8000/books/1

# Add a new book
curl -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{"id":11,"title":"Brave New World","author":"Aldous Huxley","price":13.50,"category":"Dystopian","available":true}'

# Update a book
curl -X PUT http://127.0.0.1:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"id":1,"title":"The Great Gatsby (Updated)","author":"F. Scott Fitzgerald","price":9.99,"category":"Fiction","available":false}'

# Delete a book
curl -X DELETE http://127.0.0.1:8000/books/1
```

## Known Limitations / Notes

- **In-memory storage:** Data is not persisted; restarting the server resets the library to its original 10-book seed list. A real deployment would need a database (e.g. SQLite, PostgreSQL) behind it.
- **No duplicate/ID validation:** The `POST` and `PUT` endpoints don't currently check whether an `id` already exists or enforce uniqueness.
- **No proper HTTP status codes:** Not-found and error cases currently return `200 OK` with a message body rather than standard codes like `404 Not Found`. Consider raising `HTTPException` for more RESTful behavior.
- **No authentication:** All endpoints are open with no access control.

## Possible Future Improvements

- Replace in-memory `library` list with a real database and an ORM (e.g. SQLAlchemy)
- Add proper HTTP status codes using FastAPI's `HTTPException`
- Add pagination, filtering, and search (e.g. filter by category or availability)
- Add partial update support via `PATCH`
- Add unit tests (e.g. with `pytest` and `httpx`/`TestClient`)
- Add authentication and authorization

## License

This project is provided as-is for educational/demo purposes. Add a license of your choice if distributing publicly.
