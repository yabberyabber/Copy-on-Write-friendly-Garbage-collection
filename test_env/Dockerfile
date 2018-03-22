#FROM pypy:2-5
FROM ubuntu:16.04

RUN apt update  --fix-missing
RUN apt purge -y python2.7-minimal python2.7 python
RUN apt install -y nginx
RUN apt install -y build-essential
RUN apt install -y nano less vim
RUN apt install -y libffi6 libffi-dev

COPY pypy-withpatch/ /pypy-root/
RUN echo "export PATH=\"/pypy-root/pypy/goal:${PATH}\"" >> /root/.bashrc
ENV PATH="/pypy-root/pypy/goal:${PATH}"
RUN export PATH="/pypy-root/pypy/goal:${PATH}"
RUN ln -s /pypy-root/pypy/goal/pypy-c /pypy-root/pypy/goal/pypy

RUN pypy -m pip install django==1.10.6
RUN pypy -m pip install uwsgi

COPY django_applet /usr/share/nginx/html

RUN ldconfig

RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /mysite/mysite_nginx.conf /etc/nginx/sites-enabled/default

#RUN pypy manage.py collectstatic

#RUN uwsgi --http :8000 --pypy-wsgi-file mysite/test.py --pypy-lib /usr/local/bin/libpypy-c.so
EXPOSE 80 81


RUN echo "PS1='\[\033[01;31m\]DOCKER\[\033[00m\]:\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\n> '" >> /root/.bashrc

RUN echo "export PATH=\"/pypy-root/bin:${PATH}\"" >> /root/.bashrc
ENV PATH="/pypy-root/bin:${PATH}"
RUN export PATH="/pypy-root/bin:${PATH}"
RUN ln -s /pypy-root/pypy/goal/libpypy-c.so /usr/lib/libpypy-c.so

COPY mysite /mysite
WORKDIR /mysite
RUN pypy manage.py migrate
