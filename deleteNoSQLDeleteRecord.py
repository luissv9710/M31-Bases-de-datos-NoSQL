import requests

# URL base de la API
url_base = "https://66b4e5529f9169621ea4c37d.mockapi.io/api/v1/contactos"

# ID del registro que deseas eliminar
registro_id = "26"  # Cambia este valor al ID del registro que quieras eliminar

# URL completa con el ID del registro
url = f"{url_base}/{registro_id}"

# Realiza la solicitud DELETE a la API para eliminar el registro
response = requests.delete(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    print(f"Registro con ID {registro_id} eliminado exitosamente.")
else:
    print(f"Error al eliminar el registro. Código de estado: {response.status_code}")