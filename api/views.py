from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AttendenceSerializer
from .models import Attendance


# Create your views here.


class AttendanceView(APIView):
    """
    출석 정보의 get(list)과 post를 담당하는 view 입니다.
    TODO: post, update, delete method 추가
    ANCHOR: AllowAny -> authenticated로 변경 필요
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = AttendenceSerializer

    def get(self, request):
        data = Attendance.objects.all()
        return Response(self.serializer_class(data, many=True).data, status=200)
