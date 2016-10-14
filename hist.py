import csv
from datetime import datetime
date = []
rownum = 0
with open ('sampleHistory.csv') as csvfile:
	amzreader = csv.DictReader(csvfile,delimiter=',')
	amzreader
 	for row in amzreader:	
		date.append(datetime.strptime(row['Order Date'], '%m/%d/%y'))
 		#print(row['Order Date'])
		#print type(row['Order Date'])
		rownum = rownum+1
	print row[0]
