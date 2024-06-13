FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt ./

RUN apk update
RUN apk add bash
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]
