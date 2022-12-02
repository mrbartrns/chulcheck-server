from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from authentication.TokenAuthentication import BearerTokenAuthentication
from .serializers import AttendenceSerializer, OrganizationSerializer
from .models import Attendance, Organization


# Create your views here.
class APIPagination(PageNumberPagination):
    page_query_param = "p"
    page_size = 10


class AttendanceListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = AttendenceSerializer

    def get(self, request):
        user = request.user
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


class OrganizationListView(APIView, APIPagination):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = OrganizationSerializer

    def get(self, request):
        serializer = self.serializer_class

        if request.query_params:
            q = request.query_params.get("q", None)
            queryset = Organization.objects.filter(name__contains=q)

            return Response(
                serializer(queryset, many=True).data, status=status.HTTP_200_OK
            )
        # page = self.paginate_queryset(data, request, view=self)

        data = get_list_or_404(Organization)

        # response = self.get_paginated_response(serializer(page, many=True).data)

        # return response
        return Response(serializer(data, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            organization = serializer.save(leader=request.user)
            # leader로 임명함과 동시에 멤버에 추가한다.
            organization.members.add(request.user)
            return Response(
                self.serializer_class(organization).data, status=status.HTTP_201_CREATED
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


class OrganizationUserView(APIView):
    """
    Organization 멤버 조회 view
    Organization 멤버 추가 view
    """

    permission_class = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = OrganizationSerializer

    # user 추가하기. 이미 user가 있다면 추가 X
    def put(self, request, id):
        data = get_object_or_404(Organization, id=id)
        user = request.user

        data.members.add(user)
        data.save()
        serializer = self.serializer_class(instance=data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrganizationJoinedView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BearerTokenAuthentication]
    serializer_class = OrganizationSerializer

    def get(self, request):
        data = Organization.objects.filter(members=request.user)

        return Response(
            self.serializer_class(data, many=True).data, status=status.HTTP_200_OK
        )
