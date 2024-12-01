from django.shortcuts import render
from rest_framework.generics import ListAPIView


# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieves all books
    serializer_class = BookSerializer

