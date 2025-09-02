"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(book_id, title, author, **kwargs):
    """Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
    """
    for book in library:
        if book["id"] == book_id:
            return f"Book with ID {book_id} already exists!"
    
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    
    # Add optional details (e.g., year, genre)
    for key, value in kwargs.items():
        new_book[key] = value
    
    library.append(new_book)
    return f"Book '{title}' added successfully!"


def search_books(*args):
    """Search for books by multiple keywords (title, author).
    return books that match search description.
    """
    results = []
    for book in library:
        for keyword in args:
            if (keyword.lower() in book["title"].lower()) or (keyword.lower() in book["author"].lower()):
                results.append(book)
                break  # Avoid duplicate matches
    return results


def borrow_book(book_id):
    """Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
    """
    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return f"You borrowed '{book['title']}'."
            else:
                return f"Book '{book['title']}' not available."
    return "Book not found!"


def return_book(book_id):
    """Return a borrowed book."""
    for book in library:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                return f"You returned '{book['title']}'."
            else:
                return f"Book '{book['title']}' was not borrowed."
    return "Book not found!"

print(add_book(1,"The Python programming language","Guido van rossum",year=1991,genre="education"))
print(add_book(2,"The history of computer","By MIT",year=1940,genre="education"))

print(search_books("python","jibrin"))

print(borrow_book(2))
