from django.contrib import admin
from nutfood.models import NutData

class NutAdmin(admin.ModelAdmin):
    fields = [
    'NUTR_CONT3',
    'NUTR_CONT2' ,
    'NUTR_CONT1' ,
    'SERVING_SIZE',
    'MAKER_NAME' ,
    'NUTR_CONT9' ,
    'NUTR_CONT8' ,
    'FOOD_CD',
    'NUTR_CONT7' ,
    'NUTR_CONT6',
    'NUTR_CONT5',
    'NUTR_CONT4',
    'DESC_KOR',
    'SAMPLING_MONTH_NAME',
    'SUB_REF_NAME',
    'SAMPLING_REGION_NAME' ,
    'GROUP_NAME' ,
    'RESEARCH_YEAR',
    'SAMPLING_REGION_CD',
    'SAMPLING_MONTH_CD' ,
    'NUM',
    'SEARCH_SCORE' 
         ]
    search_fields = ('DESC_KOR',)

admin.site.register(NutData, NutAdmin)
