import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import numpy as np

covid_df = pd.read_csv('result.csv')
# print(covid_df.info())

covid_df['date'] = pd.to_datetime(covid_df.date)
# print(covid_df.info())

covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
# print(covid_df.info())
new_data = covid_df[['new_cases', 'new_deaths', 'Death Rate', 'month']]
print(new_data.shape)

print(new_data.info())
plt.figure(figsize=(8, 4.5))
#plt.title('COVID Data')
# plt.xlabel('Month')
# plt.ylabel('Death Rate')
# plt.bar('month', 'Death Rate', data=covid_df)
# sns.barplot('new_cases', 'month', data=new_data.loc[1000:1100])

# sns.lineplot(x="new_cases", y="new_deaths",hue="month",data=new_data.loc[42700:43000])
sns.jointplot(data=new_data.loc[40950:43000], x="month", y="Death Rate", kind="hex");
plt.show()
