from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeed, LikePostView, UnlikePostView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeed.as_view(), name='user_feed')
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]

