FROM python:3.10

RUN mkdir /app
WORKDIR /app

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONPATH=/app
ENV FLASK_APP=app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
