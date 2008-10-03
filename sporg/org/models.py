from appengine_django.models import BaseModel
from google.appengine.ext import db

SPORT_CHOICES = (
    ('Basketball'),
    ('Baseball'),
    ('Football'),
    ('Soccer'),
    ('Ice Hockey'),
    ('Field Hockey'),
    ('Lacrosse')
    )

PERSON_ROLES = (
    ('Player'),
    ('Coach'),
    ('Administrator'),
    ('Guardian')
    )

ANNOUNCEMENT_CLASS = (
    ('Organization'),
    ('League'),
    ('Division'),
    ('Team'),
    ('Person')
    )

VENUE_TYPES = (
    ('Playing'),
    ('Practice only'),
    ('Meeting')
    )

EVENT_TYPES = (
    ('Game'),
    ('Practice'),
    ('Meeting')
    )

class Announcement(BaseModel):
    Headline = db.StringProperty()
    aclass = db.StringProperty(choices=ANNOUNCEMENT_CLASS)
    entered_date = db.DateProperty(verbose_name='date entered')
    valid_until_date = db.DateProperty(verbose_name='valid until date')
    message_text = db.TextProperty()
    entity_for_name = db.StringProperty()

    def __str__(self):
        return self.Headline + " " + self.entity_for_name

    class Admin:
        pass
    
class Org(BaseModel):
    name = db.StringProperty()
    address = db.PostalAddressProperty()
    sport = db.StringProperty(choices=SPORT_CHOICES)
    established = db.DateProperty(verbose_name='date established')

    def __str__(self):
        return self.name

    class Admin:
        fields = (
            (None, {'fields': ('name', 'sport', 'established',)}),
            ('Address', {'fields': ('address1', 'address2', 'city', 'state',)}),
            )
        list_display = ('name', 'city', 'sport', 'established')

class Person(BaseModel):
    last_name = db.StringProperty()
    first_name = db.StringProperty()
    address = db.PostalAddressProperty()
    phone = db.PhoneNumberProperty()
    guardian1 = db.SelfReferenceProperty(collection_name='child_of_g1')
    guardian2 = db.SelfReferenceProperty(collection_name='child_of_g2')
    normal_role = db.StringProperty(choices=PERSON_ROLES)

    def __str__(self):
        return self.last_name + ', ' + self.first_name

    class Admin:
        fields = (
            (None, {'fields': ('last_name', 'first_name', 'normal_role',)}),
            ('Address', {'fields': ('address1', 'address2', 'city', 'state', 'phone',)}),
            ('Guardians', {'fields': ('guardian1', 'guardian2',)}),
            )
        list_display = ('normal_role', 'last_name', 'first_name')
        search_fields = ['last_name', 'first_name', 'normal_role']
        list_filter = ['normal_role']
        ordering = ('normal_role', 'last_name', 'first_name')
        

class League(BaseModel):
    org = db.ReferenceProperty(Org)
    name = db.StringProperty()
    period_start = db.DateProperty(verbose_name='start date')
    period_end = db.DateProperty(verbose_name='end date')
    player_birthdate_low = db.DateProperty(verbose_name='low birthdate')
    player_birthdate_high = db.DateProperty(verbose_name='high birthdate')

    def __str__(self):
        return self.name

    class Admin:
        pass

class Division(BaseModel):
    league = db.ReferenceProperty(League)
    name = db.StringProperty()

    def __str__(self):
        return self.name

    class Admin:
        pass

class Team(BaseModel):
    division = db.ReferenceProperty(Division)
    name = db.StringProperty()

    def __str__(self):
        return self.name

class Team_player(BaseModel):
    team = db.ReferenceProperty(Team)
    player = db.ReferenceProperty(Person)

    def __str__(self):
        return self.team.name + ": " + self.player.first_name + " " + self.player.last_name
    class Admin:
        list_display = ('team', 'player')
        ordering = ('team', 'player')
        list_filter = ['team']
        search_fields = ['player']

class Team_coach(BaseModel):
    team = db.ReferenceProperty(Team)
    coach = db.ReferenceProperty(Person)
    title = db.StringProperty()

    def __str__(self):
        return self.team.name + ": " + self.coach.first_name + " " + self.coach.last_name
    
    class Admin:
        list_display = ('team', 'coach')
        ordering = ('team', 'coach')
        list_filter = ['team']
        search_fields = ['coach']


class Venue(BaseModel):
    name = db.StringProperty()
    venue_type = db.StringProperty(choices=VENUE_TYPES) 
    address = db.PostalAddressProperty()
    contact = db.ReferenceProperty(Person)

    def __str__(self):
        return self.name

    class Admin:
        #ordering = ('name')
        list_filter = ['name', 'venue_type']
        search_fields = ['name', 'venue_type']

class VenueAvailability(BaseModel):
    venue = db.ReferenceProperty(Venue)
    time_start = db.DateTimeProperty()
    time_end = db.DateTimeProperty()
    comment = db.StringProperty()

    def __str__(self):
        return self.venue.name + " " + self.time_start.strftime("%m/%d/%Y %H:%M") + " - " + self.time_end.strftime("%H:%M")

    class Admin:
	#list_display = ('time_start')
	ordering = ['time_start']
        list_filter = ['time_start', 'venue']
        search_fields = ['time_start', 'venue']
        date_hierarchy = ('time_start')
        save_as = True
        
class Event(BaseModel):
    name = db.StringProperty()
    event_type = db.StringProperty(choices=EVENT_TYPES)
    time_start = db.DateTimeProperty()
    time_end = db.DateTimeProperty()
    venue = db.ReferenceProperty(Venue)
    team1 = db.ReferenceProperty(Team, collection_name='team1')
    team2 = db.ReferenceProperty(Team, collection_name='team2')
    team1_points = db.IntegerProperty()
    team2_points = db.IntegerProperty()

    def __str__(self):
        rval = self.time_start.strftime("%m/%d/%Y") + " " + self.venue.name + " " + self.get_event_type_display() + ": " + self.team1.name
        if self.team2 != None:
            rval += " vs. " + self.team2.name
        return rval
    
    class Admin:
        fields = (
            (None, {'fields': ('event_type',)}),
            ('Time',  {'fields': ('time_start', 'time_end','venue')}),
            ('Team1', {'fields': ('team1', 'team1_points',)}),
            ('Team2', {'fields': ('team2', 'team2_points',)}),
            ('Other', {'fields': ('name',)}),
            )
        ordering = ('time_start', 'team1', 'team2')
        list_filter = ['time_start', 'team1', 'team2', 'event_type', 'venue']
        search_fields = ['time_start', 'team1', 'team2', 'event_type', 'venue']

