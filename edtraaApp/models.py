from django.db import models

# Create your models here.

class Instructor(models.Model):
    name=models.CharField(max_length=50)


class Course(models.Model):

    categories=[('tech', 'Technology')]

    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=100)
    subTitle=models.CharField(max_length=200)
    description=models.TextField()
    aboutCourse=models.CharField(max_length=1000)
    instructors=models.ManyToManyField(Instructor)
    duration=models.CharField(max_length=50)
    category=models.CharField(max_length=50, choices=categories)
    topics=models.JSONField()



class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    number = models.IntegerField()
    topic = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=10)  
    lessonVideoLink = models.URLField(blank=True)  
    description = models.TextField()

    def __str__(self):
        return f"{self.number}: {self.topic}"

