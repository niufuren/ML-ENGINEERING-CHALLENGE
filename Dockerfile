FROM python:3.10.9

WORKDIR /app 

ADD requirements.txt . 

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "FastAPI_practice/main.py"]