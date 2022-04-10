from django.db import models

class Restaurants(models.Model):
    resto_id = models.IntegerField()
    resto_name = models.CharField(max_length=255)
    resto_address = models.CharField(max_length=255)
    resto_description = models.TextField(default='null')
    kuhnya = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    namazhana = models.CharField(max_length=255, default= 'null')
    contacts = models.CharField(max_length=255, default='null')
    certificate = models.ImageField(upload_to='images/', null=True, verbose_name="certificate")
    menu = models.FileField(upload_to='files/', null=True)
    resto_photo = models.ImageField(upload_to='images/', null=True, verbose_name="photo")

class Mosque(models.Model):
    mosque_name = models.CharField(max_length=100)
    mosque_description = models.TextField(default='null')
    mosque_address = models.CharField(max_length=100)
    mosque_contacts = models.CharField(max_length=100, default='null')
    mosque_photo = models.ImageField(upload_to='images/', null=True, verbose_name= "")
    mosque_time = models.CharField(max_length=100)

class User(models.Model):
    user_fname = models.CharField(max_length=100)
    user_lname = models.CharField(max_length=100)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=65)

class Reviews(models.Model):
    user_id = models.IntegerField()
    resto_id = models.IntegerField()
    review = models.TextField(default='null')
    rate = models.IntegerField()
    review_time = models.TimeField()