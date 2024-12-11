from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView
from .views import FollowUser, UnfollowUser

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Registration endpoint
    path('login/', CustomAuthToken.as_view(), name='login'),    # Login endpoint
    path('profile/', ProfileView.as_view(), name='profile'),   # Profile management endpoint
    path('follow/<int:user_id>/', FollowUser.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view(), name='unfollow_user')
]


