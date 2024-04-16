from django.urls import path
from .views import *
from .views import CourseView
from edtraaApp.CustomModifications.serializers import CourseSerializer,InstructorSerializer

urlpatterns = [

path('deactivate/<int:id>', CourseView.as_view()),
path('delete/<int:id>', CourseView.as_view()),
path('upload/', CourseView.as_view()),
path('edit/<int:id>/', CourseView.as_view()),

    
]
