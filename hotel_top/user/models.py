from django.db import models

# Create your models here.
class Review (models.Model):
    text=models.TextField()
    email=models.EmailField(null=True)


class Inquiry(models.Model):
    text=models.TextField()
    email=models.EmailField(null=True)


class Rooms(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    price = models.FloatField(null=False)

class Booking(models.Model):
    room = models.ForeignKey(Rooms)
    date_beginnig=models.DateField()
    date_end=models.DateField()
    client=models.EmailField()

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = 
    reviews = models.ForeignKey(Review, null=True)