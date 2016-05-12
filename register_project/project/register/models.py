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

class Limit(models.Model):
    ch_type = models.CharField(max_length=50)
    type_activities = models.CharField(max_length=200)
    date = models.DateField()

class Founder(models.Model):
    PIB = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

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

class Party(models.Model):
    oper_type = models.CharField(max_length=50)
    register_number = models.CharField(max_length=50, blank=True, null=True)
    name_full = models.CharField(max_length=200)
    goal = models.CharField(max_length=200)
    registrator_name = models.CharField(max_length=200, blank=True)
    doc = models.ForeignKey(Document)
    cert = models.ForeignKey(Certificate)
    address = models.ForeignKey(Address)
    limit = models.ForeignKey(Limit, blank=True, null=True)

class Leader(models.Model):
    PIB = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    party = models.ForeignKey(Party)

class NGO(models.Model):
    ngo_type = models.CharField(max_length=50)
    ngo_status = models.CharField(max_length=50)
    oper_type = models.CharField(max_length=50)
    legal_form = models.CharField(max_length=50)
    #limit_id = models.ForeignKey(Limit, blank=True, null=True)
    register_number = models.CharField(max_length=50, blank=True, null=True)
    cert = models.ForeignKey(Certificate)
    doc = models.ForeignKey(Document)
    address = models.ForeignKey(Address)
    date_stop = models.DateField(blank=True, null=True)
    name_full = models.CharField(max_length=200)
    name_short = models.CharField(max_length=100, blank=True, null=True)
    goal = models.CharField(max_length=200)
    direction = models.CharField(max_length=200, blank=True, null=True)
    registrator_name = models.CharField(max_length=200)
    gov_address = models.CharField(max_length=200, blank=True, null=True)
    gov_phone = models.CharField(max_length=50, blank=True, null=True)