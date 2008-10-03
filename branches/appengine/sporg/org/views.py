from django.shortcuts import render_to_response
from django.http import Http404
from datetime import date, timedelta, datetime
from org.models import Org, League, Division, Team, Person, Team_player, Team_coach, Announcement, Event, Venue, VenueAvailability


def get_specific_announcements(entity):
    q = Announcement.all()
    #q.filter('entered_date <= ', date.today())
    q.filter('valid_until_date >= ', date.today())
    q.filter('entity_for_name = ', entity)
    return [a for a in q]

def get_announcements(league_name = None, team_name = None):
    rval = []
    rval.append(('org', 'Organization Wide', get_specific_announcements('org')))
    if league_name != None:
        rval.append(('league', league_name, get_specific_announcements(league_name)))
    if team_name != None:
        rval.append(('team', team_name, get_specific_announcements(team_name)))

    return rval

def get_game_context(league_id = None, team_id = None):
    game_context = ''
    if league_id != None:
        game_context = league_id + '/league'
        if team_id != None:
            game_context += '/' + team_id + '/team'
    return game_context

##def schedule(request, league_id = None, team_id=None):
##    tq = Q(event_type='G', time_start__gte=date.today())
##    schedule_list, announcements  = schedule_helper(tq, league_id, team_id)
##    game_context = get_game_context(league_id, team_id) 
##    return render_to_response('org/schedule.html', {'schedule_list': schedule_list,
##                                                    'announcements': announcements,
##                                                    'is_staff': is_staff(request),
##                                                    'game_context' : game_context})
##
##def results(request, league_id = None, team_id=None):
##    tq = Q(event_type='G', time_start__lte=date.today())
##    schedule_list, announcements = schedule_helper(tq, league_id, team_id)
##    for s in schedule_list:
##        if s.team1_points > s.team2_points:
##            s.team1_winner = True
##            s.team2_winner = False
##        else:
##            s.team2_winner = True
##            s.team1_winner = False
##    game_context = get_game_context(league_id, team_id)
##    return render_to_response('org/results.html', {'schedule_list': schedule_list,
##                                                   'announcements': announcements,
##                                                   'is_staff': is_staff(request),
##                                                   'game_context' : game_context})
##    
##def standings(request, league_id=None, team_id=None):
##    standings_list = []
##    if league_id != None:
##        st = standings_helper(league_id)
##        announcements = st['announcements']
##        game_context = st['game_context']
##        standings_list.append(st)
##    else:
##        league_list = League.objects.all().order_by('name')
##        for league in league_list:
##            standings_list.append(standings_helper(str(league.id)))
##        announcements = get_announcements()
##        game_context = get_game_context()
##    return render_to_response('org/standings.html', {'standings_list': standings_list,
##                                                     'announcements': announcements,
##                                                     'is_staff': is_staff(request),
##                                                     'game_context' : game_context})
##                                                     
##    
##def standings_helper(league_id, team_id=None):
##    tq = Q(event_type='G', time_start__lte=date.today())
##    schedule_list, announcements = schedule_helper(tq, league_id, team_id)
##    games_won = {}
##    games_lost = {}
##    for s in schedule_list:
##        if s.team1_points > s.team2_points:
##            winner = s.team1.name
##            loser = s.team2.name
##        else:
##            winner = s.team2.name
##            loser = s.team1.name
##        games_won.update([(winner, games_won.setdefault(winner, 0) + 1)])
##        games_lost.update([(loser, games_lost.setdefault(loser, 0) + 1)])
##
##    out_list = []
##    league = League.objects.get(pk=league_id)
##    division_list = Division.objects.filter(league=league_id)
##    for division in division_list:
##        team_list = Team.objects.filter(division=division.id)
##        teams = []
##        for team in team_list:
##            team.won = games_won.setdefault(team.name, 0)
##            team.lost = games_lost.setdefault(team.name, 0)
##            team.total = team.won + team.lost
##            if team.total > 0:
##                team.pct = float(team.won) / float(team.total)
##            else:
##                team.pct = 0.0
##            print team.name, team.pct
##            teams.append(team)
##        teams.sort(cmp=lambda x, y: cmp(y.pct, x.pct))
##        out_list.append((division, teams))
##    game_context = get_game_context(league_id, team_id)
##    return {'league': league,
##            'out_list': out_list,
##            'announcements': announcements,
##            'game_context': game_context
##            }
##
##def schedule_helper(tq, league_id = None, team_id=None):
##    league_nm = None
##    team_nm = None
##
##    if team_id != None:
##        print 'doing team query'
##        team = Team.objects.get(pk=team_id)
##        team_nm = team.name
##        q = Q(team1=team_id) | Q(team2=team_id)
##        tq = q & tq
##
##    schedule_list = Event.objects.filter(tq).order_by('time_start')
##
##    if league_id != None:
##        league = League.objects.get(pk=league_id)
##        league_nm = league.name
##        schedule_list = [s for s in schedule_list
##                         if s.team1.division.league.id == league.id
##                         or s.team2.division.league.id == league.id]
##    announcements = get_announcements(league_name=league_nm,team_name=team_nm)
##    return (schedule_list, announcements)
##
##
##def schedule0(request):
##    return schedule(request)
##
##def schedule1(request, league_id):
##    return schedule(request, league_id)
##
##def schedule2(request, league_id, team_id):
##    return schedule(request, league_id, team_id)
##
##def results0(request):
##    return results(request)
##
##def results1(request, league_id):
##    return results(request, league_id)
##
##def results2(request, league_id, team_id):
##    return results(request, league_id, team_id)
##
##def standings0(request):
##    return standings(request)
##
##def standings1(request, league_id):
##    return standings(request, league_id)
##
##def standings2(request, league_id, team_id):
##    return standings(request, league_id, team_id)
##
def is_staff(request):
    return request.user.is_authenticated() and request.user.is_staff

