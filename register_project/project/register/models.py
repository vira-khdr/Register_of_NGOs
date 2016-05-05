# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Address(models.Model):
    _region = models.CharField(max_length=50)
    _area = models.CharField(max_length=50, blank=True, null=True)
    _city = models.CharField(max_length=50)
    _address = models.CharField(max_length=200)
    _post_index = models.CharField(max_length=50)
    _phone = models.CharField(max_length=50, blank=True, null=True)

class Document(models.Model):
    _name = models.CharField(max_length=50)
    _number = models.CharField(max_length=50)
    _date = models.DateField()
    _issued_by = models.CharField(max_length=50)
    _termination_date = models.DateField(blank=True, null=True)

class Certificate(models.Model):
    _number = models.CharField(max_length=50)
    _date = models.DateField()

class Commerce_Chambers(models.Model):
    _type = models.CharField(max_length=50)
    _oper_type = models.CharField(max_length=50)
    _register_number = models.CharField(max_length=50, blank=True, null=True)
    _name_full = models.CharField(max_length=200)
    _location = models.CharField(max_length=200)
    _goal = models.CharField(max_length=200)
    _registrator_name = models.CharField(max_length=200)
    _cert = models.ForeignKey(Certificate)
    _doc = models.ForeignKey(Document)
    _address = models.ForeignKey(Address)