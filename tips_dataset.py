import matplotlib.pyplot as plt
import seaborn as sns

tips_df = sns.load_dataset('tips')
print(tips_df)
print(tips_df.describe())
print(tips_df.info)
print(tips_df.day.unique)
plt.figure(figsize=(8,4.5))
#plt.bar(tips_df.day, tips_df.total_bill)
#plt.bar('day', 'total_bill', data=tips_df)
#sns.barplot('day', 'total_bill', data=tips_df)
sns.barplot('day', 'total_bill', data=tips_df, hue='sex')
plt.show()
