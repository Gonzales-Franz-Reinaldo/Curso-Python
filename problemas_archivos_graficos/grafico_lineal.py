import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("problemas_archivos_graficos\\ejercicios.csv")

# creando el grafico 
sns.lineplot(x = "fecha", y = "ejercicios", data = df)

# marcando un punto en el momento que hizo ejercicios
plt.plot("01-12", 16, "o")

# mostrando el grafico 
plt.show()