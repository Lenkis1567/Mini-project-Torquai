from datetime import datetime
from django.db import models

# Create your models here.
class Review (models.Model):
    text           = models.TextField()
    email          = models.EmailField(null=True, blank=True)


class Inquiry(models.Model):
    text           = models.TextField()
    email          = models.EmailField(null=True)
    is_answered    = models.BooleanField(default=False)

class RoomType (models.Model):
    type           = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.type

class AdultsCount (models.Model):
    count          = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.count

class Rooms(models.Model):
    adults         = models.ForeignKey(AdultsCount,on_delete=models.DO_NOTHING)
    type           = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING)
    price          = models.FloatField(null=False)
    quantity       = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.type.type + ":" + self.adults.count

class Booking(models.Model):
    room           = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING)
    date_beginning = models.DateField()
    date_end       = models.DateField()
    client         = models.IntegerField(null=True,blank=True)
    paid           = models.BooleanField()
    def __str__(self) -> str:
        defferense = self.date_end - self.date_beginning
        return f"Booking from {self.date_beginning} for {defferense.days} days"

class RommPhoto(models.Model):
    room           = models.ForeignKey(Rooms,on_delete=models.DO_NOTHING)
    photo          = models.ImageField(upload_to="photos/%Y/%m/%d/")
    def __str__(self) -> str:
        return f"Photo for {self.room}"
