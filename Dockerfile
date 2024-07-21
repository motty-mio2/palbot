FROM python:3.11-slim

WORKDIR /workdir
COPY . /workdir/


RUN pip install --no-cache-dir -r /workdir/requirements.lock

ENTRYPOINT [ "python", "/workdir/src/main.py" ]