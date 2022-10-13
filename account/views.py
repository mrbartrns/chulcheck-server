from rest_framework import status
from rest_framework.authtoken.models import Token
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

        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
