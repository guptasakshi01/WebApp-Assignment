# WebApp-Assignment
Assignment to create a webapp.

## Assumptions

* Name of csv file to be loaded is Corpus.csv, Although new key value pair can be added in the same file.
* Docker is up and running
* First Column of csv file will be considered as key and second column will be as value.
* If multiple similar keys are present, then value of first key will be returned

## Build Instruction

* Download the project from Repository
* Navigate to project directory
* Execute `docker build -t webapp:v1 .` to build image
* Execute `docker run -it -d -p 8000:8000 --name application webapp:v1` for creating container
* Once Container is created successfully, Try `curl http://127.0.0.1:8000/one` or hit the url in browser

## Technology Used
* Python DJango Framework to create web server
* Docker for building images and running container
* Python modules for loading csv data in Django Default DB sqlite3

## Result Sets
* If key is present in loaded csv
```
http://127.0.0.1:8000/one
{"key": "one", "value": "1"}
```
* If key is not present in csv file
```
 http://127.0.0.1:8000/abc
{"key": "one", "value": "1"}
```
* when none of url matches
```
http://127.0.0.1:8000/
Please try http://127.0.0.1/one
```
