from django.db import models
from django.contrib.auth.models import User
import uuid



class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    profile_image = models.ImageField(default="default.jpg")
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, editable=False, related_name="post_creator")
    picture = models.ImageField(null=True, blank=True)
    body = models.TextField(max_length=2083, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-created']

class Review(models.Model):
    owner = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    review_list = (
        ('Like','Like'),
        ('Love', 'Love'),
        ('Smile','Smile'),
    )
    review = models.CharField(max_length=100, choices=review_list, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(null=True, blank=True)
    body = models.CharField(max_length=2083, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    receipient = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='receipient')
    body = models.CharField(max_length=2083, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    
    



