from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

# Create your views here.
class SignupView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user=user)
            token = Token.objects.get(user=user).key
            return Response({"token": token})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(ObtainAuthToken):
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"message": "username or password is incorrect."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        user = serializer.validated_data["user"]  # type: ignore
        token, _ = Token.objects.get_or_create(user=user)
        response = {"id": user.id, "username": user.username, "token": token.key}
        return Response(response, status=status.HTTP_200_OK)
