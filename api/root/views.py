from rest_framework_simplejwt.views import TokenObtainPairView

from root.serializers import CustomTokenObtainSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)