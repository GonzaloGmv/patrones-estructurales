from abc import ABC, abstractmethod

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

    def mostrar_info(self):
        print(f"Carpeta: {self.nombre}, Tamaño total: {self.obtener_tamano()}")

    def agregar(self, componente):
        self.elementos.append(componente)

    def eliminar(self, componente):
        self.elementos.remove(componente)

    def mostrar_contenido(self):
        for elemento in self.elementos:
            elemento.mostrar_info()
    
    def obtener_tamano(self):
        return sum([elemento.obtener_tamano() for elemento in self.elementos])

# Ejemplo de Uso
if __name__ == "__main__":
    # Crear documentos y carpetas
    doc1 = Documento("Documento 1", "Texto", 10)
    doc2 = Documento("Documento 2", "Imagen", 20)
    link1 = Link("Link 1", "Documento 1")
    carpeta1 = Carpeta("Carpeta 1")
    carpeta1.agregar(doc1)
    carpeta1.agregar(doc2)
    carpeta1.agregar(link1)

    # Mostrar la información y el contenido de la carpeta
    carpeta1.mostrar_info()
    carpeta1.mostrar_contenido()
