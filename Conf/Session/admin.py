from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Notification)
admin.site.register(Book)
