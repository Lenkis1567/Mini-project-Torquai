from django.db import models

# Create your models here.
class Review (models.Model):
    text=models.TextField()
    email=models.EmailField(null=True)


class Inquiry(models.Model):
    text=models.TextField()
    email=models.EmailField(null=True)
    answered=models.BooleanField()

class Rooms(models.Model):
    people = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    price = models.FloatField(null=False)

class Roomtype(models.Model):
    type=models.CharField(max_length=25)

class Roompeople(models.Model):
    quantity=models.IntegerField()

class Booking(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    date_beginning=models.DateField()
    date_end=models.DateField()
    client=models.EmailField()
    paid=models.BooleanField()

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    reviews = models.ForeignKey(Review, null=True, on_delete=models.CASCADE)