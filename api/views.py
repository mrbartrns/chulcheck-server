from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from authentication.TokenAuthentication import BearerTokenAuthentication
from .serializers import AttendenceSerializer
from .models import Attendance


# Create your views here.


class AttendanceView(APIView):
    """
    출석 정보의 get(list)과 post를 담당하는 view 입니다.
    TODO: post, update, delete method 추가
    ANCHOR: AllowAny -> authenticated로 변경 필요
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = AttendenceSerializer

    def get(self, request):
        user = request.user
        data = Attendance.objects.filter(user=user)
        return Response(self.serializer_class(data, many=True).data, status=200)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.save(user=request.user)
            return Response(
                self.serializer_class(data).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
