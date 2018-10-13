# -*- coding: utf-8 -*- from __future__ import unicode_literals 
from django.db import models


class Parent(models.Model):
    p1_firstname = models.CharField(max_length=45)
    p1_lastname = models.CharField(max_length=45)
    p2_firstname = models.CharField(max_length=45)
    p2_lastname = models.CharField(max_length=45)
    p1_telephone = models.CharField(max_length=45)
    p1_address = models.CharField(max_length=45) 


class Child(models.Model):
    fname = models.CharField(max_length=45) 
    lname = models.CharField(max_length=45) 
    grade = models.CharField(max_length=45) 
    username = models.CharField(max_length=45) 
    p1_telephone = models.CharField(max_length=45) 
    p1_fname = models.CharField(max_length=45) 
    p1_lname = models.CharField(max_length=45) 
    p2_fname = models.CharField(max_length=45) 
    p2_lname = models.CharField(max_length=45)
    

class Enrollment(models.Model):
        ch_fname = models.CharField(max_length=45) 
        ch_lname = models.CharField(max_length=45) 
        p1_tel = models.CharField(max_length=45) 
        p1_fname = models.CharField(max_length=45) 
        p2_fname = models.CharField(max_length=45) 
        p1_lname = models.CharField(max_length=45) 
        p2_lname = models.CharField(max_length=45)  


class Users(models.Model):
        uname = models.CharField(max_length=45) 
        pword = models.CharField(max_length=45) 
        pnum = models.CharField(max_length=45)  

class Assignments(models.Model):
        topic = models.CharField(max_length=45)  
        difficulty = models.CharField(max_length=45)
        level = models.CharField(max_length=45)
        question = models.CharField(max_length=500)

 



