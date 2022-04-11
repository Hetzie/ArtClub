from .models import Student, Mentor, ArtStyle
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class ArtStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtStyle
        fields = '__all__'