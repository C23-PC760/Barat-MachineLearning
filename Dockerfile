FROM python:3.8.13-slim AS dependencies

WORKDIR /app

EXPOSE 5000

ADD . .


RUN pip3 install --timeout 1000 --retries 10 -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
