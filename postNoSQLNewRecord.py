import requests
import json

# URL de la API
url = "https://66b4e5529f9169621ea4c37d.mockapi.io/api/v1/contactos"

# Datos del nuevo registro que deseas agregar
nuevo_registro = {
    "nombre": "Lus Santana",
    "pais": "México",
    "estado": "Hidalgo",
    "ciudad": "Pachuca",
    "imagen": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/717.jpg",
    "genero": "Man"
}

# Realiza la solicitud POST a la API para agregar el nuevo registro
response = requests.post(url, json=nuevo_registro)

# Verifica si la solicitud fue exitosa
if response.status_code == 201:
    # Muestra la respuesta de la API con los detalles del nuevo registro agregado
    data = response.json()
    print("Registro agregado exitosamente:")
    for key, value in data.items():
        print(f"{key}: {value}")

else:
    print(f"Error al agregar el registro. Código de estado: {response.status_code}")