#!/bin/bash

echo "------------------------------------"
echo "Update repo"
echo "------------------------------------"
echo ""
cd /home/ubuntu/trottoir
git fetch
git reset --hard origin/master
sudo git clean -d -x -f -e ve/ -e node_modules/ db.sqlite3
echo " "

echo "------------------------------------"
echo "Install any new packages into env"
echo "------------------------------------"
echo ""
/home/ubuntu/trottoir/ve/bin/pip install -r /home/ubuntu/trottoir/requirements.txt
echo " "

echo "----------------"
echo "Upgrade Node env"
echo "----------------"
npm install

echo "---------------------------"
echo "Build the production bundle"
echo "---------------------------"
npm run build

echo "------------------------------------"
echo "Collect Static"
echo "------------------------------------"
echo ""
sudo /home/ubuntu/trottoir/ve/bin/python /home/ubuntu/trottoir/apps/manage.py collectstatic --noinput --clear --settings=trottoir.production_settings
echo " "

echo "------------------------------------"
echo "Migrate Apps"
echo "------------------------------------"
echo ""
/home/ubuntu/trottoir/ve/bin/python /home/ubuntu/trottoir/apps/manage.py migrate --settings=trottoir.production_settings
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

echo "-----------------------------------------------"
echo "Restart uWSGI Emperor service to restart Django"
echo "-----------------------------------------------"
sudo systemctl restart emperor.uwsgi.service

