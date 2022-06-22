FROM python:3.8.5-slim-buster

RUN apt-get update -y; \
    apt-get install make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev -y
WORKDIR /workspace/
COPY requirements/requirements.txt ./
RUN pip install -r requirements.txt

ENV TZ="UTC-3"
RUN date

COPY ./src/ ./
CMD ["python", "main.py"]
