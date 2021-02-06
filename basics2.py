import matplotlib.pyplot as plt
import seaborn as sns

years = range(2000, 2012)

apple = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.932, 0.991, 0.921]

oranges = [0.961, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.991, 0.933, 0.945]

plt.figure(figsize=(8, 4.5))
sns.set_style('darkgrid')
#sns.set_style('dak')
# plt.plot(years, apple, marker='o', c='b', ls='-', lw=2, ms=8, mew=2)
# plt.plot(years, oranges, marker='s', c='g', ls='--', lw=4, ms=10, mew=2, alpha=.8)  #alpha gives transpirancy
plt.plot(years, apple, 's--g')  # marker, line, color, MLC
plt.plot(years, oranges, 'o-b')

plt.xlabel('Years')
plt.ylabel('Yields')
plt.title('Yields of Fruits')
plt.legend(['Apple', 'Oranges'])
plt.show()
