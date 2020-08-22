from django.contrib import admin
from main import models
from main import views

# Register your models here.

admin.site.register([models.Article,
models.Author])








