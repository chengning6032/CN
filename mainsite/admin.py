from django.contrib import admin
from .models import Location, Post
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'slug', 'author', 'create_date', 'location')

admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
