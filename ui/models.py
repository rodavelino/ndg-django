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
#  Create your models here :) root@ianlawrence.info
#
#
#=========================================================================


from django.db import models
from django.contrib.auth.models import User


class company(models.Model):
    companyName = models.CharField(max_length=200)
    companyType = models.CharField(max_length=200)
    companyCountry = models.CharField(max_length=200)
    companyIndustry = models.CharField(max_length=200)
    companySize= models.IntegerField()

    def __unicode__(self):
        return self.companyName

class device(models.Model):
    deviceModel = models.CharField(max_length=10, null=True)

    def __unicode__(self):
        return self.deviceModel

class imei(models.Model):
    imei = models.CharField(max_length=15)
    msisdn = models.CharField(max_length=25)
    qtdeResults = models.IntegerField(null=True)
    idDevice = models.ForeignKey(device)
    iduser = models.ForeignKey(User)
    companyCountry = models.CharField(max_length=200)
    companyIndustry = models.CharField(max_length=200)

    def __unicode__(self):
        return self.imei

class surveys(models.Model):
    surveyXML = models.TextField()
    iduser = models.ForeignKey(User)
    isUploaded = models.CharField(max_length=2, default='N')
 
    def __unicode__(self):
        return self.iduser

    class Meta:
        verbose_name_plural = "surveys"


class results(models.Model):
    resultXML = models.TextField()
    idSurvey = models.ForeignKey(surveys)
    imei = models.ForeignKey(imei)
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    title = models.CharField(max_length=150)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "results"





