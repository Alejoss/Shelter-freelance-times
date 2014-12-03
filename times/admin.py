from django.contrib import admin
from times.models import Day, Week, Records
from activities.models import TrophySet, Activity

# Register your models here.
admin.site.register(Day)
admin.site.register(Week)
admin.site.register(Records)
admin.site.register(TrophySet)
admin.site.register(Activity)
