import csv
with open ('sampleHistory.csv') as csvfile:
	amzreader = csv.DictReader(csvfile,delimiter=',')
	amzreader
 	for row in amzreader:
 		#print(row['Order Date'])
		print type(row['Order Date'])
