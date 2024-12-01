from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from .serializers import MyModelSerializer
from .models import MyModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet



class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieves all books
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MyModelViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsAuthenticated]

