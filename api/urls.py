from django.urls import path
from .views import AttendanceView, OrganizationView


urlpatterns = [
    path("attendance", AttendanceView.as_view()),
    path("attendance/<int:month>", AttendanceView.as_view()),
    path("organizations/<int:id>", OrganizationView.as_view()),
]
