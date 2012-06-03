from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)

    def __unicode__(self):
    	return self.artist_name + " - " + self.title 
        # return str(self.year) + "." + str(self.week) +  ": " + str(self.rank) + " - " + self.artist_name + " - " + self.title + " - " + str(self.listener_count) + " listeners" 

class Rank(models.Model):
    position = models.IntegerField()
    week = models.IntegerField()
    year = models.IntegerField()
    track = models.ForeignKey(Track)
    listener_count = models.IntegerField()

    def __unicode__(self):
    	return str(self.year) + "." + str(self.week) +": " + str(self.position) + " [" + str(self.listener_count) + " listeners]"