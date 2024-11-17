from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register, CustomLoginView, CustomLogoutView
from . import views
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     path('register/', views.register, name='register'),  # Register view from views.py

    # Login and Logout
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Built-in LoginView
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Built-in LogoutView 
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]



