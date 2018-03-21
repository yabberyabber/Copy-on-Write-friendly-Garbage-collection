start: stop
	docker build -t pypy-django-serve .
	docker run -m 4g --cpus=3 --name pypyd -d -p 4000:80 -p 4001:81 pypy-django-serve ./start_server.sh

interactive: stop
	docker build -t pypy-django-serve .
	docker run -m 4g --cpus=3 -it --entrypoint /bin/bash -p 4000:80 -p 4001:81 pypy-django-serve

stop:
	-docker stop $(shell docker ps -aq --filter name=pypyd)
	-docker rm $(shell docker ps -aq --filter name=pypyd)
