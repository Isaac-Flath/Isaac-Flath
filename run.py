import pandas as pd
import calplot
import matplotlib.pyplot as plt

df = pd.read_csv('daily_tracker.csv')
df.Day = pd.to_datetime(df.Day)

df = df.set_index('Day')
fig,ax = plt.subplots(len(df.columns),1,figsize = (10,8))
for i,col in enumerate(df.columns):
    calplot.yearplot(df[col], cmap='PiYG', ax = ax[i], dropzero= True) #, 
    ax[i].set_title(f"Daily {col} Tracker")

fig.savefig('2024.png')