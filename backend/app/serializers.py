from rest_framework import serializers
from .models import School, Student, Exam, Mark

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    marks = MarkSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
