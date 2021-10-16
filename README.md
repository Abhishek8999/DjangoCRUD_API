# DjangoCRUD_API
==> DJANGO PROJECT NAME : python_api
==> APPLICATION NAME : api
==> DATABASES = MongoDB
        'ENGINE': 'djongo',
        'NAME': 'pythonapidatabase',

  database setting in settings.py file:
	DATABASES = {
 	   'default': {
	   'ENGINE': 'djongo',
  	   'NAME': 'pythonapidatabase',
    	   }
	}
--------------------------------------
=======================================

==>   MODELS:
	Participants
	Song
	Podcast
	AudioBook

==> All the Models Registered in admin.py file

==> seralizers.py file: To convers complex data into JSON

==> views.py file : it contained all the logic that acts on the incoming HTTP requests

==> urls.py file: contains API endpoint URL to request and submit data

---------------------------------------------------------------------------------------
=======================================================================================

==> REQUIREMENTS AND INSTALLED PACKAGES:
appdirs==1.4.4
asgiref==3.4.1
astroid==2.8.2
async-generator==1.10
attrs==21.2.0
autopep8==1.5.7
backports.entry-points-selectable==1.1.0
beautifulsoup4==4.10.0
certifi==2021.10.8
cffi==1.15.0
chardet==4.0.0
charset-normalizer==2.0.7
colorama==0.4.4
cryptography==35.0.0
distlib==0.3.3
Django==3.2.8
django-cors-headers==3.10.0
djangorestframework==3.12.4
djangorestframework-jsonapi==4.2.1
djongo==1.3.6
dnspython==2.1.0
filelock==3.3.0
future==0.18.2
h11==0.12.0
html==1.13
idna==3.3
importlib-metadata==4.8.1
importlib-resources==5.2.2
inflection==0.5.1
isort==5.9.3
Jinja2==3.0.2
jsonparser==1.0
lazy-object-proxy==1.6.0
MarkupSafe==2.0.1
mccabe==0.6.1
mongo==0.2.0
outcome==1.1.0
platformdirs==2.4.0
pycodestyle==2.8.0
pycparser==2.20
pylint==2.11.1
pymongo==3.12.0
pyOpenSSL==21.0.0
pypiwin32==223
python-dateutil==2.8.2
pytz==2021.3
pywin32==302
PyYAML==6.0
render==1.0.0
reqs==0.0.2
requests==2.26.0
selenium==4.0.0
serializers==0.2.4
six==1.16.0
sniffio==1.2.0
sortedcontainers==2.4.0
soupsieve==2.2.1
sqlparse==0.2.4
toml==0.10.2
trio==0.19.0
trio-websocket==0.9.2
typing-extensions==3.10.0.2
urllib3==1.26.7
virtualenv==20.8.1
whitenoise==5.3.0
win10toast==0.9
wrapt==1.12.1
wsproto==1.0.0
zipp==3.6.0
=============================================
=============================================

==> PROCEDURE

	--> Windows 10, RAM-minimum 4 GB, Processor-ntel(R) Core(TM) i5-10210U CPU @ 1.60GHz 2.11 GHz
	--> Install Python 3.10
	--> Install Django 1.3.6
	--> Install VS Code
	--> Install MongoDB
	--> Open project folder in VS Code
	--> Connect MongoDB 
	--> Open the terminal and run the command:
		 python manage.py createsuperuser
	--> Open terminal in VS Code run the command
		 python manage.py runserver
	--> development server will start at http://127.0.0.1:8000/
	--> Open the link into the browser
	--> open the urls.py file of the project and check the endpoints one by one
	--> Below are the all endpoints:
		admin
		songlcapi
		podcastlcapi
		audiobooklcapi
		songrudapi
		audiobookrudapi
		podcastrudapi

	--> Below is the example how to implement the url in browser
		http://127.0.0.1:8000/songrudapi/1


