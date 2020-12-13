# sounb_statistics
Статистика СОУНБ
https://drive.google.com/drive/folders/19MKWgGAwx9gabE27erxqFcWeCszShbKu
http://brutusin.org/json-forms/ 



Startup:
sudo apt-get install python3
pip3 install django
pip3 install djangorestframework
django-admin startproject sounb_statistics
python3 manage.py startapp sounbs_api
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py makemigrations
python3 manage.py startapp sounbs_operator
python3 manage.py runserver 0:8080

for apache 
#pip3 install mod_wsgi
sudo apt-get install libapache2-mod-wsgi

/var/www/django/sounb_statistics/sounb_statistics
<VirtualHost *:80>
    #ServerName example.com

    WSGIDaemonProcess example_com processes=2 threads=15 display-name=%{GROUP} python-path=/var/www/django/sounb_statistics
    WSGIProcessGroup sounb_statistics

    WSGIScriptAlias / /var/www/django/sounb_statistics/sounb_statistics/wsgi.py

    <Directory /var/www/django/sounb_statistics/sounb_statistics>
        Order allow,deny
        allow from all
    </Directory>

    LogLevel warn

    Alias /static/ /var/www/example_com//var/www/django/sounb_statistics/static/
    <Directory /var/www/example_com/>
        Options Indexes MultiViews FollowSymLinks
        AllowOverride None
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>