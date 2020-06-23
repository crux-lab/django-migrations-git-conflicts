from django.db import models


class BarModel(models.Model):
    bar_field = models.TextField(default='bar')
