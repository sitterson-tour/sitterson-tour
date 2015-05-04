Sitterson Tour Django Project
=============================

# Local Development Installation
This project is intended to run on an Ubuntu linux system in production. To reliably emulate this environment for development we will be using two tools, Vagrant and Virtualbox. By virtualizing our develoment environments we can also install the system much more quickly, and with reproducability across a wide range of OSes. 

## Install Vagrant and Virtualbox:
[Vagrant](https://www.vagrantup.com/downloads.html)

[Virtualbox](https://www.virtualbox.org/wiki/Downloads)

## Clone this Repository:
````
git clone https://github.com/sitterson-tour/tournamint.git
```

## Start Vagrant:

In this repo's root directory you should find a `Vagrantfile`. This file is our configuration for our development environment. To start it up, run:
```
vagrant up
```
The first time you run this it will take some time (15+ minutes). This is because you will have to wait for vagrant to download the .iso file it will deploy. You should only have to download this the first time. Subsequent `vagrant up` commands will run more quickly. 

## SSH into our Vagrant box:
```
vagrant ssh
```
## Set up Virtualenv
Virtualenv is a tool that helps us isolate our python level dependencies. We can guarantee that we're always running with the same python packages, which helps keep our environments consistant. Run the following commands after ssh-ing into your vagrant box. If you want to understand what it's doing take a look at this [virtualenv tutorial](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
```
cd ~/
virtualenv venv
source venv/bin/activate
cd /vagrant/requrements
sudo pip install -r local.txt
```

## Create Database

```
cd /vagrant/tour/
python manage.py syncdb
```
The syncdb command will ask you to create a new user. Creat one with the `username: demo`, and `password: demo`. This account will be used by our functional testing suite. 

## Start Development Server
```
python manage.py runserver 0.0.0.0:8000 --settings=tour.settings.dev
```

I recommend saving that command in a script or an alias that allows you to quickly launch your app. 

## Check to see if it's working

Back on your host machine open up a webrowser. You should be able to see the app running at: 
*[localhost:8888](http://localhost:8888/)

You can access the admin interface at: 
*[localhost:8888/admin](http://localhost:8888/admin/)
