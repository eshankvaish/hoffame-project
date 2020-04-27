from django.contrib import admin
from .models import Hall, Video

# Register your models here.
class HallAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','hall')

admin.site.register(Hall, HallAdmin)
admin.site.register(Video, VideoAdmin)
