FROM python:3.12-alpine

EXPOSE 6969/tcp

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache g++ gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del g++ gcc musl-dev 

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./server.py" ]