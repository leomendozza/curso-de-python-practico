import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/avocado.csv")

atlanta = df[ df["region"] == "Atlanta"]

precio = atlanta["AveragePrice"]
precioPromediado = precio.rolling(30).mean()
volumen = atlanta["Total Volume"]

bolsasAguacate = atlanta ["Total Bags"]
sbolsas = atlanta ["Small Bags"]
lbolsas = atlanta ["Large Bags"]
xlbolsas = atlanta ["XLarge Bags"]

plt.subplot(221)
plt.title("precio aguacate")
plt.plot(precio, label="Precio", color="green")
plt.plot(precioPromediado, label="Precio Promediado", color="orange")
plt.legend()

plt.subplot(222)
plt.title("Volumen de aguacates")
plt.plot(volumen, label="Volume Total", color="red")
plt.legend()

plt.subplot(223)
plt.title("Bolsas totales de aguacates")
plt.plot(bolsasAguacate, label="Bolsas Totales", color="blue")
plt.legend()

plt.subplot(224)
plt.title("Bolsas por tamaño")
plt.plot(sbolsas, label="Bolsas - S", color="black")
plt.plot(lbolsas, label="Bolsas - L", color="cyan")
plt.plot(xlbolsas, label="Bolsas - XL", color="yellow")
plt.legend()

plt.tight_layout()
plt.show()