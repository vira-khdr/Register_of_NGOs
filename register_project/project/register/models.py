# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Address(models.Model):
    region = models.CharField(max_length=50)
    area = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    post_index = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)

class Document(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    date = models.DateField()
    issued_by = models.CharField(max_length=50)
    termination_date = models.DateField(blank=True, null=True)

class Certificate(models.Model):
    number = models.CharField(max_length=50)
    date = models.DateField()

class Commerce_Chambers(models.Model):
    ch_type = models.CharField(max_length=50)
    oper_type = models.CharField(max_length=50)
    register_number = models.CharField(max_length=50, blank=True, null=True)
    name_full = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    goal = models.CharField(max_length=200)
    registrator_name = models.CharField(max_length=200)
    cert = models.ForeignKey(Certificate)
    doc = models.ForeignKey(Document)
    address = models.ForeignKey(Address)