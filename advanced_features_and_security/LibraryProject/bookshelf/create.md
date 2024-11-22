from bookshelf.models import Book

# Creating a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

expected output:
<Book: 1984>

