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
fig, ax = plt.subplots(2)

#Plot the distribution of purchase sizes
n, bins, patches = ax[0].hist(total, 5,  facecolor='green', alpha=0.75)
ax[0].set_ylabel("# of Purchases")
ax[0].set_xlabel("Dollar Amount")

#Plot cumulative total
ax[1].plot(date,cumtotal)
ax[1].set_ylabel("Cumulative Spend ($)")

#Format figure
plt.setp(plt.xticks()[1],rotation=30, ha='right')
plt.tight_layout()  # Moves axis edges to prevent axis labels from being clipped
plt.show()


