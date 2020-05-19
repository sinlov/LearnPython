.PHONY: test check clean build dist all

ROOT_DOCKER_IMAGE_NAME ?= learn-python
ROOT_DOCKER_IMAGE_TAG ?= 1.0.0

dockerLocalImageRemove:
	-docker image rm -f $(ROOT_DOCKER_IMAGE_NAME):$(ROOT_DOCKER_IMAGE_TAG)

dockerImagesBuild: dockerLocalImageRemove
	docker build --tag $(ROOT_DOCKER_IMAGE_NAME):$(ROOT_DOCKER_IMAGE_TAG) .
	@echo "=> build success image info is"
	-docker image inspect --format='{{ .Created}}' $(ROOT_DOCKER_IMAGE_NAME):$(ROOT_DOCKER_IMAGE_TAG)
	@echo ""
	@echo "=> in docker-compose.yml use as\nservices:\n  $(ROOT_DOCKER_IMAGE_NAME):\n    image: learn-python:1.0.0"

help:
	@echo "~> make dockerLocalImageRemove  -- remove build image as: $(ROOT_DOCKER_IMAGE_NAME):$(ROOT_DOCKER_IMAGE_TAG)"
	@echo "~> make dockerImagesBuild  -- build new image as $(ROOT_DOCKER_IMAGE_NAME):$(ROOT_DOCKER_IMAGE_TAG)"