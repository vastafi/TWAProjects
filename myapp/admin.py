from django.contrib import admin
from .models import About
from .models import Work
from .models import Review

admin.site.register(About)
admin.site.register(Work)
admin.site.register(Review)