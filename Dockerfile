FROM tamuarch/django_docker_base
MAINTAINER John Phillips <johnphillips@arch.tamu.edu>

RUN mkdir /var/www/www.arch

#RUN pip install git+https://github.tamu.edu/architecture/app.profile@14.6.3#tamu.coa.app.profile

ADD . /var/www/www.arch

WORKDIR /var/www/www.arch

RUN python bootstrap.py

RUN bin/buildout
