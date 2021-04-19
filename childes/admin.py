from django.contrib import admin

from .models import Transcript
from .models import Mother

# Register your models here.
admin.site.register(Transcript)
admin.site.register(Mother)