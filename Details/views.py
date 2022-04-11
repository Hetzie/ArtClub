import imp
from rest_framework import generics
from rest_framework.views import Response
from .models import Student, Mentor, ArtStyle
from .serializers import StudentSerializer, MentorSerializer, ArtStyleSerializer

# Create your views here.
class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MentorView(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class ArtStyleView(generics.ListCreateAPIView):
    queryset = ArtStyle.objects.all()
    serializer_class = ArtStyleSerializer