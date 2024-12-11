from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Registration endpoint
    path('login/', CustomAuthToken.as_view(), name='login'),    # Login endpoint
    path('profile/', ProfileView.as_view(), name='profile'),   # Profile management endpoint
]


