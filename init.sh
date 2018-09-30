sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default.conf
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
cd /home/box/web/ask
sudo killall gunicorn
gunicorn -b 0.0.0.0:8000 ask.wsgi:application -D
#sudo /etc/init.d/gunicorn stop
#sudo /etc/init.d/mysql start
sudo /etc/init.d/nginx restart
