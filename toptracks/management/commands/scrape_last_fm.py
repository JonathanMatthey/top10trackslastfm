from django.core.management.base import BaseCommand
# from minnpost.dockets.models import Case
from toptracks.models import Track

import requests
import lxml
from lxml import html
import time, datetime
import inspect
from pprint import pprint

class Command(BaseCommand):
    help = 'Scrapes last fm top 10 tracks'

    def handle(self, *args, **options):
        self.stdout.write('\nScraping started at %s\n' % str(datetime.datetime.now()))

        url = 'http://www.last.fm/charts/tracks/top/place/all?ending=1336305600'

        now = datetime.datetime.now()
        year_val = datetime.datetime.now().isocalendar()[0]
        week_val = 21 #datetime.datetime.now().isocalendar()[1]

        self.stdout.write('Scraping url: %s\n' % url)
        r = requests.get(url)
        root = lxml.html.fromstring(r.content)
        # Find the correct table element, skip the first row
        for li in root.cssselect('div.rankedChart ol li.rankItem')[0:10]:
            rank_val = li.cssselect('span.rankItem-position')[0].text_content().strip().replace('.','')
            raw = li.cssselect('span.rankItem-title')[0].text_content()
            artist_and_title = raw.encode("ascii", "replace").split('???')
            artist_val = ''
            title_val = ''
            if len(artist_and_title) > 1:
                artist_val = artist_and_title[0].strip()
                title_val = artist_and_title[1].strip()

            t = Track.objects.get_or_create(artist_name=artist_val, rank=int(rank_val), title=title_val,listener_count=1, week=week_val, year=year_val)
            print "Added: [ " + rank_val + " ][ " + artist_val + " ][ " + title_val + " ] "

now = time.gmtime(time.time())

def convertTime(t):
    """Converts times in format HH:MMPM into seconds from epoch (but in CST)"""
    convertedTime = time.strptime(t + ' ' + str(now.tm_mon) + ' ' + str(now.tm_mday) + ' ' + str(now.tm_year), "%I:%M%p %m %d %Y")
    return time.mktime(convertedTime)
    # This used to add 5 * 60 * 60 to compensate for CST