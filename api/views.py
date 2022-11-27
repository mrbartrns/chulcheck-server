from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from authentication.TokenAuthentication import BearerTokenAuthentication
from .serializers import AttendenceSerializer, OrganizationSerializer
from .models import Attendance, Organization


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

    def get(self, request, month):
        user = request.user

        if month:
            if month < 0 or month > 12:
                return Response(
                    {
                        "message": "month must be greater than 0 and smaller than or equal to 12."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            data = Attendance.objects.filter(timestamp__month=month, user=user)
            return Response(
                self.serializer_class(data, many=True).data, status=status.HTTP_200_OK
            )

        data = Attendance.objects.filter(user=user)
        return Response(
            self.serializer_class(data, many=True).data, status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.save(user=request.user)
            return Response(
                self.serializer_class(data).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationView(APIView):
    """
    Organization 관련 view
    TODO - post 시 add user 및 remove user 추가
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = OrganizationSerializer

    def get(self, request, id):
        serializer = self.serializer_class
        data = get_object_or_404(Organization, id=id)
        return Response(serializer(data).data, status=status.HTTP_200_OK)
