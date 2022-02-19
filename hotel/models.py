from distutils.command.upload import upload
from email.mime import image
from ssl import Options
from unicodedata import category
from django.db import models

# Create your models here.


class Room(models.Model):
    
    ROOM_CATEGORIES = (
        ('YAC','AC'),
        ('NAC','NON-AC'),
        ('DEL','DELUXE'),
        ('KIN','KING'),
        ('QUE', 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3,choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    desc = models.TextField()
    capacity = models.IntegerField()
    image = models.CharField(max_length=400)

    def __str__(self):
        return self.category
    

