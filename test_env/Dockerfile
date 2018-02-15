FROM pypy:2-5

RUN apt update
RUN apt install -y nginx
RUN apt install -y build-essential
RUN apt install -y nano less vim
RUN pypy -m pip install django==1.10.6
RUN pypy -m pip install uwsgi

COPY django_applet /usr/share/nginx/html

RUN ldconfig

COPY mysite /mysite
WORKDIR /mysite
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /mysite/mysite_nginx.conf /etc/nginx/sites-enabled/default

#RUN pypy manage.py collectstatic

#RUN uwsgi --http :8000 --pypy-wsgi-file mysite/test.py --pypy-lib /usr/local/bin/libpypy-c.so
EXPOSE 80


RUN echo "PS1='\[\033[01;31m\]DOCKER\[\033[00m\]:\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\n> '" >> /root/.bashrc

#CMD ["nginx", "-g", "daemon off;"]
#CMD /etc/init.d/nginx start
#CMD uwsgi --http :80 --pypy-wsgi mysite.wsgi
