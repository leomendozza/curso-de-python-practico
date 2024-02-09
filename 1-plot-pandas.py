import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./data/avocado.csv") #agrego el csv con el que voy a trabajar 
#print(df.head(5)) #imprimo los 5 primeros elementos

#print(df["region"][:49]) #imprimo 49 regiones

chicago = df[ df["region"] == "Chicago"]
#print(chicago.head(15))

chicago = chicago.set_index("Date") #cambie el indice por la fecha 
chicago = chicago.sort_values(by="Date") #lo ordene por fecha
#print(chicago.head(15))

#grafico

MAX_SAMPLES = 100

precio = chicago["AveragePrice"][: MAX_SAMPLES]
cantidad = chicago["Total Volume"][: MAX_SAMPLES]

plt.plot(precio, label ="precio medio")
plt.plot(cantidad, label="Volume total")
plt.title("precio de los aguacates con respecto al tiempo")
plt.xlabel("fecha")
plt.xticks(rotation=90)
plt.ylabel("precio en $")
plt.legend()
plt.show()