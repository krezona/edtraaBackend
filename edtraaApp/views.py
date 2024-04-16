from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Course


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
    
        
    def deactivate(self, request, id):

        try:

         course=Course.objects.get(id=id)
         course.is_active=False
         course.save()
         return JsonResponse({"message":"Course deactivated sucessfully !"}, status=200)

        except Exception as e:
           return JsonResponse({"error": str(e)}, status=400)
        
        



