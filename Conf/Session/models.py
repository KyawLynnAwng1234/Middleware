from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)


class Notification(models.Model):
    message=models.TextField(blank=True,null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    updated_at=models.DateTimeField(auto_now=True,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    