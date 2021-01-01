from django.db import models

class NutData(models.Model):
    
    NUTR_CONT3 = models.CharField(max_length=50)
    NUTR_CONT2 = models.CharField(max_length=50)
    NUTR_CONT1 = models.CharField(max_length=50)
    SERVING_SIZE = models.CharField(max_length=50)
    MAKER_NAME = models.CharField(max_length=200)
    NUTR_CONT9 = models.CharField(max_length=50)
    NUTR_CONT8 = models.CharField(max_length=50)
    FOOD_CD = models.CharField(max_length=50)
    NUTR_CONT7 = models.CharField(max_length=50)
    NUTR_CONT6 = models.CharField(max_length=50)
    NUTR_CONT5 = models.CharField(max_length=50)
    NUTR_CONT4 = models.CharField(max_length=50)
    DESC_KOR = models.CharField(max_length=200)
    SAMPLING_MONTH_NAME = models.CharField(max_length=200)
    SUB_REF_NAME = models.CharField(max_length=200)
    SAMPLING_REGION_NAME = models.CharField(max_length=200)
    GROUP_NAME = models.CharField(max_length=200)
    RESEARCH_YEAR = models.CharField(max_length=50)
    SAMPLING_REGION_CD = models.CharField(max_length=50)
    SAMPLING_MONTH_CD = models.CharField(max_length=50)
    NUM = models.IntegerField(primary_key=True)
    SEARCH_SCORE = models.IntegerField(default=0)
    def __str__(self):
        return self.DESC_KOR