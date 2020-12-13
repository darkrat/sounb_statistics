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
