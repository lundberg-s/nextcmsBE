from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):

        response = super().post(request, *args, **kwargs)

        if response.status_code != 200:
            return response

        data = response.data
        access_token = data.get("access")
        refresh_token = data.get("refresh")

        res = Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

        res.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=300
        )

        res.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite="None",
            max_age=604800
        )

        return res


class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Extract the refresh token from the cookie
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token not found in cookies'}, status=status.HTTP_400_BAD_REQUEST)

        # Inject refresh token into the request data
        request.data['refresh'] = refresh_token

        # Call the parent method
        response = super().post(request, *args, **kwargs)

        if response.status_code != 200:
            return response

        # Extract new access token
        access_token = response.data.get("access")

        res = Response({'message': 'Token refreshed'}, status=status.HTTP_200_OK)
        res.set_cookie(
            key="access_token",
            value=access_token,
            httponly=False,
            secure=True,  # Set to False for local dev (True for production with HTTPS)
            samesite="None",
            max_age=300
        )

        return res


class LogoutView(APIView):
    def post(self, request):
        res = Response({'message': 'Logged out'})
        res.delete_cookie('access_token')
        res.delete_cookie('refresh_token')
        return res
    