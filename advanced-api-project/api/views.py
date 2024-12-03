from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework


from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
import django_filters


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    publication_year = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# List view with filtering, searching, and ordering capabilities
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # Ensure OrderingFilter is included
    filter_backends = (filters.OrderingFilter)
    filterset_class = BookFilter  # Custom filter
    search_fields = ['title', 'author']  # Fields to search
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering



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
