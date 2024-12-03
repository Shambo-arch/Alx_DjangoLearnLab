from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class BookApiTests(APITestCase):

    def setUp(self):
        # Create test user and book
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '1234567890',
            'published_date': '2023-01-01',
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        """Test creating a new book"""
        url = reverse('book-list')  # Assuming you have a 'book-list' endpoint
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_read_book(self):
        """Test reading a book's details"""
        url = reverse('book-detail', args=[self.book.id])  # Assuming you have a 'book-detail' endpoint
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_update_book(self):
        """Test updating a book"""
        url = reverse('book-detail', args=[self.book.id])
        updated_data = {'title': 'Updated Book'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])

    def test_delete_book(self):
        """Test deleting a book"""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_permissions(self):
        """Test permissions for access control"""
        # Test that only authenticated users can create a book
        url = reverse('book-list')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

