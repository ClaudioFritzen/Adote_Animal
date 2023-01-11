from django.contrib import admin
from .models import Raca, Tag, Pet

# Register your models here.
admin.site.register([Raca, Tag, Pet])