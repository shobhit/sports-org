from django.conf.urls.defaults import *

urlpatterns = patterns('org.views',
     (r'^$', 'index'),
     (r'^(?P<league_id>\d+)/league/$', 'league'),
     (r'^(?P<division_id>\d+)/division/$', 'division'),
     (r'^(?P<league_id>\d+)/league/(?P<team_id>\d+)/team/$', 'team'),
     (r'^(?P<league_id>\d+)/league/(?P<team_id>\d+)/team/(?P<player_id>\d+)/player/$', 'player'),
     (r'^/schedule/$', 'schedule0'),
     (r'^(?P<league_id>\d+)/league/schedule/$', 'schedule1'),
     (r'^(?P<league_id>\d+)/league/(?P<team_id>\d+)/team/schedule/$', 'schedule2'),
     (r'^/results/$', 'results0'),
     (r'^(?P<league_id>\d+)/league/results/$', 'results1'),
     (r'^(?P<league_id>\d+)/league/(?P<team_id>\d+)/team/results/$', 'results2'),
     (r'^/standings/$', 'standings0'),
     (r'^(?P<league_id>\d+)/league/standings/$', 'standings1'),
     (r'^(?P<league_id>\d+)/league/(?P<team_id>\d+)/team/standings/$', 'standings2'),
     (r'^(?P<league_id>\d+)/league/build_schedule/$', 'build_schedule'),
     (r'^(?P<league_id>\d+)/league/build_availability/$', 'build_availability'),
     (r'^/accept_availability/$', 'accept_availability'),
)

