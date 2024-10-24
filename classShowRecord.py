
import tkinter as tk
from classGetRecord import GetRecord

class ShowRecord:
    __textoRegistro = None

    def mostrar_datos(self, registro):
        self.__textoRegistro = (
            f"ID: {registro['id']}\n"
            f"Nombre: {registro['nombre']}\n"
            f"Apellido: {registro['apellido']}\n"
            f"Ciudad: {registro['ciudad']}\n"
            f"Calle: {registro['calle']}"
        )
        resultado_label.config(text=self.__textoRegistro)

class AplicacionEstudiante:
    def __init__(self, master):
        self.master = master
        self.master.title("Último Registro Estudiante")
        self.master.geometry("300x200")

        self.api = GetRecord()

        self.show_record = ShowRecord()

        self.boton = tk.Button(master, text="Obtener Último Registro", command=self.obtener_ultimo_registro)
        self.boton.pack(pady=10)

        global resultado_label
        resultado_label = tk.Label(master, text="", justify="left")
        resultado_label.pack(pady=10)

    def obtener_ultimo_registro(self):
        registro = self.api.get_class_record()

        if isinstance(registro, dict):
            self.show_record.mostrar_datos(registro)
        else:
            resultado_label.config(text=f"Error: {registro}")

root = tk.Tk()
app = AplicacionEstudiante(root)

root.mainloop()
