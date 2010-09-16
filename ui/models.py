# Copyright (C) 2010 INdT - Instituto Nokia de Tecnologia
#
# NDG is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# NDG is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with NDG. If not, see <http://www.gnu.org/licenses/

# Contact: Ian Lawrence root@ianlawrence.info

#===========================================================================
#
# Django Framework views - HTTP-oriented functions that will make our app talk to the outside world root@ianlawrence.info
#
#
#===========================================================================

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order (done Ian 16/09/2010)
#     * Make sure each model has one field with primary_key=True (done Ian 16/09/2010)
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

# so we can relate the models to djangos User authentication system.
from django.contrib.auth.models import User


class Company(models.Model):
    idcompany = models.FloatField(db_column=u'idCompany', unique=True, primary_key=True) # Field name made lowercase.
    companyname = models.DateTimeField(db_column=u'companyName', unique=True) # Field name made lowercase.
    companytype = models.DateTimeField(db_column=u'companyType') # Field name made lowercase.
    companycountry = models.DateTimeField(db_column=u'companyCountry') # Field name made lowercase.
    companyindustry = models.DateTimeField(db_column=u'companyIndustry') # Field name made lowercase.
    companysize = models.DateTimeField(db_column=u'companySize') # Field name made lowercase.

    class Meta:
        db_table = u'company'
        verbose_name_plural = "Company"

class Device(models.Model):
    iddevice = models.FloatField(db_column=u'idDevice', unique=True, primary_key=True) # Field name made lowercase.
    devicemodel = models.DateTimeField(db_column=u'deviceModel', unique=True, blank=True, null=True) # Field name made lowercase.

    class Meta:
        db_table = u'device'
        verbose_name_plural = "Device"


class Role(models.Model):
    idrole = models.FloatField(db_column=u'idRole', unique=True, primary_key=True) # Field name made lowercase.
    rolename = models.DateTimeField(db_column=u'roleName', unique=True, blank=True, null=True) # Field name made lowercase.

    class Meta:
        db_table = u'role'
        verbose_name_plural = "Role"



class Surveys(models.Model):
    idsurvey = models.DateTimeField(db_column=u'idSurvey', unique=True, primary_key=True) # Field name made lowercase.
    surveyxml = models.TextField(db_column=u'surveyXML', blank=True) # Field name made lowercase. This field type is a guess.
    iduser = models.ForeignKey(User, db_column=u'idUser') # Field name made lowercase.
    isuploaded = models.IntegerField(db_column=u'isUploaded', blank=True, null=True) # Field name made lowercase.

    class Meta:
        db_table = u'surveys'
        verbose_name_plural = "Surveys"

class Imei(models.Model):
    imei = models.DateTimeField(primary_key=True)
    msisdn = models.DateTimeField(unique=True)
    qtderesults = models.FloatField(db_column=u'qtdeResults', blank=True, null=True) # Field name made lowercase.
    iduser = models.ForeignKey(User, db_column=u'idUser') # Field name made lowercase.
    iddevice = models.ForeignKey(Device, db_column=u'idDevice') # Field name made lowercase.
    realimei = models.IntegerField(db_column=u'realImei') # Field name made lowercase.

    class Meta:
        db_table = u'imei'
        verbose_name_plural = "IMEI"

class Results(models.Model):
    idresult = models.DateTimeField(db_column=u'idResult', unique=True, primary_key=True) # Field name made lowercase.
    resultxml = models.TextField(db_column=u'resultXML', blank=True) # Field name made lowercase. This field type is a guess.
    idsurvey = models.ForeignKey(Surveys, db_column=u'idSurvey') # Field name made lowercase.
    imei = models.ForeignKey(Imei, db_column=u'imei', blank=True, null=True)
    latitude = models.DateTimeField(blank=True, null=True)
    longitude = models.DateTimeField(blank=True, null=True)
    title = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = u'results'
        verbose_name_plural = "Results"


class Transactionlog(models.Model):
    idtransactionlog = models.FloatField(db_column=u'idTransactionLog', unique=True, primary_key=True) # Field name made lowercase.
    address = models.DateTimeField(blank=True, null=True)
    transactiontype = models.DateTimeField(db_column=u'transactionType', blank=True, null=True) # Field name made lowercase.
    transactionstatus = models.DateTimeField(db_column=u'transactionStatus', blank=True, null=True) # Field name made lowercase.
    transmissionmode = models.DateTimeField(db_column=u'transmissionMode', blank=True, null=True) # Field name made lowercase.
    transactiondate = models.TextField(db_column=u'transactionDate', blank=True) # Field name made lowercase. This field type is a guess.
    idsurvey = models.ForeignKey(Surveys, db_column=u'idSurvey', blank=True, null=True) # Field name made lowercase.
    idresult = models.ForeignKey(Results, db_column=u'idResult', blank=True, null=True) # Field name made lowercase.
    imei = models.ForeignKey(Imei, db_column=u'imei', blank=True, null=True)
    iduser = models.ForeignKey(User, db_column=u'idUser') # Field name made lowercase.

    class Meta:
        db_table = u'transactionlog'
        verbose_name_plural = "Transaction Log"


class Userbalance(models.Model):
    iduserbalance = models.FloatField(db_column=u'idUSerBalance', primary_key=True) # Field name made lowercase.
    users = models.FloatField(blank=True, null=True)
    imeis = models.FloatField(blank=True, null=True)
    sendalerts = models.FloatField(db_column=u'sendAlerts', blank=True, null=True) # Field name made lowercase.
    results = models.FloatField(blank=True, null=True)
    surveys = models.FloatField(blank=True, null=True)
    iduser = models.ForeignKey(User, db_column=u'idUser', blank=True, null=True) # Field name made lowercase.

    class Meta:
        db_table = u'userbalance'
        verbose_name_plural = "User Balance"

