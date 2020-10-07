FROM python:3.8.6-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg

RUN mkdir code

COPY . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]