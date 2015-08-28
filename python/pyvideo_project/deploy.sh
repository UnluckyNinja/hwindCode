#!/bin/bash

rm -rf staticfiles/*
export DJANGO_SETTINGS_MODULE=pyvideo.settings.production
/usr/bin/python3 manage.py collectstatic
echo "staticfiles folder updated"

/usr/bin/python3 manage.py check

dt=$(date '+%Y%m%d_%H%M%S');
sudo mv /var/www/pyvideo_project /var/www/pyvideo_project_bak_$dt
sudo cp -R ../pyvideo_project /var/www/pyvideo_project
sudo cp ~/config/config.json /var/www/pyvideo_project/pyvideo/settings/config.json

/usr/bin/python3 /var/www/pyvideo_project/manage.py migrate
echo "project and config files moved to web folder"

sudo service apache2 restart
echo "done"
