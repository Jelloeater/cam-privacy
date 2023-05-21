# cam-privacy

[![CodeQL](https://github.com/Jelloeater/cam-privacy/actions/workflows/codeql.yml/badge.svg)](https://github.com/Jelloeater/cam-privacy/actions/workflows/codeql.yml)
[![GitHub](https://img.shields.io/github/license/jelloeater/cam-privacy)](https://github.com/Jelloeater/cam-privacy/blob/main/LICENSE)

## Intro
- Simple glue app to toggle Amcrest Camera Privacy on and off via a GET request
- Uses FastAPI for the webserver endpoint and https://github.com/tchellomello/python-amcrest for Camera control.
- Shoutout to @tchellomello

# How to use
## STEP 1:
- Setup env file

```shell
cp .env.example .env
```
- Fill out the env file with your camera info
- 
## STEP 2:
- You will need to deploy the application on a Linux VM with Docker installed
- The easiest thing to do is to copy your .env file and let Docker Compose handle the rest
- The docker_deploy TaskFile step can be used as reference

## STEP 3:
- You can trigger the privacy mode w/ a simple GET request to the webserver.py endpoints.
- 

## Dev Setup

Install Go-Task --> <https://taskfile.dev/installation/>

```shell
task setup
task docker_build_and_run
```

# Testing

```shell
task test
```

PS I'll be amazed if anyone actually uses this
