import pandas as pd
import os

def unir_csv_carpeta(carpeta):
    lista_df = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.csv'):
            ruta = os.path.join(carpeta, archivo)
            df = pd.read_csv(ruta)
            lista_df.append(df)
    df_total = pd.concat(lista_df, ignore_index=True)
    return df_total

def main():
    carpeta = 'DATA'  # Carpeta donde tienes los CSV
    df = unir_csv_carpeta(carpeta)

    # Convertir Arrival a fecha
    df['Arrival'] = pd.to_datetime(df['Arrival'], errors='coerce')

    # Crear columna con el año
    df['Year'] = df['Arrival'].dt.year

    # Agrupar por año y contar reservas
    reservas_por_ano = df.groupby('Year').size()

    print('Reservas por año:')
    print(reservas_por_ano)

    # Guardar CSV unido si quieres
    df.to_csv('reservas_unidas.csv', index=False)
    print('✅ CSV combinado guardado como reservas_unidas.csv')

if __name__ == '__main__':
    main()





