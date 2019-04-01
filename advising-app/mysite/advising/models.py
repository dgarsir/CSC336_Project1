from django.db import models
from django.utils import timezone
from users.models import CustomUser

# Create your models here.

majors = (
    ('Computer Science', 'CS'),
    ('Computer Engineering', 'CE')
)

class Advising(models.Model):
    advising_form_id = models.IntegerField(default = 0)
    semester = models.CharField(max_length = 100)
    major = models.CharField(max_length = 100,choices=majors)
    qpa = models.CharField(max_length=100)
    gpa = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #should this model have a status? i.e. submitted, pending approval, approved?
    status = models.IntegerField(default = 0)