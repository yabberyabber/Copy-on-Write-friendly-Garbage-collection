start: stop
	docker build -t pypy-django-serve .
	docker run --name pypyd -d -p 4000:80 pypy-django-serve ./start_server.sh

interactive: stop
	docker build -t pypy-django-serve .
	docker run -it --entrypoint /bin/bash -p 4000:80 pypy-django-serve

stop:
	-docker stop $(shell docker ps -aq --filter name=pypyd)
	-docker rm $(shell docker ps -aq --filter name=pypyd)
