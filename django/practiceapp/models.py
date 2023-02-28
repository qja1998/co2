from django.conf import settings
from django.db import models

class Parameters(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL)
    model_name = models.CharField(max_length=4)
    seq_len = models.IntegerField(blank=False)
    hidden_num = models.IntegerField(blank=False)
    layer_num = models.IntegerField(blank=False)
    epochs = models.IntegerField(blank=False)
    lr = models.FloatField(blank=False)

class TrainedData(models.Model):
    model_path = models.CharField(max_length=100)
    loss = models.FloatField(blank=False)
    img_path = models.CharField(max_length=100)