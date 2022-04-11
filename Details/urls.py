from django.urls import path
from .views import StudentView, MentorView, ArtStyleView

urlpatterns = [
    path('student/', StudentView.as_view()),
    path('mentor/', MentorView.as_view()),
    path('artstyle/', ArtStyleView.as_view()),
]