from django.db import models
from django.contrib.localflavor.us.models import *

SPORT_CHOICES = (
    ('BA', 'Basketball'),
    ('BS', 'Baseball'),
    ('FT', 'Footbal'),
    ('SO', 'Soccer'),
    ('IH', 'Ice Hockey'),
    ('FH', 'Field Hockey'),
    ('LA', 'Lacrosse')
    )

PERSON_ROLES = (
    ('P', 'Player'),
    ('C', 'Coach'),
    ('A', 'Administrator'),
    ('G', 'Guardian')
    )

ANNOUNCEMENT_CLASS = (
    ('O', 'Organization'),
    ('L', 'League'),
    ('D', 'Division'),
    ('T', 'Team'),
    ('P', 'Person')
    )

VENUE_TYPES = (
    ('G', 'Playing'),
    ('P', 'Practice only'),
    ('M', 'Meeting')
    )

EVENT_TYPES = (
    ('G', 'Game'),
    ('P', 'Practice'),
    ('M', 'Meeting')
    )

class Announcement(models.Model):
    headline = models.CharField(max_length=200)
    aclass = models.CharField(max_length=2, choices=ANNOUNCEMENT_CLASS, null=True)
    entered_date = models.DateField('date entered', null=True)
    valid_until_date = models.DateField('valid until date', null=True)
    message_text = models.TextField()
    entity_for_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.headline + " " + self.entity_for_name

    
class Org(models.Model):
    name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=80, null=True)
    address2 = models.CharField(max_length=80, null=True)
    city = models.CharField(max_length=80, null=True)
    state = USStateField(null=True)
    sport = models.CharField(max_length=2, choices=SPORT_CHOICES, null=True)
    established = models.DateField('date established', null=True)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    last_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    address1 = models.CharField(max_length=80)
    address2 = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80, default='Btown')
    state = USStateField(default='MA')
    phone = PhoneNumberField()
    guardian1 = models.ForeignKey('self', null=True, related_name='child_of_g1', blank=True)
    guardian2 = models.ForeignKey('self', null=True, related_name='child_of_g2', blank=True)
    normal_role = models.CharField(max_length=1, choices=PERSON_ROLES, blank=True, null=True)

    def __unicode__(self):
        return self.last_name + ', ' + self.first_name

        

class League(models.Model):
    org = models.ForeignKey(Org)
    name = models.CharField(max_length=200)
    period_start = models.DateField('start date')
    period_end = models.DateField('end date')
    player_birthdate_low = models.DateField('low birthdate')
    player_birthdate_high = models.DateField('high birthdate')

    def __unicode__(self):
        return self.name


class Division(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    division = models.ForeignKey(Division)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Team_player(models.Model):
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Person)

    def __unicode__(self):
        return self.team.name + ": " + self.player.first_name + " " + self.player.last_name

class Team_coach(models.Model):
    team = models.ForeignKey(Team)
    coach = models.ForeignKey(Person)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.team.name + ": " + self.coach.first_name + " " + self.coach.last_name
    


class Venue(models.Model):
    name = models.CharField(max_length=200)
    venue_type = models.CharField(max_length=1, choices=VENUE_TYPES) 
    address1 = models.CharField(max_length=80, null=True, blank=True)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    contact = models.ForeignKey(Person, null=True, blank=True)

    def __unicode__(self):
        return self.name


class VenueAvailability(models.Model):
    venue = models.ForeignKey(Venue)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.venue.name + " " + self.time_start.strftime("%m/%d/%Y %H:%M") + " - " + self.time_end.strftime("%H:%M")

        
class Event(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPES)
    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)
    venue = models.ForeignKey(Venue, null=True, blank=True)
    team1 = models.ForeignKey(Team, related_name='team1', null=True, blank=True)
    team2 = models.ForeignKey(Team, related_name='team2', null=True, blank=True)
    team1_points = models.IntegerField(null=True, blank=True)
    team2_points = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        rval = self.time_start.strftime("%m/%d/%Y") + " " + self.venue.name + " " + self.get_event_type_display() + ": " + self.team1.name
        if self.team2 != None:
            rval += " vs. " + self.team2.name
        return rval
    
