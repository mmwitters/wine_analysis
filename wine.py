import pandas as pd
import matplotlib.pyplot as plt

wine = pd.read_csv('wine.csv', names = ["Cultivator", "Alcohol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])

print(wine.head())

print(wine['Alcohol'].head(10))

plt.plot(wine['Malic_Acid'])
plt.show()