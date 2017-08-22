# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Adress = models.TextField()
    Department = models.CharField(max_length=50)
    Manager = models.CharField(max_length=20)
    Work_Contact_Number = models.CharField(max_length=20)
    Personal_Contact_Number = models.CharField(max_length=20)
    Work_Email = models.CharField(max_length=30)
    Personal_Email = models.CharField(max_length=30)
    Date_Added_to_System = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.Name
