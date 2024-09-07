import requests
import json
import time

BASE_URL = "http://127.0.0.1:5000"

def get_cliente(cliente_id):
    response = requests.get(f"{BASE_URL}/clientes")
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error: {response.status_code}")

# def create_cliente(data):
#     response = requests.post(f"{BASE_URL}/clientes", json=data)
#     if response.status_code == 201:
#         print("Cliente creado con éxito")
#         print(json.dumps(response.json(), indent=4))
#     else:
#         print(f"Error: {response.status_code}")

# def get_solicitud(solicitud_id):
#     response = requests.get(f"{BASE_URL}/solicitudes/{solicitud_id}")
#     if response.status_code == 200:
#         print(json.dumps(response.json(), indent=4))
#     else:
#         print(f"Error: {response.status_code}")

# def create_solicitud(data):
#     response = requests.post(f"{BASE_URL}/solicitudes", json=data)
#     if response.status_code == 201:
#         print("Solicitud creada con éxito")
#         print(json.dumps(response.json(), indent=4))
#     else:
#         print(f"Error: {response.status_code}")

if __name__ == "__main__":
    cliente_id = 1  # Puedes cambiar el ID del cliente según sea necesario

    while True:
        for _ in range(10):
            get_cliente(cliente_id)
            time.sleep(1)  # Espera 30 segundos entre cada petición

        print("Esperando 5 minutos antes de la siguiente ronda de peticiones...")
        time.sleep(300)

