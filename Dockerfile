# pull official base image
FROM python:3.9


# set work directory
WORKDIR /usr/src/djangostripe
ADD . /usr/src/djangostripe

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /usr/src/djangostripe/docker-entrypoint.sh

ENTRYPOINT ["/usr/src/djangostripe/docker-entrypoint.sh"]