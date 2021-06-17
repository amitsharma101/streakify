from django.urls import path
from streakify.friends.views import *

app_name = "friends"

urlpatterns = [
    path("my-friends", FriendsAPIView.as_view(), name='my-friends'),
    path("update-request-status", FriendRequestUpdateView.as_view(), name='update-request-status'),
]