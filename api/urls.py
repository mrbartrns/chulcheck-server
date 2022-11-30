from django.urls import path
from .views import (
    AttendanceView,
    AttendanceListView,
    OrganizationView,
    OrganizationListView,
    OrganizationUserView,
)


urlpatterns = [
    path("attendance", AttendanceListView.as_view()),
    path("attendance/<int:month>", AttendanceView.as_view()),
    path("organizations", OrganizationListView.as_view()),
    path("organizations/<int:id>", OrganizationView.as_view()),
    path("organizations/<int:id>/users", OrganizationUserView.as_view()),
]
