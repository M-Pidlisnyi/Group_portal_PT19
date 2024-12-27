from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):

    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} {self.user} {self.description}"

class Thread(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} made post about {self.title} on {self.topic}"


class Post(models.Model):

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post_pic = models.ImageField(upload_to="post_pics/", null=True, blank=True)

    def __str__(self):
        return f"{self.thread} by {self.user}"
