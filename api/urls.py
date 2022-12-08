from django.urls import path
from .views import (
    AttendanceView,
    AttendanceListView,
    OrganizationView,
    OrganizationListView,
    OrganizationUserView,
    OrganizationJoinedView,
)


urlpatterns = [
    path("attendance", AttendanceListView.as_view()),
    path("attendance/<int:id>", AttendanceView.as_view()),
    path("organizations/joined", OrganizationJoinedView.as_view()),
    path("organizations", OrganizationListView.as_view()),
    path("organizations/<int:id>", OrganizationView.as_view()),
    path("organizations/<int:id>/users", OrganizationUserView.as_view()),
]
