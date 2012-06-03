from django.template import Context, loader
from toptracks.models import Track, Rank
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum, Avg
import json 
from django.utils.safestring import mark_safe
from django.core.cache import cache

def index(request):
	qyear = request.GET.get('year', '')
	qweek = request.GET.get('week', '')
	if qyear and qweek:
		print 'CACHE MISS - DB Query: Rank.objects'
		billboard = Rank.objects.filter(year=qyear).filter(week=qweek).values('track__artist_name','track__title','position','listener_count').filter(track__isnull=False)
	else:
		billboard = []

	print 'CACHE MISS - DB Query: Track.objects.all()'
	latest_track_list = Track.objects.all()

	print 'CACHE MISS - DB Query: Rank.objects.all()'
	latest_ranks = Rank.objects.all()
	tracks_json = serializers.serialize('json', Track.objects.all())
	t = loader.get_template('toptracks/index.html')

	print len(latest_track_list)
	all_weeks = Rank.objects.values_list('week', flat=True).distinct()

	# # order O(n^2) - terrible double for loop... improve it using outer join / cartesian on sql 
	# for track in latest_track_list:
	# 	print track
	# 	for week in all_weeks:
	# 		print 'a'

	track_total_listeners = Rank.objects.values('track__artist_name').filter(track__isnull=False).annotate(total_listeners=Sum('listener_count'))

	artist_listeners_x_axis = []
	artist_listeners_series = []
	# track total listeners chart series
	for track_listeners in track_total_listeners:
		artist_listeners_x_axis.append( str(track_listeners['track__artist_name']))
		artist_listeners_series.append(track_listeners['total_listeners'])

	# total listeners chart series
	total_listeners = Rank.objects.values('week').annotate(total_listeners=Sum('listener_count'))

	total_listeners_x_axis = []
	total_listeners_series = []
	for week in total_listeners:
		total_listeners_x_axis.append(week['week'])
		total_listeners_series.append(week['total_listeners'])

	billboard_listeners_series = []
	for bb in billboard:
		billboard_listeners_series.append(bb['listener_count']) 

	print billboard_listeners_series

	# print json.dumps(artist_listeners_x_axis[0])
	c = Context({
	    'latest_track_list': latest_track_list,
	    'tracks_json':tracks_json,
	    'all_weeks': all_weeks,
	    'total_listeners':total_listeners[0],
	    'total_listeners_x_axis':total_listeners_x_axis,
	    'total_listeners_series':total_listeners_series,
	    'artist_listeners_x_axis':mark_safe(artist_listeners_x_axis),
	    'artist_listeners_series':artist_listeners_series,
	    'billboard':billboard,
	    'qweek':qweek,
	    'billboard_listeners_series':billboard_listeners_series

	})
	return HttpResponse(t.render(c))


def dbdump(request):
	t = loader.get_template('toptracks/dbdump.html')
	alltracks = Track.objects.all();
	allranks = Rank.objects.values('track__id','position','listener_count','year','week').filter(track__isnull=False);
	
	c = Context({
	    'alltracks': alltracks,
	    'allranks':allranks,

	})
	return HttpResponse(t.render(c))

