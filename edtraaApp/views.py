from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

from edtraaApp.models import Course ,Instructor
from edtraaApp.CustomModifications.serializers import CourseSerializer,InstructorSerializer

# Create your views here.

class CourseView(APIView):

    def patch(self, request, id):

        if 'deactivate' in request.path:
            return self.deactivate( request, id)
    
    def delete(self, request, id):
       
       try:
       
        course=Course.objects.get(id=id)
        course.delete()
        return JsonResponse({'message': 'Course Deleted Sucessfully !!'}, status=204)
       
       except Course.DoesNotExist:
          return JsonResponse({'error': 'Course not found'}, status=404)
    
    def post(self, request):#UploadCourse-post method
        serializer = CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):#Editcourse-put method
        try:
            course = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def deactivate(self, request, id):

        try:

         course=Course.objects.get(id=id)
         course.is_active=False
         course.save()
         return JsonResponse({"message":"Course deactivated sucessfully !"}, status=200)

        except Exception as e:
           return JsonResponse({"error": str(e)}, status=400)
        
        



