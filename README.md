# porch_light

[![CodeQL](https://github.com/Jelloeater/cam_privacy/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/Jelloeater/cam_privacy/actions/workflows/codeql.yml)
[![GitHub](https://img.shields.io/github/license/jelloeater/cam_privacy)](https://github.com/Jelloeater/cam_privacy/blob/main/LICENSE)

## Intro


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
- Just make sure to remove it after you've deployed, so you don't leave your API keys lying around :-)
- Having SSH keys setup will make the deployment easier
- The docker_deploy task step can be used as reference

## STEP 3:
- You can trigger the privacy mode w/ a simple GET request to the webserver.py endpoints.


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
