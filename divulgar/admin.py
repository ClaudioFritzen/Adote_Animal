from django.contrib import admin
from .models import Raca, Tag, Pet, Estados

# Register your models here.
admin.site.register([Raca, Tag, Pet, Estados])