import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Abrimos el archivo
path = r"C:\Users\USUARIO\Desktop\Mensual.xlsx"
file = pd.read_excel(io=path)

# Creamos los diccionarios
meses = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0}
meses_str = {"Enero":0,"Febrero":0,"Marzo":0,"Abril":0,"Mayo":0,"Junio":0,"Julio":0,"Agosto":0,"Septiembre":0,"Octubre":0,"Noviembre":0,"Diciembre":0}

# Vamos sumando todos los valores de la variacion porcentual de cada mes
for i, row in file.iterrows():
    meses[str(pd.to_datetime(row['Fecha']).month)] += row['Variacion']
    
# Tenemos 51 veces cada mes ya que 2021-1970 = 51
for i in meses:
    meses.update({f"{i}": (meses.get(i)/51)*100})

# Copiamos los values al segundo diccionario para el plotting:
for i in meses_str:
    meses_str.update({f"{i}":(meses.get(i))})

# Codigo para colores TO-DO iterar y comprobar si el value es > 0 o no 
colors = ['green', 'green', 'green', 'green', 'green','green','green','green','red','green','green','green']
plt.figure(figsize=(17, 10))
plt.bar(list(meses_str.keys()), meses.values(), color=colors, edgecolor = 'black')
plt.xlabel('Mes del año')
plt.ylabel('Variacion (%)')
plt.title('S&P500 : 01/01/1970 - 23/06/2021')
plt.xticks(rotation=45)
plt.tick_params(axis='x', labelsize=12)
plt.show()
