from django.db import models


class Partner(models.Model):
    tradingName = models.CharField(max_length=200)
    ownerName = models.CharField(max_length=200)
    document = models.CharField(max_length=50, unique= True)
    coverageArea = models.JSONField()
    address = models.JSONField()
    
    
    def __str__(self):
        return self.tradingName
    

class Nearest_Partner(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    distance = models.FloatField()