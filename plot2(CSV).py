import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_df = pd.read_csv('covid_fulldata.txt')
# print(data_df)
# print(data_df.info())
# print(data_df.columns)
# print(data_df.nunique())
# print(data_df.location.unique)

data_df['date'] = pd.to_datetime(data_df.date)
# print(data_df.columns)
# print(data_df.info())

data_df['month'] = pd.DatetimeIndex(data_df.date).month
# print(data_df.info())

data_df['week'] = pd.DatetimeIndex(data_df.date).week
# print(data_df.info())

data_df['day'] = pd.DatetimeIndex(data_df.date).day
# print(data_df.info())
new_df = data_df[['month', 'new_cases', 'new_deaths', 'total_cases', 'total_deaths', 'location']]
#covid = new_df.pivot("month", "new_cases", "location")

#plt.figure(figsize=(8, 9))
sns.set_style('darkgrid')

# plt.plot('month', 'new_cases', data=data_df)

# sns.scatterplot('month', 'new_cases', data=new_df, hue='location')

sns.lineplot(x="month", y="new_cases", hue="location", data=new_df.loc[1000:1300])  # works a little

# plt.hist('month', 'new_cases', data=data_df.loc[100, 200], bins=np.arange(1,12+1,1))

# g = sns.jointplot(data=new_df.loc[1000:1500], x="month", y="new_cases", hue="location", kind="kde")


# f, ax = plt.subplots(figsize=(9, 6))

#sns.heatmap(covid, annot=True, fmt="d", cmap='Blues', linewidths=.5)

#cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
#g = sns.relplot(data=new_df, x="month", y="new_cases", hue="location", palette=cmap, sizes=(10, 200))
#g.set(xscale="log", yscale="log")
#g.ax.xaxis.grid(True, "minor", linewidth=.25)
#g.ax.yaxis.grid(True, "minor", linewidth=.25)
#g.despine(left=True, bottom=True)

plt.title('COVID Data')
# plt.legend(['Month', 'New cases'])
#plt.xlabel('Month')
#plt.ylabel('New Cases')
plt.show()
