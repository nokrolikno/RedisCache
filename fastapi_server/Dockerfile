FROM ubuntu:latest

WORKDIR /home

COPY . /home

RUN apt-get update && apt-get install -y pip && \
    pip install -r requirements.txt

CMD ["uvicorn", "--app-dir", "src", "--host", "0.0.0.0", "--port", "7777", "server:app"]
