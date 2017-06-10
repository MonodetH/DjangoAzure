"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Item:

    price = 0
    name = ""
    pictureUrl = ""
    description = ""
    sellerId = ""


    def setName(self,nombre):
        self.name = nombre

    def setPrice(self,precio):
        self.price = precio

    def setPictureUrl(self,url):
        self.pictureUrl = url

    def setDescription(self,desc):
        self.description = desc

    def setSellerId(self,vendedor):
        self.sellerId = vendedor

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getPictureUrl(self):
        return self.pictureUrl

    def getDescription(self):
        return self.description

    def getSellerId(self):
        return self.sellerId

