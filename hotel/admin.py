from django.contrib import admin
from .models import Room
from .models import VacinationStatus
from .models import BookingRoom
from .models import UserProfiles
from .models import ContactUs
from .models import RoomCategory

#Register your models here.

admin.site.register(Room)
admin.site.register(VacinationStatus)
admin.site.register(RoomCategory)
admin.site.register(BookingRoom)
admin.site.register(UserProfiles)
admin.site.register(ContactUs)

