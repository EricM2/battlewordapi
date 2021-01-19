from django.contrib import admin

# Register your models here.
from .models import Word, Subscriber

admin.site.register(Word)
admin.site.register(Subscriber)
