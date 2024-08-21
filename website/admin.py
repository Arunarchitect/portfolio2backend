from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'description')
    search_fields = ('name', 'about')

admin.site.register(About, AboutAdmin)
