from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
import django_filters

# Filter class to define available filters
class BookFilter(django_filters.FilterSet,filters.OrderingFilter):
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
    filterset_class = BookFilter  # Custom filter
    search_fields = ['title', 'author']  # Fields to search
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering

