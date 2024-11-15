from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),  # Registration view
    path('login/', CustomLoginView.as_view(), name='login'),  # Login view
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout view
]

