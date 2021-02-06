import matplotlib.pyplot as plt
import seaborn as sns

flowers_df = sns.load_dataset('iris')
print(flowers_df.describe())
print(flowers_df.columns)
print(flowers_df.species.unique())
plt.figure(figsize=(8, 4.5))
plt.title('Sepal Dimentions')
sns.set_style('darkgrid')
#plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
sns.scatterplot(flowers_df.sepal_length, flowers_df.sepal_width, hue=flowers_df.species, s=70, data= flowers_df)
#plt.hist(flowers_df.sepal_width, bins=[1, 2, 3, 4, 5])
# plt.legend(['SL', 'SW'])
plt.show()
