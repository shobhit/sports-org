from django.db import models

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
    headline = models.CharField(maxlength=200)
    aclass = models.CharField(maxlength=2, choices=ANNOUNCEMENT_CLASS, null=True)
    entered_date = models.DateField('date entered', null=True)
    valid_until_date = models.DateField('valid until date', null=True)
    message_text = models.TextField()
    entity_for_name = models.CharField(maxlength=200)

    def __str__(self):
        return self.headline + " " + self.entity_for_name

    class Admin:
        pass
    
class Org(models.Model):
    name = models.CharField(maxlength=200)
    address1 = models.CharField(maxlength=80, null=True)
    address2 = models.CharField(maxlength=80, null=True)
    city = models.CharField(maxlength=80, null=True)
    state = models.USStateField(null=True)
    sport = models.CharField(maxlength=2, choices=SPORT_CHOICES, null=True)
    established = models.DateField('date established', null=True)

    def __str__(self):
        return self.name

    class Admin:
        fields = (
            (None, {'fields': ('name', 'sport', 'established',)}),
            ('Address', {'fields': ('address1', 'address2', 'city', 'state',)}),
            )
        list_display = ('name', 'city', 'sport', 'established')

class Person(models.Model):
    last_name = models.CharField(maxlength=40, core=True)
    first_name = models.CharField(maxlength=40, core=True)
    address1 = models.CharField(maxlength=80)
    address2 = models.CharField(maxlength=80, blank=True)
    city = models.CharField(maxlength=80, default='Btown')
    state = models.USStateField(default='MA')
    phone = models.PhoneNumberField()
    guardian1 = models.ForeignKey('self', null=True, related_name='child_of_g1', blank=True)
    guardian2 = models.ForeignKey('self', null=True, related_name='child_of_g2', blank=True)
    normal_role = models.CharField(maxlength=1, choices=PERSON_ROLES, blank=True, null=True)

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
        

class League(models.Model):
    org = models.ForeignKey(Org)
    name = models.CharField(maxlength=200, core=True)
    period_start = models.DateField('start date')
    period_end = models.DateField('end date')
    player_birthdate_low = models.DateField('low birthdate')
    player_birthdate_high = models.DateField('high birthdate')

    def __str__(self):
        return self.name

    class Admin:
        pass

class Division(models.Model):
    league = models.ForeignKey(League, edit_inline=models.TABULAR, num_in_admin=3)
    name = models.CharField(maxlength=200, core=True)

    def __str__(self):
        return self.name

    class Admin:
        pass

class Team(models.Model):
    division = models.ForeignKey(Division, edit_inline=models.TABULAR, num_in_admin=6)
    name = models.CharField(maxlength=200, core=True)

    def __str__(self):
        return self.name

class Team_player(models.Model):
    team = models.ForeignKey(Team, edit_inline=models.TABULAR, num_in_admin=3, core=True)
    player = models.ForeignKey(Person, edit_inline=models.TABULAR, num_in_admin=3, core=True)

    def __str__(self):
        return self.team.name + ": " + self.player.first_name + " " + self.player.last_name
    class Admin:
        list_display = ('team', 'player')
        ordering = ('team', 'player')
        list_filter = ['team']
        search_fields = ['player']

class Team_coach(models.Model):
    team = models.ForeignKey(Team, edit_inline=models.TABULAR, num_in_admin=3, core=True)
    coach = models.ForeignKey(Person, edit_inline=models.TABULAR, num_in_admin=3)
    title = models.CharField(maxlength=200, core=True)

    def __str__(self):
        return self.team.name + ": " + self.coach.first_name + " " + self.coach.last_name
    
    class Admin:
        list_display = ('team', 'coach')
        ordering = ('team', 'coach')
        list_filter = ['team']
        search_fields = ['coach']


class Venue(models.Model):
    name = models.CharField(maxlength=200, core=True)
    venue_type = models.CharField(maxlength=1, choices=VENUE_TYPES) 
    address1 = models.CharField(maxlength=80, null=True, blank=True)
    address2 = models.CharField(maxlength=80, null=True, blank=True)
    city = models.CharField(maxlength=80, null=True, blank=True)
    state = models.USStateField(null=True, blank=True)
    contact = models.ForeignKey(Person, null=True, blank=True)

    def __str__(self):
        return self.name

    class Admin:
        #ordering = ('name')
        list_filter = ['name', 'venue_type']
        search_fields = ['name', 'venue_type']

class VenueAvailability(models.Model):
    venue = models.ForeignKey(Venue)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    comment = models.CharField(maxlength=200, null=True, blank=True)

    def __str__(self):
        return self.venue.name + " " + self.time_start.strftime("%m/%d/%Y %H:%M") + " - " + self.time_end.strftime("%H:%M")

    class Admin:
	#list_display = ('time_start')
	ordering = ['time_start']
        list_filter = ['time_start', 'venue']
        search_fields = ['time_start', 'venue']
        date_hierarchy = ('time_start')
        save_as = True
        
class Event(models.Model):
    name = models.CharField(maxlength=200, null=True, blank=True)
    event_type = models.CharField(maxlength=1, choices=EVENT_TYPES)
    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)
    venue = models.ForeignKey(Venue, null=True, blank=True)
    team1 = models.ForeignKey(Team, related_name='team1', null=True, blank=True)
    team2 = models.ForeignKey(Team, related_name='team2', null=True, blank=True)
    team1_points = models.IntegerField(null=True, blank=True)
    team2_points = models.IntegerField(null=True, blank=True)

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
