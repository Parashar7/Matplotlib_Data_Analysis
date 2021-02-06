import matplotlib.pyplot as plt
import seaborn as sns

flowers_df= sns.load_dataset('iris')
print(flowers_df.info())

plt.figure(figsize=(8,4.5))
plt.bar(flowers_df.species, flowers_df.sepal_length)
plt.plot(flowers_df.species, flowers_df.sepal_length, 'o--r')
plt.bar(flowers_df.species, flowers_df.sepal_width)
#sns.heatmap()
plt.show()