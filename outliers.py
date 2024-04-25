import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('Hello outliers0')
df= pd.read_csv('Ventas_totales_sinnulos.csv', index_col=0)
#print(df.head()) 

valores_nulos=df.isnull().sum()
valores_nulos

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente")
#plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y=df["ventas_precios_corrientes"]
print(y)