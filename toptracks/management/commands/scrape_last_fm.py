from django.core.management.base import BaseCommand
# from minnpost.dockets.models import Case
from toptracks.models import Track, Rank

import requests
import lxml
from lxml import html
import time, datetime
import inspect
from pprint import pprint

class Command(BaseCommand):
    help = 'Scrapes last fm top 10 tracks - arg1 is unix datetime, if ommited, datetime set to now'

    def handle(self, *args, **options):
        self.stdout.write('\nScraping started at %s\n' % str(datetime.datetime.now()))

        if len(args) == 1:
            week_val = datetime.datetime.fromtimestamp(int(args[0])).isocalendar()[1]
            year_val = datetime.datetime.fromtimestamp(int(args[0])).isocalendar()[0]
            url = 'http://www.last.fm/charts/tracks/top/place/all?ending=' + args[0]
        else:
            now = datetime.datetime.now()
            year_val = now.isocalendar()[0]
            week_val = now.isocalendar()[1]
            url = 'http://www.last.fm/charts/tracks/top/place/all'

        self.stdout.write('Scraping url: %s\n' % url)
        r = requests.get(url)
        root = lxml.html.fromstring(r.content)

        for li in root.cssselect('div.rankedChart ol li.rankItem')[0:10]:
            rank_val = li.cssselect('span.rankItem-position')[0].text_content().strip().replace('.','')
            raw = li.cssselect('span.rankItem-title')[0].text_content()
            artist_and_title = raw.encode("ascii", "replace").split('???')
            listener_count_val = int(li.cssselect('span.rankItem-bar-percentage span')[0].text_content().strip().replace(' listeners','').replace(',',''))
            artist_val = ''
            title_val = ''
            if len(artist_and_title) > 1:
                artist_val = artist_and_title[0].strip()
                title_val = artist_and_title[1].strip()
            track = Track.objects.get_or_create(artist_name=artist_val, title=title_val)
            rank = Rank.objects.get_or_create(track=track[0], position=rank_val,week=week_val,year=year_val,listener_count=listener_count_val)
            # t = Track.objects.get_or_create(artist_name=artist_val, rank=int(rank_val), title=title_val,listener_count=listener_count_val, week=week_val, year=year_val)
            print "Added track:  " + str(track[0])
            print "at position: " + str(rank[0])
            
now = time.gmtime(time.time())

def convertTime(t):
    """Converts times in format HH:MMPM into seconds from epoch (but in CST)"""
    convertedTime = time.strptime(t + ' ' + str(now.tm_mon) + ' ' + str(now.tm_mday) + ' ' + str(now.tm_year), "%I:%M%p %m %d %Y")
    return time.mktime(convertedTime)
    # This used to add 5 * 60 * 60 to compensate for CST