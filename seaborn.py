import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.title("Iris Sepal Length vs. Width")
plt.show()