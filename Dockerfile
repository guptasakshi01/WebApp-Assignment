FROM django

ADD . /data

WORKDIR /data

EXPOSE 8000

RUN ["echo","Making Migration for csv model"]

RUN ["python","/data/WebApp/manage.py","makemigrations"]

RUN ["echo","Migrating"]

RUN ["python","/data/WebApp/manage.py","migrate"]

RUN ["echo","Loading CSV File"]

RUN ["python","/data/WebApp/manage.py","loadcsv","/data/Corpus.csv"]

CMD ["python", "/data/WebApp/manage.py", "runserver" ,"0.0.0.0:8000"]
