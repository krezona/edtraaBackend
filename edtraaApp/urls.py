from django.urls import path
from .views import *
from .views import CourseView

urlpatterns = [

path('deactivate/<int:id>', CourseView.as_view()),
path('delete/<int:id>', CourseView.as_view()),
path('upload/', CourseView.as_view()),
path('edit/<int:id>/', CourseView.as_view()),

    
]
