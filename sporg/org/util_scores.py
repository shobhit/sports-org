from sporg.org.models import Event

from random import randrange

high_score = 15
for e in Event.objects.all():
    if e.team1_points == None:
        e.team1_points = randrange(high_score)
        e.team2_points = randrange(high_score)
        print e, e.team1_points, e.team2_points
        e.save()
    
