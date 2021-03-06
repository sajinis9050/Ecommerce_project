from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Home(models.Model):
    message = models.CharField(max_length=255)
    special = models.CharField(max_length=500)
    notes = models.CharField(max_length=1000)


class Cart(models.Model):
    instruction = models.CharField(max_length=255)
    note = models.CharField(max_length=255)


class Chat(models.Model):
    display = models.CharField(max_length=30)
    submit = models.CharField(max_length=10)