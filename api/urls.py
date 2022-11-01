from django.urls import path
from .views import AttendanceView


urlpatterns = [
    path("attendance", AttendanceView.as_view()),
    path("attendance/<int:month>", AttendanceView.as_view()),
]
