from django.urls import path
from .views import BookListView, APIDocumentation

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('api-docs/', APIDocumentation.as_view(), name='api-docs'),
]

