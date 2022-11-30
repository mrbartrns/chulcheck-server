from django.urls import path
from .views import AttendanceView, OrganizationView, OrganizationListView


urlpatterns = [
    path("attendance/<int:month>", AttendanceView.as_view()),
    path("organizations", OrganizationListView.as_view()),
    path("organizations/<int:id>", OrganizationView.as_view()),
]
