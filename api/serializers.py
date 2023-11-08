from rest_framework import serializers
from api.models import Student,Professor,Course,CourseRegistration

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    course = serializers.StringRelatedField(many=True)
    #course=CourseListSerializer(many=True)

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
    course = serializers.StringRelatedField(many=True)

class ProfileListSerializer(serializers.Serializer):
    #studentList = serializers.ListField(child=serializers.CharField())
    #professorList = serializers.ListField(child=serializers.CharField())
    studentList = StudentSerializer(many=True)
    professorList = ProfessorSerializer(many=True)


class CourseRetrieveSerializer(serializers.Serializer):
    coursename = CourseListSerializer()
    studentList = serializers.StringRelatedField(many=True)
    professorList = serializers.StringRelatedField(many=True)

class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields='__all__'
    student= serializers.StringRelatedField()
    professor = serializers.StringRelatedField()
    course = serializers.StringRelatedField()