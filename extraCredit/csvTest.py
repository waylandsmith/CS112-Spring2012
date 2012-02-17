#!/usr/bin/env python

import csv

testReader = csv.reader(open("test3.csv", "rb"))

for row in testReader:
    print row
