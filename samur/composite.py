from abc import ABC, abstractmethod
from datetime import datetime

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
    
    def acceso_documento(self, usuario):
        print(f"Acceso a la carpeta '{self.nombre}' registrado para el usuario {usuario} el {datetime.now()}.")
        for elemento in self.elementos:
            if hasattr(elemento, 'acceso_documento'):
                elemento.acceso_documento(usuario)

    def mostrar_info(self):
        print(f"Carpeta: {self.nombre}, Tamaño total: {self.obtener_tamano()}")

    def obtener_tamano(self):
        return sum([elemento.obtener_tamano() for elemento in self.elementos])
    
    def mostrar_contenido(self):
        for elemento in self.elementos:
            elemento.mostrar_info()

    def agregar(self, documento):
        self.elementos.append(documento)

    def eliminar(self):
        # Pedir nombre del documento
        nombre = input("Ingrese el nombre del documento: ")
        # Buscar el documento
        for elemento in self.elementos:
            if elemento.nombre == nombre:
                # Eliminar el documento de la carpeta
                self.elementos.remove(elemento)
                print(f"El documento {nombre} ha sido eliminado.")
                break
        else:
            print(f"El documento {nombre} no existe.")