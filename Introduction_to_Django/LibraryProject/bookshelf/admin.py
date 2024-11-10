from django.contrib import admin
from .models import Book

# Customizing the Book model admin interface
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable filters in the admin interface to filter by author and publication year
    list_filter = ('author', 'publication_year')

    # Enable search functionality to search by title and author
    search_fields = ('title', 'author')

# Register the customized Book model admin
admin.site.register(Book, BookAdmin)

