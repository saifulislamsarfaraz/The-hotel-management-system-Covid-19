from distutils.command.upload import upload
from email.mime import image
from ssl import Options
from unicodedata import category
from django.db import models

# Create your models here.


class Room(models.Model):
    
    ROOM_CATEGORIES = (
        ('YAC','Ac'),
        ('NAC','Non-Ac'),
        ('DEL','Deluex'),
        ('KIN','King'),
        ('QUE', 'Queen'),
        ('STDIOU', 'Stduio'),
        ('HTR', 'Hollywood-Twin-Room'),
        ('ES', 'Executive'),
        ('MS', 'MiniSuite'),
        ('PS', 'PresidentialSuite'),
        ('AP', 'Apartments'),
        ('CR', 'ConnectingRooms'),
        ('MR', 'MurphyRooms'),
        ('AR', 'Accessible'),
        ('CN', 'Cabana'),
        ('ADR', 'AdjoiningRoom'),
        ('VIL', 'Villa'),
        ('EF', 'ExecutiveRoom'),
        ('NSM', 'Non-SmokingRoom'),

    )
    number = models.IntegerField()
    category = models.CharField(max_length=6,choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    desc = models.TextField()
    capacity = models.IntegerField()
    image = models.CharField(max_length=400)

    def __str__(self):
        return self.category
    

