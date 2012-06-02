from django.template import Context, loader
from toptracks.models import Track
from django.http import HttpResponse

def index(request):
    latest_track_list = Track.objects.all()
    t = loader.get_template('toptracks/index.html')
    c = Context({
        'latest_track_list': latest_track_list,
    })
    return HttpResponse(t.render(c))