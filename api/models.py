from django.db import models
from django.utils import timezone
# Create your models here.
def upload_to(instance, filename):
    # birthday 필드 값을 기반으로 저장 경로 생성
    return f'Images/{instance.birthday.strftime("%Y/%m")}/{filename}'

class Profile(models.Model):
    name=models.CharField(max_length=5)
    introduce = models.TextField(blank=True)
    birthday=models.DateField()
    image=models.ImageField(upload_to=upload_to, blank=True, null=True)

    
    def __str__(self):
        return self.name

class Student(Profile):
    course=models.ManyToManyField('Course',blank=True)

class Professor(Profile):
    course=models.ManyToManyField('Course',blank=True)
    

class Course(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class CourseRegistration(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    registration_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'[{self.pk}] {self.course.name} {self.student.name}'

