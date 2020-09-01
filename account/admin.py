from django.contrib import admin
from .models import Login, Signup, Blog

# Register your models here.
admin.site.register(Login)
admin.site.register(Signup)
admin.site.register(Blog)