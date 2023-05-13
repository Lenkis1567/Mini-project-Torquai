from datetime import datetime
from django.db import models
from django.db.models import Q

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
        return "ID:"+str(self.pk) + ' | ' + self.type.type + " | " + self.adults.count
    
    def main_photo(self):
        photos = self.r_photo.all().filter(main_photo=True)
        if photos:
            return photos[0]
        return []
    
    def is_free(self, d_from, d_to):
        reservations = self.booking_set.all().filter(
            Q(date_end__gte=d_from),
            Q(
                Q(
                    Q(date_beginning__lte=d_from),
                    Q(date_end__gte=d_from)
                 ) |
                Q(
                    Q(date_beginning__lte=d_to),
                    Q(date_end__gte=d_to)            
                ) |
                Q(
                    Q(date_beginning__gte=d_from),
                    Q(date_end__lte=d_to)
                )          
            ) 
        )
        print (f'******* From SELF. {reservations}, {len(reservations) == 0}, {len(reservations)}')
        return True if len(reservations)<self.quantity else False


class Booking(models.Model):
    room           = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING)
    date_beginning = models.DateField()
    date_end       = models.DateField()
    client         = models.IntegerField(null=True,blank=True)
    paid           = models.BooleanField()
    def __str__(self) -> str:
        defferense = self.date_end - self.date_beginning
        # return f"Booking room {self.room} from {self.date_beginning} for {defferense.days} days"
        return f"Booking room {self.room} from {self.date_beginning} until {self.date_end} days"

class RoomPhoto(models.Model):
    room           = models.ForeignKey(Rooms,on_delete=models.DO_NOTHING,related_name='r_photo')
    photo          = models.ImageField(upload_to="photos/%Y/%m/%d/")
    main_photo     = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"Photo for {self.room}"
    
