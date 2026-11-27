run-api:
	uvicorn api.fast:app --reload

docker_build_local:
	docker build -t ${DOCKER_IMAGE_NAME}:dev .

docker-run:
	docker run -p 8001:8000 ${DOCKER_IMAGE_NAME}:dev
