from django.db import models


class Lover(models.Model):
    image = models.ImageField(upload_to='images/lovers/')
