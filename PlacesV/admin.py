from __future__ import unicode_literals
from .models import Countries, Cities
from django.contrib import admin


admin.site.register(Countries)
# Register your models here.
admin.site.register(Cities)