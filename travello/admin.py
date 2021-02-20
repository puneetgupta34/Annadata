from django.contrib import admin
from .models import Crop, Seed , Front
# Register your models here.

admin.site.register(Crop)
admin.site.register(Seed)
admin.site.register(Front)