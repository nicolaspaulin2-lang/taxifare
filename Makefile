run-api:
	uvicorn api.fast:app --reload

docker_build_local:
   docker build \
     -t ${DOCKER_IMAGE_NAME}:dev .
