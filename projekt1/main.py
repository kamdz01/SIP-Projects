from ucimlrepo import fetch_ucirepo
import pandas as pd

# fetch dataset
automobile = fetch_ucirepo(id=10)

# data (as pandas dataframes)
X = automobile.data.features
y = automobile.data.targets

# metadata
# print(automobile.metadata)

# # variable information
# print(automobile.variables)

# Wyświetlenie pierwszych 10 rekordów cech (X)
print("\nPierwsze 10 rekordów cech:")
print(X.head(10))

# Wyświetlenie pierwszych 10 rekordów zmiennych docelowych (y)
print("\nPierwsze 10 rekordów zmiennych docelowych:")
print(y.head(10))

# Wyświetlenie połączonych danych (cechy + zmienne docelowe)
print("\nPierwsze 10 rekordów całych danych:")
print(pd.concat([X, y], axis=1).head(10))
