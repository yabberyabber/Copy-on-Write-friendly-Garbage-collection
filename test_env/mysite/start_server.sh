#!/usr/bin/env sh

/etc/init.d/nginx start
#uwsgi --socket mysite.sock --pypy-wsgi mysite.wsgi --chmod-socket=666
uwsgi --ini mysite_uwsgi.ini
