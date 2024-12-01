from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # A field for the book's title
    author = models.CharField(max_length=100)  # A field for the book's author

    def __str__(self):
        return self.title  # Display the title in admin and queries


# Create your models here.
