FROM --platform=linux/amd64 ubuntu:22.04 as base


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
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Install Tesseract 5, current version in Ubuntu 22.04 official repo is 4
RUN add-apt-repository ppa:alex-p/tesseract-ocr-devel
RUN apt-get install -y tesseract-ocr

# Switch to the non-privileged user to run the application.
USER appuser

# Run the application.
CMD ["tesseract"]
