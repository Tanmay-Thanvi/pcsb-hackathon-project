from django.contrib import admin
from .models import SIG,coursecontent,announcement,classroom
# Register your models here.
admin.site.register(SIG)
admin.site.register(coursecontent)
admin.site.register(announcement)
admin.site.register(classroom)