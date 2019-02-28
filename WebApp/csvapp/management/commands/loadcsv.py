import csv
import os
from django.core.management.base import BaseCommand, CommandError
from csvapp.models import csvdata

class Command(BaseCommand):

    help = "Loads the csv File data in DB"
    def add_arguments(self, parser):
        parser.add_argument("filename",nargs='+',type=str)
        
    def handle(self, *args, **options):
        path = options["filename"][0]
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] and row[1]:
                    p = csvdata(key=row[0],value=row[1])
                    p.save()
        self.stdout.write("Loaded Successfully")
