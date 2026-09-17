from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
    category: str
    available: bool

library = [
    Book(id = 1, title="The Great Gatsby", author="F. Scott Fitzgerald", price=10.99, category="Fiction", available=True),
    Book(id = 2, title="To Kill a Mockingbird", author="Harper Lee", price=12.99, category="Fiction", available=True),
    Book(id = 3, title="1984", author="George Orwell", price=11.99, category="Dystopian", available=False),
    Book(id = 4, title="Pride and Prejudice", author="Jane Austen", price=9.99, category="Romance", available=True),
    Book(id = 5, title="The Catcher in the Rye", author="J.D. Salinger", price=8.99, category="Fiction", available=True),
    Book(id = 6, title="The Hobbit", author="J.R.R. Tolkien", price=14.99, category="Fantasy", available=True),
    Book(id = 7, title="The Lord of the Rings", author="J.R.R. Tolkien", price=29.99, category="Fantasy", available=False),
    Book(id = 8, title="The Chronicles of Narnia", author="C.S. Lewis", price=19.99, category="Fantasy", available=True),
    Book(id = 9, title="The Da Vinci Code", author="Dan Brown", price=15.99, category="Thriller", available=True),
    Book(id = 10, title="Angels & Demons", author="Dan Brown", price=13.99, category="Thriller", available=True)
]


@app.get("/books")
def get_books():
    """Get a list of all books in the library."""
    return library

@app.post("/books")
def add_book(new_book: Book):
    """Add a new book to the library."""
    library.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

@app.get("/books/{book_id}")
def get_book(book_id : int):
    """Get a book by its ID."""
    for book in library:
        if book.id == book_id:
            return {"message": "Book found", "book": book}
        
    return {"message": "Book not found in library"}

@app.put("/books/{book_id}")
def update_book(book_id:int, updated_book: Book):
    """Update a book's information by its ID."""
    for index, book in enumerate(library):
        if book.id == book_id:
            library[index] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}

    return {"message": "Book not found in library"}

@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    """Delete a book from the library by its ID."""
    for index, book in enumerate(library):
        if book.id == book_id:
            deleted_book = library.pop(index)
            return {"message": "Book deleted successfully", "book": deleted_book}

    return {"message": "Book not found in library"}



