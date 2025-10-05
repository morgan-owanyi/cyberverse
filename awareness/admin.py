from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import modules

admin.site.register(modules)
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date_submitted')
    list_filter = ('date_submitted',)
    search_fields = ('name', 'email', 'message')

