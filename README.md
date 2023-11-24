# Hands-on DevOps

Docker, GitHub Actions

## Setup

[Docker Desktop](https://docs.docker.com/desktop/install/ubuntu/) on Ubuntu

#### Local GitHub Actions runs

A [guide](https://blog.logrocket.com/guide-using-act-github-actions/) to using [act](https://github.com/nektos/act) with GitHub Actions.

```
act -j
act -j ci-python -s DOCKER_USERNAME={YOUR_ID} -s DOCKERHUB_TOKEN={YOUR_TOKEN}
```

#### [`pre-commit`](https://pre-commit.com/) hooks
```
pre-commit install
pre-commit run --all-files
```

## References

- How to fix [docker: Got permission denied](https://stackoverflow.com/a/65938290).
