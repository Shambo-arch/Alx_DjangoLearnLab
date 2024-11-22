# Update Operation

## Command
```python
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
updated_book

expected output:
<Book: Nineteen Eighty-Four>
