"""
URL configuration for APIprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from api.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'student', StudentListAPIView)
router.register(r'professor', ProfessorAPIView)
router.register(r'enrolment',CourseRegistrationAPIView)
urlpatterns = [
     path('', include(router.urls)),
     path('profile/',ProfileListAPIView.as_view()),
     path('course/',CourseListAPIView.as_view()),
     path('course/<int:pk>',CourceRetrieveAPIView.as_view()),
]
