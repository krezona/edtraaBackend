from django.urls import path
from .views import *

urlpatterns = [

path('deactivate/<int:id>', CourseView.as_view()),
path('delete/<int:id>', CourseView.as_view())

    
]
