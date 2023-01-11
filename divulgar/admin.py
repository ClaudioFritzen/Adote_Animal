from django.contrib import admin
from .models import Raca, Tag

# Register your models here.
admin.site.register([Raca, Tag])