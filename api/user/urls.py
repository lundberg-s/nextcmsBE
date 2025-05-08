from django.urls import path
from user.views import UserMeView, UserListView

app_name = "core"

urlpatterns = [
    path("users/me/", UserMeView.as_view(), name="users-me"),
    path("users/", UserListView.as_view(), name="user-list-view"),
]
