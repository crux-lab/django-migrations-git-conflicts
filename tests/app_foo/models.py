from django.db import models


class FooModel(models.Model):
    foo_field = models.TextField(default='foo_update')
