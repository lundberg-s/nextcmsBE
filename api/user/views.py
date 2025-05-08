from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, ListAPIView

from user.serializers import UserSerializer

# Create your views here.
User = get_user_model()


class UserMeView(RetrieveAPIView):
    queryset = User.objects.none()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserListView(ListAPIView):
    queryset = User.objects.none()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
