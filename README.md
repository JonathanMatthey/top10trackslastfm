hi everybody ! it's Dr Nick

![Alt text](http://images.wikia.com/simpsons/images/5/5e/Dr._Riviera.png)

***

This is a small demo app built using django and sqlite 3 locally, deployed to heroku on postgresql.

It scrapes lastfm top 10 tracks, stores them in a db and then spits them back in a view with basic table lookup and javascript charts:

demo:  
http://lastfm-analytics.herokuapp.com/?year=2012&week=22

admin:  
http://lastfm-analytics.herokuapp.com/admin

username: mattheyj  
password: asdasd

***

this is a django app 1.4

docs available at:

https://docs.djangoproject.com/en/dev/releases/1.4/

clone this using:

    git clone git@github.com:manymengofishing/top10trackslastfm.git
    cd top10trackslastfm

access shell:  

    python manage.py shell

sql statements generated using

    python manage.py sql toptracks
    python manage.py sqlclear toptracks

setup db:  

    python manage.py syncdb

run the server:  

    python manage.py runserver     


run scraping command that runs for current week: 

    python manage.py scrape_last_fm

also there's a shell script that will scrape the last 4 months, run it using 

    ./scrape_last_3months.sh


