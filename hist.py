'''
Take Amazon csv and visualize your spending
'''
import pdb
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#pdb.set_trace()
from datetime import datetime

#Initialize variables
date = []
total = []
rownum = 0

# Import the csv file
with open ('sampleHistory.csv') as csvfile:
        amzreader = csv.DictReader(csvfile,delimiter=',')
        for row in amzreader:   
                date.append(datetime.strptime(row['Order Date'], '%m/%d/%y'))
                totalstr = row['Item Total']
                totalstr = totalstr[1:]
                total.append(float(totalstr))
                #print(row['Order Date'])
                rownum = rownum+1

#### Calculate quantities of interest ###
cumtotal = np.cumsum(total)


#### Visualize the data ####

#Plot cumulative total
fig, ax = plt.subplots(211)
#ax.plot_date(date,cumtotal)
plt.plot(date,cumtotal)
plt.ylabel("Cumulative Spend ($)")
fig.autofmt_xdate()
plt.show()


#Plot the distribution of purchase sizes
#plt.subplot(212)
#n, bins, patches = plt.hist(total, 5, normed=1, facecolor='green', alpha=0.75)


#plt.show()