def set_ids(the_list):
    rval = []
    for obj in the_list:
        obj.id = obj.key().id()
        rval.append(obj)
    return rval

def index(request):
    league_list = set_ids(League.all().order('name'))
    announcements = get_announcements()
    return render_to_response('org/index.html', {'league_list': league_list,
                                                 'is_staff': is_staff(request),
                                                 'announcements': announcements})

def league(request, league_id):
    try:
        out_list = []
        league = League.get_by_id(int(league_id))
        division_list = set_ids(Division.all().filter('league = ', league))
        for division in division_list:
            team_list = set_ids(Team.all().filter('division = ', division))
            out_list.append((division, team_list))
        announcements = get_announcements(league_name=league.name)
        game_context = get_game_context(league_id)
    except League.DoesNotExist:
        raise Http404
    return render_to_response('org/league.html', {'league': league,
                                                  'out_list': out_list,
                                                  'announcements': announcements,
                                                  'is_staff': is_staff(request),
                                                  'game_context': game_context
                                                  })

def set_team_player_ids(team_player_list):
    rval = []
    for tp in team_player_list:
        tp.player_id = tp.player.key().id()
        tp.team_id = tp.team.key().id()
        rval.append(tp)
    return rval

def team(request, league_id, team_id):
    try:
        league = League.get_by_id(int(league_id))
        team = Team.get_by_id(int(team_id))
        player_list = set_team_player_ids(Team_player.all().filter('team = ', team))
        announcements = get_announcements(league_name=league.name, team_name=team.name)
        game_context = get_game_context(league_id, team_id)
    except Team.DoesNotExist:
        raise Http404
    return render_to_response('org/team.html', {'league': league,
                                                'team': team,
                                                'player_list':player_list,
                                                'game_context': game_context,
                                                'is_staff': is_staff(request),
                                                'announcements': announcements})

def player(request, league_id, team_id, player_id):
    try:
        league = League.get_by_id(int(league_id))
        team = Team.get_by_id(int(team_id))
        player = Person.get_by_id(int(player_id))
        announcements = get_announcements(league_name=league.name, team_name=team.name)
    except Team.DoesNotExist:
        raise Http404
    return render_to_response('org/player.html', {'league': league,
                                                  'team': team,
                                                  'player':player,
                                                  'is_staff': is_staff(request),
                                                  'announcements': announcements})

