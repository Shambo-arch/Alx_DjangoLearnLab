from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

# Create your views here.
# Step 1: Configure Pagination (Optional but Recommended)
class BookPagination(PageNumberPagination):
    page_size = 10  # Number of books per page
    page_size_query_param = 'page_size'
    max_page_size = 50

# Step 2: Update BookListView to Include Filtering, Searching, and Ordering
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

    # Integrate Filtering, Searching, and Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering options
    filterset_fields = ['title', 'author', 'publication_year']

    # Search configuration
    search_fields = ['title', 'author']

    # Ordering configuration
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

