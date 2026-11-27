run-api:
	uvicorn api.fast:app --reload

docker-build-local:
	docker build -t ${DOCKER_IMAGE_NAME}:dev .

docker-run:
	docker run -p 8001:8000 ${DOCKER_IMAGE_NAME}:dev


####################################

docker-build-cloud:
	docker build --platform linux/amd64 -t ${GAR_IMAGE_NAME}:prod .

docker-auth-cloud:
	gcloud auth configure-docker ${GCP_REGION}-docker.pkg.dev

docker-create-artifact-cloud:
	gcloud artifacts repositories create ${DOCKER_REPO_NAME} \
		--repository-format=docker \
		--location=${GCP_REGION} \
		--description="Repository for storing Docker images"

docker-push-cloud:
	docker push ${GAR_IMAGE_NAME}:prod

docker-run-cloud:
	gcloud run deploy --image ${GAR_IMAGE_NAME}:prod --region ${GCP_REGION}

