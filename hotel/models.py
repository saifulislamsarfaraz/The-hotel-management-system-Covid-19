from django.db import models
from django.conf import settings
from django.db.models import DecimalField

# Create your models here.

class RoomCategory(models.Model):
    category = models.CharField(max_length=50)
    rate = models.FloatField()

    def __str__(self):
        return self.category

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
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'   



    
class BookingRoom(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    payment_status = models.CharField(max_length=20, default='PENDING')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount_paid = DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
   

    def __str__(self):
        return f'From = {self.check_in.strftime("%d-%b-%Y %H:%M")} To = {self.check_out.strftime("%d-%b-%Y %H:%M")}'


sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class VacinationStatus(models.Model):
    vacinationCirtificateNum = models.CharField(max_length=12)
    totalDose = models.IntegerField()
    covidTest = models.CharField(max_length=10)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class UserProfiles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DateofBirth = models.DateField()
    gender = models.CharField(max_length=50, choices=sex_choice, default='Male')

	
class ContactUs(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    message = models.CharField(max_length=200) 


