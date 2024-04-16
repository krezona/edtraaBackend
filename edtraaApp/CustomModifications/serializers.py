from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate 

from edtraaApp.models import Course, Instructor

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email'] 


class CourseSerializer(serializers.ModelSerializer):
    instructors = InstructorSerializer(many=True)  

    class Meta:
        model = Course
        fields = [
            'id',
            'image',
            'title',
            'subTitle',
            'description',
            'aboutCourse',
            'instructors',
            'duration',
            'category',
            'topics',
            'is_active',
        ]
