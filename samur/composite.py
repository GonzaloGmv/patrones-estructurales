from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd

# Componente base: Documento
class DocumentoComponent(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

    @abstractmethod
    def obtener_tamano(self, componente):
        pass

# Hoja: Documento
class Documento(DocumentoComponent):
    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.tipo = tipo
        self.tamano = tamano

    def mostrar_info(self):
        print(f"{self.nombre}: {self.tipo}, Tamaño: {self.tamano}")
    
    def obtener_tamano(self):
        return self.tamano

# Hoja: Enlace
class Link(DocumentoComponent):
    def __init__(self, nombre, vinculo):
        self.nombre = nombre
        self.vinculo = vinculo

    def mostrar_info(self):
        print(f"{self.nombre}: Link a {self.vinculo}")
    
    def obtener_tamano(self):
        return 0

# Composite: Carpeta
class Carpeta(DocumentoComponent):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
    
    # Funcion para crear las carpetas. No lo hago desde agregar() porque no quiero que el usuario tenga que ingresar los documentos
    def add(self, componente):
        self.elementos.append(componente)
    
    def acceso(self, usuario):
        hora_acceso = datetime.now()
        print(f"Acceso a la carpeta '{self.nombre}' registrado para el usuario {usuario} el {hora_acceso}.")
        registro = pd.read_csv("samur/csv/registro.csv")
        nueva_fila = pd.DataFrame({'Usuario': [usuario], 'Carpeta': [self.nombre], 'Archivo': [self.nombre],'Operacion':['Acceso'], 'Fecha': [hora_acceso]})
        registro = pd.concat([registro, nueva_fila], ignore_index=True)
        registro.to_csv("samur/csv/registro.csv", index=False)
    
    def acceso_documento(self, usuario):
        # Pedir nombre del documento
        nombre = input("Ingrese el nombre del documento: ")
        # Buscar el documento
        for elemento in self.elementos:
            if elemento.nombre == nombre:
                # Acceder al documento
                elemento.mostrar_info()
                # Guardar registro en el csv
                registro = pd.read_csv("samur/csv/registro.csv")
                nueva_fila = pd.DataFrame({'Usuario': [usuario], 'Carpeta': [self.nombre], 'Archivo': [nombre],'Operacion':['Acceso'], 'Fecha': [datetime.now()]})
                registro = pd.concat([registro, nueva_fila], ignore_index=True)
                registro.to_csv("samur/csv/registro.csv", index=False)
                break
        else:
            print(f"El documento {nombre} no existe o no está en esta carpeta.")
            return None
    
    def mostrar_info(self, usuario):
        print(f"Carpeta: {self.nombre}, Tamaño total: {self.obtener_tamano()}")
        # Guardar registro en el csv
        registro = pd.read_csv("samur/csv/registro.csv")
        nueva_fila = pd.DataFrame({'Usuario': [usuario], 'Carpeta': [self.nombre], 'Archivo': [self.nombre],'Operacion':['Mostrar info'], 'Fecha': [datetime.now()]})
        registro = pd.concat([registro, nueva_fila], ignore_index=True)
        registro.to_csv("samur/csv/registro.csv", index=False)

    def obtener_tamano(self):
        return sum([elemento.obtener_tamano() for elemento in self.elementos])
    
    def mostrar_contenido(self, usuario):
        for elemento in self.elementos:
            print(elemento.nombre)
        # Guardar registro en el csv
        registro = pd.read_csv("samur/csv/registro.csv")
        nueva_fila = pd.DataFrame({'Usuario': [usuario], 'Carpeta': [self.nombre], 'Archivo': [self.nombre],'Operacion':['Mostrar contenido'], 'Fecha': [datetime.now()]})
        registro = pd.concat([registro, nueva_fila], ignore_index=True)
        registro.to_csv("samur/csv/registro.csv", index=False)

    def agregar(self, usuario):
        # Pedir nombre del documento
        nombre = input("Ingrese el nombre del documento: ")
        # Pedir tipo de documento
        tipo = input("Ingrese el tipo de documento: ")
        # Pedir tamaño del documento. Asegurarse de que sea un número
        while True:
            try:
                tamano = int(input("Ingrese el tamaño del documento: "))
                break
            except ValueError:
                print("El tamaño debe ser un número.")
        # Crear el documento
        documento = Documento(nombre, tipo, tamano)
        # Agregar el documento a la carpeta
        self.elementos.append(documento)
        print(f"El documento {nombre} ha sido agregado.")
        # Guardar registro en el csv
        registro = pd.read_csv("samur/csv/registro.csv")
        nueva_fila = pd.DataFrame({'Usuario': [usuario], 'Carpeta': [self.nombre], 'Archivo': [nombre],'Operacion':['Agregar'], 'Fecha': [datetime.now()]})
        registro = pd.concat([registro, nueva_fila], ignore_index=True)
        registro.to_csv("samur/csv/registro.csv", index=False)

    def eliminar(self, usuario):
        # Pedir nombre del documento
        nombre = input("Ingrese el nombre del documento: ")
        # Buscar el documento
        for elemento in self.elementos:
            if elemento.nombre == nombre:
                # Eliminar el documento de la carpeta
                self.elementos.remove(elemento)
                print(f"El documento {nombre} ha sido eliminado.")
                # Guardar registro en el csv
                registro = pd.read_csv("samur/csv/registro.csv")
                nueva_fila = pd.DataFrame({'Usuario': [usuario], 'Carpeta': [self.nombre], 'Archivo': [nombre],'Operacion':['Eliminar'], 'Fecha': [datetime.now()]})
                registro = pd.concat([registro, nueva_fila], ignore_index=True)
                registro.to_csv("samur/csv/registro.csv", index=False)
                break
        else:
            print(f"El documento {nombre} no existe.")