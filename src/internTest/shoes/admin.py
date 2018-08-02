from django.contrib import admin
from .models import Shoe

# Register your models here.
class shoeAdmin(admin.ModelAdmin):
    list_display=['__str__','slug']
    class Meta:
        model=Shoe


admin.site.register(Shoe)
