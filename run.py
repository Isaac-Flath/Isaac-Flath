import pandas as pd
import calplot
import matplotlib.pyplot as plt

df = pd.read_csv('daily_tracker.csv')
df.Day = pd.to_datetime(df.Day)

df = df.set_index('Day')
fig,ax = plt.subplots(2,2,figsize = (9,2))
for i,col in enumerate(df.columns):
    monthlabels = ['J','F','M','A','May']
    calplot.yearplot(df[col], cmap='PiYG', ax = ax[i//2][i%2], dropzero= True, monthticks=False, dayticks=False) #, 
    ax[i//2][i%2].set_title(f"{col} Daily Tracker")

fig.savefig('2024.png')