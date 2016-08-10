FROM ubuntu:14.04

RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi python python-pip python2.7-dev libmysqlclient-dev
COPY apache /etc/apache2/sites-available/000-default.conf
#RUN service apache2 restart

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

EXPOSE 80
CMD exec /usr/sbin/apache2ctl -D FOREGROUND