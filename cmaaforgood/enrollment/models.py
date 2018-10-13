# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Parent(models.Model):
    p1_firstname = models.CharField(max_length=45)
    p1_lastname = models.CharField(max_length=45)
    p2_firstname = models.CharField(max_length=45)
    p2_lastname = models.CharField(max_length=45)
    p1_telephone = models.CharField(max_length=45)
     
    class Meta:
            unique_together = ('p1_firstname', 'p1_lastname', 'p1_telephone')


#class Child(models.Model):
     
