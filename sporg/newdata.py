import datetime
from org.models import *
Announcement1=Announcement(Headline='All announcements first',aclass='Organization',entered_date=datetime.date(2009,4,21),valid_until_date=datetime.date(2009,5,31),message_text='This announcement is valid for all in the\n            organization',entity_for_name='org')
Announcement1.save()
Announcement2=Announcement(Headline='announcement for NBA league',aclass='League',entered_date=datetime.date(2009,4,21),valid_until_date=datetime.date(2009,6,30),message_text='This announcement is valid for NBA league',entity_for_name='NBA')
Announcement2.save()
Announcement3=Announcement(Headline='Announcement for the Bummers',aclass='Team',entered_date=datetime.date(2009,4,21),valid_until_date=datetime.date(2009,5,31),message_text='Announcement for the Bummers',entity_for_name='Bummers')
Announcement3.save()
Announcement4=Announcement(Headline='New schedule posted',aclass='League',entered_date=datetime.date(2009,4,23),valid_until_date=datetime.date(2009,4,30),message_text='The new schedule has been posted for the\n            enlightenment of all great people a number of whom call Btown their home. In the event\n            of events out of control, the event will have an eventful ending. In the end of an event\n            that is not eventful we will begin anew ',entity_for_name='NBA')
Announcement4.save()
Org1=Org(name='Btown Basketball Association',address1='837 Btown Drive, Btown, MA',sport='Basketball',established=datetime.date(2009,4,18))
Org1.save()
Person2=Person(last_name='Drep',first_name='Julie',address1='47 Drep St, Btown, MA',phone='617-444-1234',normal_role='Guardian')
Person2.save()
Person1=Person(last_name='Drep',first_name='Johnny',address1='127 DK St, Btown, MA',phone='617-232-4441',guardian1=Person2,normal_role='Player')
Person1.save()
Person3=Person(last_name='Fird',first_name='Joe',address1='Whatever Dr, Btown, MA',phone='617-330-3030',normal_role='Coach')
Person3.save()
Person4=Person(last_name='Ging',first_name='Graham',address1='888 What st, Btown, MA',phone='617-440-4433',normal_role='Guardian')
Person4.save()
Person5=Person(last_name='Ding',first_name='Jimmy',address1='88 What St., Btown, MA',phone='617-440-4433',guardian1=Person4,normal_role='Player')
Person5.save()
League1=League(org=Org1,name='NBA',period_start=datetime.date(2009,4,1),period_end=datetime.date(2009,6,30),player_birthdate_low=datetime.date(1995,5,1),player_birthdate_high=datetime.date(1997,5,1))
League1.save()
Division1=Division(league=League1,name='NBA West')
Division1.save()
Division2=Division(league=League1,name='NBA East')
Division2.save()
Team1=Team(division=Division2,name='Bummers')
Team1.save()
Team2=Team(division=Division2,name='Blowhards')
Team2.save()
Team3=Team(division=Division2,name='Ringers')
Team3.save()
Team4=Team(division=Division2,name='Slappers')
Team4.save()
Team5=Team(division=Division1,name='Wows')
Team5.save()
Team6=Team(division=Division1,name='Mores')
Team6.save()
Team7=Team(division=Division1,name='Bings')
Team7.save()
Team8=Team(division=Division1,name='Bats')
Team8.save()
Team_player1=Team_player(team=Team1,player=Person5)
Team_player1.save()
Team_player2=Team_player(team=Team1,player=Person1)
Team_player2.save()
Team_coach1=Team_coach(team=Team1,coach=Person3,title='Head Coach')
Team_coach1.save()
Venue1=Venue(name='Vennie Field',venue_type='Playing',address1='1 Fird St, Btown, MA')
Venue1.save()
Venue2=Venue(name='Mork Stadium',venue_type='Playing',address1='100 Mork Ave., Btown, MA')
Venue2.save()
VenueAvailability1=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,2,18,0,0),time_end=datetime.datetime(2009,5,2,20,0,0),comment='auto generated date')
VenueAvailability1.save()
VenueAvailability2=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,29,18,0,0),time_end=datetime.datetime(2009,6,29,20,0,0),comment='auto generated date')
VenueAvailability2.save()
VenueAvailability3=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,14,18,0,0),time_end=datetime.datetime(2009,5,14,20,0,0),comment='auto generated date')
VenueAvailability3.save()
VenueAvailability4=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,24,18,0,0),time_end=datetime.datetime(2009,5,24,20,0,0),comment='auto generated date')
VenueAvailability4.save()
VenueAvailability5=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,30,18,0,0),time_end=datetime.datetime(2009,5,30,20,0,0),comment='auto generated date')
VenueAvailability5.save()
VenueAvailability6=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,25,18,0,0),time_end=datetime.datetime(2009,4,25,20,0,0),comment='auto generated date')
VenueAvailability6.save()
VenueAvailability7=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,5,18,0,0),time_end=datetime.datetime(2009,4,5,20,0,0),comment='auto generated date')
VenueAvailability7.save()
VenueAvailability8=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,9,18,0,0),time_end=datetime.datetime(2009,4,9,20,0,0),comment='auto generated date')
VenueAvailability8.save()
VenueAvailability9=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,28,18,0,0),time_end=datetime.datetime(2009,6,28,20,0,0),comment='auto generated date')
VenueAvailability9.save()
VenueAvailability10=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,26,18,0,0),time_end=datetime.datetime(2009,5,26,20,0,0),comment='auto generated date')
VenueAvailability10.save()
VenueAvailability11=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,2,18,0,0),time_end=datetime.datetime(2009,4,2,20,0,0),comment='auto generated date')
VenueAvailability11.save()
VenueAvailability12=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,12,18,0,0),time_end=datetime.datetime(2009,4,12,20,0,0),comment='auto generated date')
VenueAvailability12.save()
VenueAvailability13=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,27,18,0,0),time_end=datetime.datetime(2009,6,27,20,0,0),comment='auto generated date')
VenueAvailability13.save()
VenueAvailability14=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,4,18,0,0),time_end=datetime.datetime(2009,4,4,20,0,0),comment='auto generated date')
VenueAvailability14.save()
VenueAvailability15=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,20,18,0,0),time_end=datetime.datetime(2009,4,20,20,0,0),comment='auto generated date')
VenueAvailability15.save()
VenueAvailability16=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,23,18,0,0),time_end=datetime.datetime(2009,4,23,20,0,0),comment='auto generated date')
VenueAvailability16.save()
VenueAvailability17=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,14,18,0,0),time_end=datetime.datetime(2009,4,14,20,0,0),comment='auto generated date')
VenueAvailability17.save()
VenueAvailability18=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,21,18,0,0),time_end=datetime.datetime(2009,5,21,20,0,0),comment='auto generated date')
VenueAvailability18.save()
VenueAvailability19=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,15,18,0,0),time_end=datetime.datetime(2009,6,15,20,0,0),comment='auto generated date')
VenueAvailability19.save()
VenueAvailability20=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,17,18,0,0),time_end=datetime.datetime(2009,5,17,20,0,0),comment='auto generated date')
VenueAvailability20.save()
VenueAvailability21=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,22,18,0,0),time_end=datetime.datetime(2009,6,22,20,0,0),comment='auto generated date')
VenueAvailability21.save()
VenueAvailability22=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,25,18,0,0),time_end=datetime.datetime(2009,5,25,20,0,0),comment='auto generated date')
VenueAvailability22.save()
VenueAvailability23=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,21,18,0,0),time_end=datetime.datetime(2009,6,21,20,0,0),comment='auto generated date')
VenueAvailability23.save()
VenueAvailability24=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,10,18,0,0),time_end=datetime.datetime(2009,5,10,20,0,0),comment='auto generated date')
VenueAvailability24.save()
VenueAvailability25=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,16,18,0,0),time_end=datetime.datetime(2009,5,16,20,0,0),comment='auto generated date')
VenueAvailability25.save()
VenueAvailability26=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,20,18,0,0),time_end=datetime.datetime(2009,6,20,20,0,0),comment='auto generated date')
VenueAvailability26.save()
VenueAvailability27=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,21,18,0,0),time_end=datetime.datetime(2009,4,21,20,0,0),comment='auto generated date')
VenueAvailability27.save()
VenueAvailability28=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,23,18,0,0),time_end=datetime.datetime(2009,5,23,20,0,0),comment='auto generated date')
VenueAvailability28.save()
VenueAvailability29=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,8,18,0,0),time_end=datetime.datetime(2009,6,8,20,0,0),comment='auto generated date')
VenueAvailability29.save()
VenueAvailability30=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,14,18,0,0),time_end=datetime.datetime(2009,6,14,20,0,0),comment='auto generated date')
VenueAvailability30.save()
VenueAvailability31=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,12,18,0,0),time_end=datetime.datetime(2009,5,12,20,0,0),comment='auto generated date')
VenueAvailability31.save()
VenueAvailability32=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,11,18,0,0),time_end=datetime.datetime(2009,5,11,20,0,0),comment='auto generated date')
VenueAvailability32.save()
VenueAvailability33=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,1,18,0,0),time_end=datetime.datetime(2009,6,1,20,0,0),comment='auto generated date')
VenueAvailability33.save()
VenueAvailability34=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,7,18,0,0),time_end=datetime.datetime(2009,5,7,20,0,0),comment='auto generated date')
VenueAvailability34.save()
VenueAvailability35=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,7,18,0,0),time_end=datetime.datetime(2009,6,7,20,0,0),comment='auto generated date')
VenueAvailability35.save()
VenueAvailability36=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,9,18,0,0),time_end=datetime.datetime(2009,5,9,20,0,0),comment='auto generated date')
VenueAvailability36.save()
VenueAvailability37=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,19,18,0,0),time_end=datetime.datetime(2009,5,19,20,0,0),comment='auto generated date')
VenueAvailability37.save()
VenueAvailability38=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,16,18,0,0),time_end=datetime.datetime(2009,6,16,20,0,0),comment='auto generated date')
VenueAvailability38.save()
VenueAvailability39=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,16,18,0,0),time_end=datetime.datetime(2009,4,16,20,0,0),comment='auto generated date')
VenueAvailability39.save()
VenueAvailability40=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,30,18,0,0),time_end=datetime.datetime(2009,4,30,20,0,0),comment='auto generated date')
VenueAvailability40.save()
VenueAvailability41=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,19,18,0,0),time_end=datetime.datetime(2009,4,19,20,0,0),comment='auto generated date')
VenueAvailability41.save()
VenueAvailability42=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,11,18,0,0),time_end=datetime.datetime(2009,6,11,20,0,0),comment='auto generated date')
VenueAvailability42.save()
VenueAvailability43=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,23,18,0,0),time_end=datetime.datetime(2009,6,23,20,0,0),comment='auto generated date')
VenueAvailability43.save()
VenueAvailability44=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,27,18,0,0),time_end=datetime.datetime(2009,4,27,20,0,0),comment='auto generated date')
VenueAvailability44.save()
VenueAvailability45=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,11,18,0,0),time_end=datetime.datetime(2009,4,11,20,0,0),comment='auto generated date')
VenueAvailability45.save()
VenueAvailability46=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,25,18,0,0),time_end=datetime.datetime(2009,6,25,20,0,0),comment='auto generated date')
VenueAvailability46.save()
VenueAvailability47=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,18,18,0,0),time_end=datetime.datetime(2009,5,18,20,0,0),comment='auto generated date')
VenueAvailability47.save()
VenueAvailability48=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,13,18,0,0),time_end=datetime.datetime(2009,6,13,20,0,0),comment='auto generated date')
VenueAvailability48.save()
VenueAvailability49=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,7,18,0,0),time_end=datetime.datetime(2009,4,7,20,0,0),comment='auto generated date')
VenueAvailability49.save()
VenueAvailability50=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,2,18,0,0),time_end=datetime.datetime(2009,6,2,20,0,0),comment='auto generated date')
VenueAvailability50.save()
VenueAvailability51=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,26,18,0,0),time_end=datetime.datetime(2009,4,26,20,0,0),comment='auto generated date')
VenueAvailability51.save()
VenueAvailability52=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,18,18,0,0),time_end=datetime.datetime(2009,4,18,20,0,0),comment='auto generated date')
VenueAvailability52.save()
VenueAvailability53=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,28,18,0,0),time_end=datetime.datetime(2009,4,28,20,0,0),comment='auto generated date')
VenueAvailability53.save()
VenueAvailability54=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,18,18,0,0),time_end=datetime.datetime(2009,6,18,20,0,0),comment='auto generated date')
VenueAvailability54.save()
VenueAvailability55=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,4,18,0,0),time_end=datetime.datetime(2009,5,4,20,0,0),comment='auto generated date')
VenueAvailability55.save()
VenueAvailability56=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,28,18,0,0),time_end=datetime.datetime(2009,5,28,20,0,0),comment='auto generated date')
VenueAvailability56.save()
VenueAvailability57=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,3,18,0,0),time_end=datetime.datetime(2009,5,3,20,0,0),comment='auto generated date')
VenueAvailability57.save()
VenueAvailability58=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,9,18,0,0),time_end=datetime.datetime(2009,6,9,20,0,0),comment='auto generated date')
VenueAvailability58.save()
VenueAvailability59=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,5,5,18,0,0),time_end=datetime.datetime(2009,5,5,20,0,0),comment='auto generated date')
VenueAvailability59.save()
VenueAvailability60=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,4,13,18,0,0),time_end=datetime.datetime(2009,4,13,20,0,0),comment='auto generated date')
VenueAvailability60.save()
VenueAvailability61=VenueAvailability(venue=Venue1,time_start=datetime.datetime(2009,6,4,18,0,0),time_end=datetime.datetime(2009,6,4,20,0,0),comment='auto generated date')
VenueAvailability61.save()
VenueAvailability62=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,2,18,0,0),time_end=datetime.datetime(2009,5,2,20,0,0),comment='auto generated date')
VenueAvailability62.save()
VenueAvailability63=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,29,18,0,0),time_end=datetime.datetime(2009,6,29,20,0,0),comment='auto generated date')
VenueAvailability63.save()
VenueAvailability64=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,30,18,0,0),time_end=datetime.datetime(2009,5,30,20,0,0),comment='auto generated date')
VenueAvailability64.save()
VenueAvailability65=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,25,18,0,0),time_end=datetime.datetime(2009,4,25,20,0,0),comment='auto generated date')
VenueAvailability65.save()
VenueAvailability66=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,6,18,0,0),time_end=datetime.datetime(2009,6,6,20,0,0),comment='auto generated date')
VenueAvailability66.save()
VenueAvailability67=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,26,18,0,0),time_end=datetime.datetime(2009,5,26,20,0,0),comment='auto generated date')
VenueAvailability67.save()
VenueAvailability68=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,20,18,0,0),time_end=datetime.datetime(2009,6,20,20,0,0),comment='auto generated date')
VenueAvailability68.save()
VenueAvailability69=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,20,18,0,0),time_end=datetime.datetime(2009,4,20,20,0,0),comment='auto generated date')
VenueAvailability69.save()
VenueAvailability70=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,14,18,0,0),time_end=datetime.datetime(2009,4,14,20,0,0),comment='auto generated date')
VenueAvailability70.save()
VenueAvailability71=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,15,18,0,0),time_end=datetime.datetime(2009,6,15,20,0,0),comment='auto generated date')
VenueAvailability71.save()
VenueAvailability72=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,22,18,0,0),time_end=datetime.datetime(2009,6,22,20,0,0),comment='auto generated date')
VenueAvailability72.save()
VenueAvailability73=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,16,18,0,0),time_end=datetime.datetime(2009,5,16,20,0,0),comment='auto generated date')
VenueAvailability73.save()
VenueAvailability74=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,21,18,0,0),time_end=datetime.datetime(2009,4,21,20,0,0),comment='auto generated date')
VenueAvailability74.save()
VenueAvailability75=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,5,18,0,0),time_end=datetime.datetime(2009,5,5,20,0,0),comment='auto generated date')
VenueAvailability75.save()
VenueAvailability76=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,8,18,0,0),time_end=datetime.datetime(2009,6,8,20,0,0),comment='auto generated date')
VenueAvailability76.save()
VenueAvailability77=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,12,18,0,0),time_end=datetime.datetime(2009,5,12,20,0,0),comment='auto generated date')
VenueAvailability77.save()
VenueAvailability78=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,11,18,0,0),time_end=datetime.datetime(2009,5,11,20,0,0),comment='auto generated date')
VenueAvailability78.save()
VenueAvailability79=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,1,18,0,0),time_end=datetime.datetime(2009,6,1,20,0,0),comment='auto generated date')
VenueAvailability79.save()
VenueAvailability80=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,9,18,0,0),time_end=datetime.datetime(2009,5,9,20,0,0),comment='auto generated date')
VenueAvailability80.save()
VenueAvailability81=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,19,18,0,0),time_end=datetime.datetime(2009,5,19,20,0,0),comment='auto generated date')
VenueAvailability81.save()
VenueAvailability82=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,16,18,0,0),time_end=datetime.datetime(2009,6,16,20,0,0),comment='auto generated date')
VenueAvailability82.save()
VenueAvailability83=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,23,18,0,0),time_end=datetime.datetime(2009,6,23,20,0,0),comment='auto generated date')
VenueAvailability83.save()
VenueAvailability84=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,27,18,0,0),time_end=datetime.datetime(2009,4,27,20,0,0),comment='auto generated date')
VenueAvailability84.save()
VenueAvailability85=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,18,18,0,0),time_end=datetime.datetime(2009,5,18,20,0,0),comment='auto generated date')
VenueAvailability85.save()
VenueAvailability86=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,13,18,0,0),time_end=datetime.datetime(2009,6,13,20,0,0),comment='auto generated date')
VenueAvailability86.save()
VenueAvailability87=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,7,18,0,0),time_end=datetime.datetime(2009,4,7,20,0,0),comment='auto generated date')
VenueAvailability87.save()
VenueAvailability88=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,2,18,0,0),time_end=datetime.datetime(2009,6,2,20,0,0),comment='auto generated date')
VenueAvailability88.save()
VenueAvailability89=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,18,18,0,0),time_end=datetime.datetime(2009,4,18,20,0,0),comment='auto generated date')
VenueAvailability89.save()
VenueAvailability90=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,28,18,0,0),time_end=datetime.datetime(2009,4,28,20,0,0),comment='auto generated date')
VenueAvailability90.save()
VenueAvailability91=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,4,18,0,0),time_end=datetime.datetime(2009,5,4,20,0,0),comment='auto generated date')
VenueAvailability91.save()
VenueAvailability92=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,27,18,0,0),time_end=datetime.datetime(2009,6,27,20,0,0),comment='auto generated date')
VenueAvailability92.save()
VenueAvailability93=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,25,18,0,0),time_end=datetime.datetime(2009,5,25,20,0,0),comment='auto generated date')
VenueAvailability93.save()
VenueAvailability94=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,6,9,18,0,0),time_end=datetime.datetime(2009,6,9,20,0,0),comment='auto generated date')
VenueAvailability94.save()
VenueAvailability95=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,5,23,18,0,0),time_end=datetime.datetime(2009,5,23,20,0,0),comment='auto generated date')
VenueAvailability95.save()
VenueAvailability96=VenueAvailability(venue=Venue2,time_start=datetime.datetime(2009,4,13,18,0,0),time_end=datetime.datetime(2009,4,13,20,0,0),comment='auto generated date')
VenueAvailability96.save()
Event2=Event(event_type='Game',time_start=datetime.datetime(2009,4,26,14,30,0),time_end=datetime.datetime(2009,4,26,15,30,0),venue=Venue1,team1=Team1,team2=Team2,team1_points=8,team2_points=3)
Event2.save()
Event3=Event(event_type='Game',time_start=datetime.datetime(2009,4,27,12,0,0),time_end=datetime.datetime(2009,4,27,1,0,0),venue=Venue2,team1=Team3,team2=Team4,team1_points=4,team2_points=6)
Event3.save()
Event4=Event(event_type='Game',time_start=datetime.datetime(2009,4,1,20,38,45),time_end=datetime.datetime(2009,4,1,21,38,49),venue=Venue2,team1=Team1,team2=Team3,team1_points=4,team2_points=2)
Event4.save()
Event5=Event(event_type='Game',time_start=datetime.datetime(2009,4,1,20,39,32),time_end=datetime.datetime(2009,4,1,21,39,37),venue=Venue1,team1=Team2,team2=Team4,team1_points=5,team2_points=3)
Event5.save()
Event6=Event(event_type='Game',time_start=datetime.datetime(2009,4,5,15,40,25),time_end=datetime.datetime(2009,4,5,15,40,34),venue=Venue1,team1=Team1,team2=Team4,team1_points=3,team2_points=1)
Event6.save()
Event7=Event(event_type='Game',time_start=datetime.datetime(2009,4,5,14,0,0),time_end=datetime.datetime(2009,4,5,15,0,0),venue=Venue1,team1=Team2,team2=Team3,team1_points=2,team2_points=6)
Event7.save()
Event8=Event(event_type='Game',time_start=datetime.datetime(2009,4,20,13,0,0),time_end=datetime.datetime(2009,4,20,14,0,0),venue=Venue2,team1=Team4,team2=Team2,team1_points=3,team2_points=2)
Event8.save()
Event9=Event(event_type='Game',time_start=datetime.datetime(2009,5,2,18,0,0),time_end=datetime.datetime(2009,5,2,20,0,0),venue=Venue1,team1=Team7,team2=Team4,team1_points=14,team2_points=5)
Event9.save()
Event10=Event(event_type='Game',time_start=datetime.datetime(2009,6,29,18,0,0),time_end=datetime.datetime(2009,6,29,20,0,0),venue=Venue1,team1=Team1,team2=Team2,team1_points=2,team2_points=14)
Event10.save()
Event11=Event(event_type='Game',time_start=datetime.datetime(2009,5,14,18,0,0),time_end=datetime.datetime(2009,5,14,20,0,0),venue=Venue1,team1=Team8,team2=Team1,team1_points=3,team2_points=13)
Event11.save()
Event12=Event(event_type='Game',time_start=datetime.datetime(2009,5,24,18,0,0),time_end=datetime.datetime(2009,5,24,20,0,0),venue=Venue1,team1=Team5,team2=Team4,team1_points=14,team2_points=8)
Event12.save()
Event13=Event(event_type='Game',time_start=datetime.datetime(2009,5,30,18,0,0),time_end=datetime.datetime(2009,5,30,20,0,0),venue=Venue1,team1=Team2,team2=Team3,team1_points=1,team2_points=7)
Event13.save()
Event14=Event(event_type='Game',time_start=datetime.datetime(2009,4,25,18,0,0),time_end=datetime.datetime(2009,4,25,20,0,0),venue=Venue1,team1=Team6,team2=Team7,team1_points=0,team2_points=2)
Event14.save()
Event15=Event(event_type='Game',time_start=datetime.datetime(2009,4,5,18,0,0),time_end=datetime.datetime(2009,4,5,20,0,0),venue=Venue1,team1=Team8,team2=Team2,team1_points=7,team2_points=5)
Event15.save()
Event16=Event(event_type='Game',time_start=datetime.datetime(2009,4,9,18,0,0),time_end=datetime.datetime(2009,4,9,20,0,0),venue=Venue1,team1=Team6,team2=Team4,team1_points=6,team2_points=4)
Event16.save()
Event17=Event(event_type='Game',time_start=datetime.datetime(2009,6,28,18,0,0),time_end=datetime.datetime(2009,6,28,20,0,0),venue=Venue1,team1=Team5,team2=Team4,team1_points=14,team2_points=6)
Event17.save()
Event18=Event(event_type='Game',time_start=datetime.datetime(2009,5,26,18,0,0),time_end=datetime.datetime(2009,5,26,20,0,0),venue=Venue1,team1=Team6,team2=Team4,team1_points=6,team2_points=7)
Event18.save()
Event19=Event(event_type='Game',time_start=datetime.datetime(2009,4,2,18,0,0),time_end=datetime.datetime(2009,4,2,20,0,0),venue=Venue1,team1=Team7,team2=Team3,team1_points=13,team2_points=2)
Event19.save()
Event20=Event(event_type='Game',time_start=datetime.datetime(2009,4,12,18,0,0),time_end=datetime.datetime(2009,4,12,20,0,0),venue=Venue1,team1=Team5,team2=Team3,team1_points=13,team2_points=14)
Event20.save()
Event21=Event(event_type='Game',time_start=datetime.datetime(2009,6,27,18,0,0),time_end=datetime.datetime(2009,6,27,20,0,0),venue=Venue1,team1=Team5,team2=Team2,team1_points=12,team2_points=2)
Event21.save()
Event22=Event(event_type='Game',time_start=datetime.datetime(2009,4,4,18,0,0),time_end=datetime.datetime(2009,4,4,20,0,0),venue=Venue1,team1=Team8,team2=Team4,team1_points=6,team2_points=13)
Event22.save()
Event23=Event(event_type='Game',time_start=datetime.datetime(2009,4,20,18,0,0),time_end=datetime.datetime(2009,4,20,20,0,0),venue=Venue1,team1=Team8,team2=Team3,team1_points=11,team2_points=3)
Event23.save()
Event24=Event(event_type='Game',time_start=datetime.datetime(2009,4,23,18,0,0),time_end=datetime.datetime(2009,4,23,20,0,0),venue=Venue1,team1=Team7,team2=Team1,team1_points=12,team2_points=0)
Event24.save()
Event25=Event(event_type='Game',time_start=datetime.datetime(2009,4,14,18,0,0),time_end=datetime.datetime(2009,4,14,20,0,0),venue=Venue1,team1=Team7,team2=Team2,team1_points=12,team2_points=12)
Event25.save()
Event26=Event(event_type='Game',time_start=datetime.datetime(2009,5,21,18,0,0),time_end=datetime.datetime(2009,5,21,20,0,0),venue=Venue1,team1=Team5,team2=Team2,team1_points=7,team2_points=1)
Event26.save()
Event27=Event(event_type='Game',time_start=datetime.datetime(2009,6,15,18,0,0),time_end=datetime.datetime(2009,6,15,20,0,0),venue=Venue1,team1=Team5,team2=Team6,team1_points=5,team2_points=2)
Event27.save()
Event28=Event(event_type='Game',time_start=datetime.datetime(2009,5,17,18,0,0),time_end=datetime.datetime(2009,5,17,20,0,0),venue=Venue1,team1=Team1,team2=Team3,team1_points=7,team2_points=9)
Event28.save()
Event29=Event(event_type='Game',time_start=datetime.datetime(2009,6,22,18,0,0),time_end=datetime.datetime(2009,6,22,20,0,0),venue=Venue1,team1=Team6,team2=Team3,team1_points=14,team2_points=6)
Event29.save()
Event30=Event(event_type='Game',time_start=datetime.datetime(2009,5,25,18,0,0),time_end=datetime.datetime(2009,5,25,20,0,0),venue=Venue1,team1=Team7,team2=Team2,team1_points=0,team2_points=4)
Event30.save()
Event31=Event(event_type='Game',time_start=datetime.datetime(2009,6,21,18,0,0),time_end=datetime.datetime(2009,6,21,20,0,0),venue=Venue1,team1=Team8,team2=Team1,team1_points=6,team2_points=3)
Event31.save()
Event32=Event(event_type='Game',time_start=datetime.datetime(2009,5,10,18,0,0),time_end=datetime.datetime(2009,5,10,20,0,0),venue=Venue1,team1=Team8,team2=Team3,team1_points=6,team2_points=14)
Event32.save()
Event33=Event(event_type='Game',time_start=datetime.datetime(2009,5,16,18,0,0),time_end=datetime.datetime(2009,5,16,20,0,0),venue=Venue1,team1=Team6,team2=Team3,team1_points=7,team2_points=4)
Event33.save()
Event34=Event(event_type='Game',time_start=datetime.datetime(2009,6,20,18,0,0),time_end=datetime.datetime(2009,6,20,20,0,0),venue=Venue1,team1=Team6,team2=Team2,team1_points=13,team2_points=8)
Event34.save()
Event35=Event(event_type='Game',time_start=datetime.datetime(2009,4,21,18,0,0),time_end=datetime.datetime(2009,4,21,20,0,0),venue=Venue1,team1=Team6,team2=Team1,team1_points=10,team2_points=2)
Event35.save()
Event36=Event(event_type='Game',time_start=datetime.datetime(2009,5,23,18,0,0),time_end=datetime.datetime(2009,5,23,20,0,0),venue=Venue1,team1=Team5,team2=Team1,team1_points=1,team2_points=7)
Event36.save()
Event37=Event(event_type='Game',time_start=datetime.datetime(2009,6,8,18,0,0),time_end=datetime.datetime(2009,6,8,20,0,0),venue=Venue1,team1=Team7,team2=Team1,team1_points=6,team2_points=8)
Event37.save()
Event38=Event(event_type='Game',time_start=datetime.datetime(2009,6,14,18,0,0),time_end=datetime.datetime(2009,6,14,20,0,0),venue=Venue1,team1=Team3,team2=Team4,team1_points=2,team2_points=2)
Event38.save()
Event39=Event(event_type='Game',time_start=datetime.datetime(2009,5,12,18,0,0),time_end=datetime.datetime(2009,5,12,20,0,0),venue=Venue1,team1=Team6,team2=Team1,team1_points=13,team2_points=0)
Event39.save()
Event40=Event(event_type='Game',time_start=datetime.datetime(2009,5,11,18,0,0),time_end=datetime.datetime(2009,5,11,20,0,0),venue=Venue1,team1=Team5,team2=Team3,team1_points=4,team2_points=2)
Event40.save()
Event41=Event(event_type='Game',time_start=datetime.datetime(2009,6,1,18,0,0),time_end=datetime.datetime(2009,6,1,20,0,0),venue=Venue1,team1=Team2,team2=Team4,team1_points=4,team2_points=0)
Event41.save()
Event42=Event(event_type='Game',time_start=datetime.datetime(2009,5,7,18,0,0),time_end=datetime.datetime(2009,5,7,20,0,0),venue=Venue1,team1=Team5,team2=Team7,team1_points=11,team2_points=5)
Event42.save()
Event43=Event(event_type='Game',time_start=datetime.datetime(2009,6,7,18,0,0),time_end=datetime.datetime(2009,6,7,20,0,0),venue=Venue1,team1=Team7,team2=Team4,team1_points=6,team2_points=8)
Event43.save()
Event44=Event(event_type='Game',time_start=datetime.datetime(2009,5,9,18,0,0),time_end=datetime.datetime(2009,5,9,20,0,0),venue=Venue1,team1=Team6,team2=Team8,team1_points=7,team2_points=13)
Event44.save()
Event45=Event(event_type='Game',time_start=datetime.datetime(2009,5,19,18,0,0),time_end=datetime.datetime(2009,5,19,20,0,0),venue=Venue1,team1=Team1,team2=Team4,team1_points=14,team2_points=0)
Event45.save()
Event46=Event(event_type='Game',time_start=datetime.datetime(2009,6,16,18,0,0),time_end=datetime.datetime(2009,6,16,20,0,0),venue=Venue1,team1=Team8,team2=Team2,team1_points=0,team2_points=12)
Event46.save()
Event47=Event(event_type='Game',time_start=datetime.datetime(2009,4,16,18,0,0),time_end=datetime.datetime(2009,4,16,20,0,0),venue=Venue1,team1=Team7,team2=Team8,team1_points=9,team2_points=2)
Event47.save()
Event48=Event(event_type='Game',time_start=datetime.datetime(2009,4,30,18,0,0),time_end=datetime.datetime(2009,4,30,20,0,0),venue=Venue1,team1=Team5,team2=Team8,team1_points=9,team2_points=3)
Event48.save()
