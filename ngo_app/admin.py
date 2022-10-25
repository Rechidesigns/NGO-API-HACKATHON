from django.contrib import admin
from .models import Ngo, Blog

admin.site.register([Ngo, Blog])
