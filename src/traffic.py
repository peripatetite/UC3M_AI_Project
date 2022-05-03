import csv
import numpy as np

with open('../resources/TrafficData.txt') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';')
    for row in csvReader:
        print(row)