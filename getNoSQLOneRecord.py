import requests
import json

# URL base de la API
url_base = "https://66b4e5529f9169621ea4c37d.mockapi.io/api/v1/contactos"

# ID del registro que deseas consultar
registro_id = "2"  # Cambia este valor al ID del registro que quieras obtener

# URL completa con el ID del registro
url = f"{url_base}/{registro_id}"

# Realiza la solicitud GET a la API
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Obtiene los datos en formato JSON
    data = response.json()

    # Muestra todos los campos del registro en formato plano
    print("Datos del registro:")
    for key, value in data.items():
        print(f"{key}: {value}")

else:
    print(f"Error al consultar la API. Código de estado: {response.status_code}")