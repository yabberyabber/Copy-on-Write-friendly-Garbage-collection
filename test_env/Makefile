start: stop
	docker build -t pypy-django-serve .
	docker run -m 8g --cpus=3 --name pypyd -d -p 4000:80 -p 4001:81 pypy-django-serve ./start_server.sh

interactive: stop
	docker build -t pypy-django-serve .
	docker run -m 8g --cpus=3 -it --entrypoint /bin/bash -p 4000:80 -p 4001:81 pypy-django-serve

stop:
	-docker stop $(shell docker ps -aq --filter name=pypyd)
	-docker rm $(shell docker ps -aq --filter name=pypyd)

# make start && sleep 10 && httperf --port=4000 --num-conns=X > 16m_N_Xkreq_8g.httperf
