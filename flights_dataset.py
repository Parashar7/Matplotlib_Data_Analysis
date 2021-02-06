import matplotlib.pyplot as plt
import seaborn as sns

flights_df = sns.load_dataset('flights').pivot('month', 'year', 'passengers')
print(flights_df.shape)
#print(flights_df)
#plt.figure(figsize=(8, 4.5))
#plt.title('Passengers Footfall')
#sns.barplot('month', 'passengers', data=flights_df, hue='year')
sns.heatmap(flights_df, fmt='d', annot=True, cmap='Blues')
plt.show()
