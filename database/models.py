from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Count

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
    resto_karta = models.CharField(max_length=5000, default='null')
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self) -> str:
        return self.resto_name

    def averageReview(self):
        reviews = ReviewRating.objects.filter(resto=self).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(resto=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

class Mosque(models.Model):
    mosque_name = models.CharField(max_length=100)
    mosque_description = models.TextField(default='null')
    mosque_address = models.CharField(max_length=100)
    mosque_contacts = models.CharField(max_length=100, default='null')
    mosque_photo = models.ImageField(upload_to='images/', null=True, verbose_name= "")
    mosque_time = models.CharField(max_length=100)
    karta = models.CharField(max_length=5000, default='null')

class ReviewRating(models.Model):
    resto = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

class Resto_tables(models.Model):
    resto = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    for2seaters_total = models.IntegerField()
    for2seaters_remain = models.IntegerField()
    for4seaters_total = models.IntegerField()
    for4seaters_remain = models.IntegerField()


class Book(models.Model):
        BOOKED = 'B'
        CANCELLED = 'C'

        TICKET_STATUSES = ((BOOKED, 'Booked'),
                           (CANCELLED, 'Cancelled'),)
        user_full_name = models.CharField(max_length=300)
        user_id = models.DecimalField(decimal_places=0, max_digits=2)
        user_phone = models.CharField(max_length=300, default='87777777777')
        resto_id = models.DecimalField(decimal_places=0, max_digits=2)
        resto_name = models.CharField(max_length=30)
        no_people = models.DecimalField(decimal_places=0, max_digits=2)
        table_type = models.DecimalField(decimal_places=0, max_digits=2)
        date = models.DateField()
        time = models.TimeField()
        status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=20)

class NamazTime(models.Model):
    date = models.DateField()
    fadjr = models.CharField(max_length=300)
    vosxod = models.CharField(max_length=300)
    zuhr = models.CharField(max_length=300)
    asr = models.CharField(max_length=300)
    magrib = models.CharField(max_length=300)
    isha = models.CharField(max_length=300)

    def countReview(self):
        reviews = ReviewRating.objects.filter(resto=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count