##def announcement1(request, announcement_id):
##    return announcement(request, announcement_id, None, None, None)
##def announcement2(request, announcement_id, league_id):
##    return announcement(request, announcement_id, league_id, None, None)
##def announcement3(request, announcement_id, league_id, team_id):
##    return announcement(request, announcement_id, league_id, team_id, None)
##def announcement4(request, announcement_id, league_id, team_id, player_id):
##    return announcement(request, announcement_id, league_id, team_id, player_id)
##def announcement(request, announcement_id, league_id=None, team_id=None, player_id=None):
##    try:
####        league = League.objects.get(pk=league_id)
####        team = Team.objects.get(pk=team_id)
####        player = Person.objects.get(pk=player_id)
##        announcement = Announcement.objects.get(pk=announcement_id)
##        announcements = get_announcements()
##    except:
##        raise Http404
##    return render_to_response('org/announcement.html', {'announcement': announcement,
##                                                        'announcements': announcements})
##
##def build_schedule(request, league_id):
##    from sched import sched_exact
##    from random import shuffle
##    try:
##        team_list = []
##        league = League.objects.get(pk=league_id)
##        division_list = Division.objects.filter(league=league_id)
##        for division in division_list:
##            teams = Team.objects.filter(division=division.id)
##            print teams
##            team_list += [team for team in teams]
##                
##        games_per_team = 10
##        print team_list
##        team_dates = {} # {(team, date):any} map to determine if a team already has an event for that date
##        events = []
##        schedule = sched_exact(team_list, games_per_team)
##        shuffle(schedule)  # don't want it to be oriented to team order which the result of schedule will be
##        va_list = [va for va in VenueAvailability.objects.all()]
##        for team1, team2 in schedule:
##            for va in va_list:
##                if (team1, va.time_start) not in team_dates and (team2, va.time_start) not in team_dates:
##                    event = Event(name = "", event_type='G', time_start=va.time_start, time_end=va.time_end,
##                                  venue=va.venue, team1=team1, team2=team2)
##                    team_dates[(team1, va.time_start)]=1
##                    team_dates[(team2, va.time_start)]=1
##                    events.append(event)
##                    va_list.remove(va)
##                    event.save()
##                    break
##                
##        announcements = get_announcements(league_name=league.name)
##        game_context = get_game_context(league_id)
##    except:
##        raise Http404
##    return render_to_response('org/new_schedule.html', {'events': events,
##                                                        'game_context': game_context,
##                                                        'is_staff': is_staff(request),
##                                                        'announcements': announcements})
##
##def drange(d, e):
##    ''' construct a daterate from d to e '''
##    t = timedelta(1)
##    while d < e:
##        yield d
##        d = d + t
##
##def build_availability(request, league_id):
##    try:
##        league = League.objects.get(pk=league_id)
##        s = league.period_start
##        e = league.period_end
##        day_list = [d for d in drange(s, e)]
##        venue_list = Venue.objects.filter(venue_type='G')
##        announcements = get_announcements(league_name=league.name)
##    except:
##        raise Http404
##    return render_to_response('org/venue_availability.html', {'day_list': day_list,
##                                                              'venue_list': venue_list,
##                                                              'league_id': league_id,
##                                                              'is_staff': is_staff(request),
##                                                              'announcements': announcements})
##
##def is_overlap(s, e, v):
##    va_list = VenueAvailability.objects.filter(time_start__lt=e, time_end__gt=s, venue=v)
##    return va_list.count() > 0
##    
##def get_time(d, t):
##    print 'get_time', d, t
##    return datetime(int(d[2]), int(d[0]), int(d[1]), int(t[0]), int(t[1]))
##    
##def accept_availability(request):
##    if request.method == 'POST':
##        p = request.POST
##        start_time_tuple = p['Start_time'].split(':')
##        end_time_tuple = p['End_time'].split(':')
##        venue_id=int(p['venue'])
##        venue=Venue.objects.get(pk=venue_id)
##        for key in p:
##            if key not in ('Start_time', 'End_time', 'venue', 'league_id'):
##                date_tuple = key.split('/')
##                s = get_time(date_tuple, start_time_tuple)
##                e = get_time(date_tuple, end_time_tuple)
##                if not is_overlap(s, e, venue):
##                    va = VenueAvailability(venue=venue,
##                                           time_start=s,
##                                           time_end=e,
##                                           comment='auto generated date')
##                    va.save()
##                else:
##                    print 'venue time overlap for ', venue.name, s.strftime("%m/%d/%Y %H:%M"),'-', e.strftime("%H:%M")
##    return build_availability(request, p['league_id'])
##
    
