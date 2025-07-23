import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Cargar datos
df = pd.read_csv('./reservas_unidas.csv')
df['Arrival'] = pd.to_datetime(df['Arrival'])
df['Mes'] = df['Arrival'].dt.month

# Agrupar reservas por mes (suma total de reservas por cada mes)
reservas_mes = df.groupby('Mes').size()

# Crear gráfico de barras mejorado
plt.figure(figsize=(10,6))
plt.bar(reservas_mes.index, reservas_mes.values, color='skyblue')

# Cambiar etiquetas del eje X a nombres de meses con rotación para mejor lectura
plt.xticks(reservas_mes.index, [calendar.month_name[i] for i in reservas_mes.index], rotation=45)

# Agregar etiquetas numéricas encima de cada barra
for i, v in enumerate(reservas_mes.values):
    plt.text(reservas_mes.index[i], v + max(reservas_mes.values)*0.01, str(v), ha='center', fontsize=9)

# Títulos y etiquetas
plt.title('Reservas Totales por Mes', fontsize=14)
plt.xlabel('Mes')
plt.ylabel('Cantidad de Reservas')

# Cuadrícula en eje Y para mejor referencia visual
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('./RESULTADOS/reservas_por_mes.png')
plt.show()

