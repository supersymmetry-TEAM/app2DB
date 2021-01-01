from django.contrib import admin
from dietrecord.models import DietRecord

class DietRecordAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('user',)

admin.site.register(DietRecord, DietRecordAdmin)
