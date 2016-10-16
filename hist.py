import pdb
import csv
import numpy as np
import matplotlib.pyplot as plt
#pdb.set_trace()
from datetime import datetime
date = []
total = []
rownum = 0
with open ('sampleHistory.csv') as csvfile:
	amzreader = csv.DictReader(csvfile,delimiter=',')
 	for row in amzreader:	
		date.append(datetime.strptime(row['Order Date'], '%m/%d/%y'))
		totalstr = row['Item Total']
		totalstr = totalstr[1:]
		total.append(float(totalstr))
 		#print(row['Order Date'])
		#print type(row['Order Date'])
		rownum = rownum+1
cumtotal = np.cumsum(total)
#print type(totalstr)
#print total[0]
#print date[0]
fig, ax = plt.subplots()
ax.plot_date(date,cumtotal)
plt.plot(date,cumtotal)
plt.ylabel("Cumulative Spend ($)")
fig.autofmt_xdate()
plt.show()
