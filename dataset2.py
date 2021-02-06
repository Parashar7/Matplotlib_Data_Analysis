import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

flowers_df = sns.load_dataset('iris')
print(flowers_df.shape)
print(flowers_df.info)
print(flowers_df.describe())
print(flowers_df.columns)
print(flowers_df.species.unique())
print(flowers_df.nunique())

setosa_h = flowers_df[flowers_df.species == 'setosa']
versicolor_h = flowers_df[flowers_df.species == 'versicolor']
virginica_h = flowers_df[flowers_df.species == 'virginica']
plt.figure(figsize=(8, 4.5))
#plt.hist(setosa_h.sepal_width, bins=np.arange(2, 5, 0.25), alpha=.8)
#plt.hist(versicolor_h.sepal_width, bins=np.arange(2, 5, 0.25))
plt.xlabel('Sepal Width')
plt.ylabel('Number of flowers')
plt.legend(['Setosa', 'Verginica'])
plt.hist([setosa_h.sepal_width, versicolor_h.sepal_width], bins=np.arange(2, 5, 0.25), stacked=True)
plt.show()
