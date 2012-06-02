from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=200)
    rank = models.IntegerField()
    listener_count = models.IntegerField()
    artist_name = models.CharField(max_length=200)
    week = models.IntegerField()
    year = models.IntegerField()
    def __unicode__(self):
        return str(self.year) + "." + str(self.week) +  ": " + str(self.rank) + " - " + self.artist_name + " - " + self.title + " - " + str(self.listener_count) + " listeners" 
