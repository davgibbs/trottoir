#!/bin/bash

echo "------------------------------------"
echo "Update repo"
echo "------------------------------------"
echo ""
cd /opt/myhealthsite
git fetch
git reset --hard origin/master
sudo git clean -d -x -f -e ve/
echo " "

echo "------------------------------------"
echo "Install any new packages into env"
echo "------------------------------------"
echo ""
/home/ubuntu/trottoir/ve/bin/pip install -r /home/ubuntu/trottoir/requirements.txt
echo " "

echo "------------------------------------"
echo "Migrate Apps"
echo "------------------------------------"
echo ""
sudo /home/ubuntu/trottoir/ve/bin/python /home/ubuntu/trottoir/apps/manage.py migrate --settings=trottoir.production_settings
echo " "

echo "------------------------------------"
echo "Collect Static"
echo "------------------------------------"
echo ""
sudo /home/ubuntu/trottoir/ve/bin/python /home/ubuntu/trottoir/apps/manage.py collectstatic --noinput --clear --settings=trottoir.production_settings
echo " "

echo "------------------------------------"
echo "Minimise JavaScript files"
echo "------------------------------------"
echo ""
sudo /home/ubuntu/trottoir/ve/bin/python /home/ubuntu/trottoir/apps/manage.py compress --settings=trottoir.production_settings
echo " "

echo "------------------------------------"
echo "Restarting uwsgi"
echo "------------------------------------"
echo ""
sudo service emperor.uwsgi restart
echo " "

echo "------------------------------------"
echo "Restarting Nginx"
echo "------------------------------------"
echo ""
sudo service nginx restart
echo " "

echo "------------------------------------"
echo "Restarting Celeryd"
echo "------------------------------------"
echo ""
sudo service celeryd restart
echo " "

