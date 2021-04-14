from django.contrib import admin

#importing models to give access to admin
from .models import Article


#to register models for accessing by admin
admin.site.register(Article)

