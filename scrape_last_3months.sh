#!/bin/bash
UNIXTIME=1335096000
for i in {1..16}
do
	python manage.py scrape_last_fm $UNIXTIME
	let "UNIXTIME -= 604800"
done