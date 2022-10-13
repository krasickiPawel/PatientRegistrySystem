from django.contrib import admin

from .models import Appointment, Request

admin.site.register(Appointment)
admin.site.register(Request)
