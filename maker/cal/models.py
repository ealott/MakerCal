from django.db import models

# Create your models here.
#Event
class Event(models.Model):
    name = models.CharField(80)
    long_description = models.TextField(max_length=65535)
    short_description = models.TextField(max_length=250)
    advisories = models.TextField(max_length=65535)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    booking_start = models.DateTimeField()
    booking_stop = models.DateTimeField()
    cost = models.DecimalField()
    eventbrite_link = models.TextField(max_length=250)
    free_spaces = models.IntegerField()
    paid_spaces = models.IntegerField()
    members_only = models.BooleanField()
    age_restriction = models.IntegerField()
    attendees_require_approval = models.BooleanField()
    extend_registration = models.IntegerField()
    class_number = models.IntegerField()
    sponsored = models.BooleanField()
    status = models.TextField(20)
    room_id = models.ForeignKey(Rooms)
    datetime = models.DateTimeField()
    event_type = models.TextField()
    honorarium = models.BooleanField()
    host = models.ForeignKey(Member)

#Host (AKA Instructor?)
#Attendee
#Registration


## Might be common among other Maker apps - consider sharing
#Member
#Room
#Tool: room, manual, support owner, Committee
#Committee: chair, vice-chair, committee-members, Room, Tools

class Member(models.Model):
    pass
class Tool(models.Model):
    pass

class Rooms(models.Model):
    pass
