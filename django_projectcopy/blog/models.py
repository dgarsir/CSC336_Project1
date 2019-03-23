from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

majors = (
		('computer science', 'Computer Science'),
		('computer engineering', 'Computer Engineering'),
	)

class Post(models.Model):
    title = models.CharField(max_length=100)
    semester = models.CharField(max_length = 100)
    major = models.CharField(max_length = 100,choices=majors)
    qpa = models.CharField(max_length=100)
    gpa = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})