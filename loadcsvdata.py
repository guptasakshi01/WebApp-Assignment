import csv
import os
path = 'D:\Corpus.CSV'
from csvapp.models import csvdata
with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] and row[1]:
            print row[0]
            print type(row[1])
            p = csvdata(key=row[0],value=row[1])
            p.save()