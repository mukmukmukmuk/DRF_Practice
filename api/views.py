from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from api.models import *
from api.serializers import *
# Create your views here.
class StudentListAPIView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get_serializer_context(self):
        return {
            'request': None,
            'format': self.format_kwarg,
            'view': self
        }

class ProfessorAPIView(ModelViewSet):
    queryset=Professor.objects.all()
    serializer_class=ProfessorSerializer
    def get_serializer_context(self):
        return {
            'request': None,
            'format': self.format_kwarg,
            'view': self
        }
    

class ProfileListAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        studentList = Student.objects.all()
        professorList = Professor.objects.all()
        data = {
            'studentList': studentList,
            'professorList': professorList,
        }

        serializer = ProfileListSerializer(instance=data)
        return Response(serializer.data)

class CourseListAPIView(ListAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseListSerializer

class CourceRetrieveAPIView(RetrieveAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseRetrieveSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()    
        studentList=instance.student_set.all()
        professorList=instance.professor_set.all()
        data={
            'coursename': instance,
            'studentList': studentList,
            'professorList': professorList,
        }

        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)

class CourseRegistrationAPIView(ModelViewSet):
    queryset=CourseRegistration.objects.all()
    serializer_class=CourseRegistrationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)