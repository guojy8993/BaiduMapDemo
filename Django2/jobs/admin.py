#author guojingyu
#date      Sep 17, 2014
from django.contrib import admin
from jobs.models import Location
from jobs.models import Job

class JobAdmin(admin.ModelAdmin):
    fieldsets = [
                (None,{'fields': ['pub_date','job_title','job_description']}),
                ('More info',{'fields': ['location'], 'classes': ['collapse']}),
             ]
    list_display = ('job_title', 'job_description', 'pub_date')

class LocationAdmin(admin.ModelAdmin):
    list_dispaly = ('city','state','country')

admin.site.register(Job, JobAdmin)
admin.site.register(Location, LocationAdmin)