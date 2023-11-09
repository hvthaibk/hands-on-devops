FROM --platform=linux/amd64 ubuntu:22.04 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Install Ubuntu packages
RUN apt-get update &&\
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev openssl git &&\
    apt-get install -y software-properties-common ca-certificates &&\
    apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libssl-dev libreadline-dev libffi-dev wget libbz2-dev libsqlite3-dev && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install Python3
ARG PYTHON_VERSION=3.10.13
RUN mkdir /python && cd /python && \
    wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -zxvf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ls -lhR && \
    ./configure --enable-optimizations && \
    make install && \
    rm -rf /python

# Install Tesseract 5, current version in Ubuntu 22.04 official repo is 4
RUN add-apt-repository ppa:alex-p/tesseract-ocr-devel
RUN apt-get install -y tesseract-ocr

# Create symlinks for python and pip
RUN ln -s /usr/local/bin/python3 /usr/local/bin/python & \
    ln -s /usr/local/bin/pip3 /usr/local/bin/pip

RUN echo $(which python3)
RUN echo $(which pip3)
RUN echo $(which python)
RUN echo $(which pip)
RUN echo $(tesseract --version)
RUN echo $(python3 --version)
RUN echo $(pip3 --version)
RUN echo $(python --version)
RUN echo $(pip --version)

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Copy the source code into the container.
COPY . .

# Switch to the non-privileged user to run the application.
USER appuser

# Expose the port that the application listens on.
EXPOSE 5000

# Run the application.
WORKDIR /app
CMD python3 -m flask run --host=0.0.0.0
