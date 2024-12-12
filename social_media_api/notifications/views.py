from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        unread_count = notifications.filter(read=False).count()

        data = {
            'unread_count': unread_count,
            'notifications': [
                {
                    'actor': notification.actor.username,
                    'verb': notification.verb,
                    'target': str(notification.target),
                    'timestamp': notification.timestamp,
                    'read': notification.read,
                }
                for notification in notifications
            ]
        }
        return Response(data)


# Create your views here.
