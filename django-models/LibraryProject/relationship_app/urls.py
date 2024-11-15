from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register, CustomLoginView, CustomLogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     path('register/', views.register, name='register'),  # Register view from views.py

    # Login and Logout
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Built-in LoginView
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Built-in LogoutView
]

