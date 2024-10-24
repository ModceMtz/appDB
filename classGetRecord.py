import requests

class GetRecord:
    __url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def get_class_record(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            data = response.json()

            if data:
                ultimo_registro = data[-1]
                return ultimo_registro
            else:
                return "No se encontraron registros."
        except Exception as e:
            return f"Error: {e}"