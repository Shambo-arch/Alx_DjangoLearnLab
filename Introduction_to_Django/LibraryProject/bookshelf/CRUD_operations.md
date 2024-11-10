# 1)Creating Operation

from bookshelf.models import Book

# Creating a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output verification
book

#Expected Output
<Book: 1984>


# 2) Retrieving Operation
# Retrieving the book instance
retrieved_book = Book.objects.get(id=book.id)
retrieved_book

# Expected Output
<Book: 1984>


# 3) Updating Operation

# Updating the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Verifying the update
updated_book = Book.objects.get(id=book.id)
updated_book

#Expected Output
<Book: Nineteen Eighty-Four>


# 4) Deleting Operation
# Deleting the book instance
book.delete()

# Verifying deletion
Book.objects.all()

#Expected Output
<QuerySet []>
 Here the query-set is empty due to the deletion of operation



