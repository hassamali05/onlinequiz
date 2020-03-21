from django.db import models


class User(models.Model):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=16, default='abcd1234')
    phone = models.CharField(max_length=13, blank=True)
    address = models.TextField(blank=True)
    type = models.IntegerField()  # 0 means student and 1 means teacher.

    def __str__(self):
        return self.name
