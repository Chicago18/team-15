# -*- coding: utf-8 -*- from __future__ import unicode_literals 
from django.db import models


class Parent(models.Model):
    p1_firstname = models.CharField(max_length=45)
    p1_lastname = models.CharField(max_length=45)
    p2_firstname = models.CharField(max_length=45)
    p2_lastname = models.CharField(max_length=45)
    p1_telephone = models.CharField(max_length=45)
    p1_address = model.CharField(max_length=45) 


class Child(models.Model):
    fname = model.CharField(max_length=45) 
    lname = model.CharField(max_length=45) 
    grade = model.CharField(max_length=45) 
    username = model.CharField(max_length=45) 
    p1_telephone = model.CharField(max_length=45) 
    p1_fname = model.CharField(max_length=45) 
    p1_lname = model.CharField(max_length=45) 
    p2_fname = model.CharField(max_length=45) 
    p2_lname = model.CharField(max_length=45)
    

class Enrollment(models.Model):
        ch_fname = model.CharField(max_length=45) 
        ch_lname = model.CharField(max_length=45) 
        p1_tel = model.CharField(max_length=45) 
        p1_fname = model.CharField(max_length=45) 
        p2_fname = model.CharField(max_length=45) 
        p1_lname = model.CharField(max_length=45) 
        p2_lname = model.CharField(max_length=45)  


class Users(models.Model):
        uname = model.CharField(max_length=45) 
        pword = model.CharField(max_length=45) 
        pnum = model.CharField(max_length=45)  

class Assignments(models.Model):
        topic = model.CharField(max_length=45)  
        difficulty = model.CharField(max_length=45)
        level = model.CharField(max_length=45)
        question = model.CharField(max_length=500)

 



