import requests
import pandas as pd
import json

# URL de la API
url = "https://66b4e5529f9169621ea4c37d.mockapi.io/api/v1/contactos"

# Realiza la solicitud GET a la API
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Obtiene los datos en formato JSON
    data = response.json()

    # Formatea y muestra los datos en JSON
    print(json.dumps(data, indent=4))

    # Convierte los datos a un DataFrame
    df = pd.DataFrame(data)

    # Muestra el DataFrame
    print("\nDataFrame:")
    print(df)

    # Exporta el DataFrame a un archivo CSV
    csv_filename = "contactos.csv"
    df.to_csv(csv_filename, index=False)
    print(f"\nDatos exportados a {csv_filename} exitosamente.")

else:
    print(f"Error al consultar la API. Código de estado: {response.status_code}")