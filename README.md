Sitterson Tour Django Project
=============================

# Local Development Installation
This project is intended to run on an Ubuntu linux system in production. To reliably emulate this environment for development we will be using two tools, Vagrant and Virtualbox. By virtualizing our develoment environments we can also install the system much more quickly, and with reproducability across a wide range of OSes. 

## Install Vagrant and Virtualbox:
(Vagrant)[https://www.vagrantup.com/downloads.html]
(Virtualbox)[https://www.virtualbox.org/wiki/Downloads]

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
