import requests
import json

# URL base de la API
url_base = "https://66b4e5529f9169621ea4c37d.mockapi.io/api/v1/contactos"

# ID del registro que deseas modificar
registro_id = "25"  # Cambia este valor al ID del registro que quieras modificar

# Datos actualizados para el registro
datos_actualizados = {
    "nombre": "Alejandro Santana",
    "pais": "MX",
    "estado": "HGO",
    "ciudad": "Actopan",
    "imagen": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/717.jpg",
    "genero": "Men"
}

# URL completa con el ID del registro
url = f"{url_base}/{registro_id}"

# Realiza la solicitud PUT a la API para modificar el registro
response = requests.put(url, json=datos_actualizados)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Muestra la respuesta de la API con los detalles del registro modificado
    data = response.json()
    print("Registro modificado exitosamente:")
    for key, value in data.items():
        print(f"{key}: {value}")

else:
    print(f"Error al modificar el registro. Código de estado: {response.status_code}")