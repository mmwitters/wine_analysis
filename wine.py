import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

wine = pd.read_csv('wine.csv', names = ["Cultivator", "Alcohol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])

print(wine.head())

print(wine['Alcohol'].head(10))

X = wine.drop('Cultivator',axis=1)
y = wine['Cultivator']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

scaler = StandardScaler()

scaler.fit(X_train) 
StandardScaler(copy=True, with_mean=True, with_std=True)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)