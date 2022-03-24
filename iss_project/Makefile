
#NAME ?= alessandrakeeler

all: build run push

images:
	docker images | grep alessandrakeeler

ps:
	docker ps -a | grep alessandrakeeler

build:
	docker build -t alessandrakeeler/app.py:latest .

run:
	docker run --name "iss_project" -d -p 5013:5000 alessandrakeeler/app.py:latest

push:
	docker push alessandrakeeler/app.py:latest