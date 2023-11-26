from samur.composite import Documento, Link, Carpeta

class CrearCarpetas():
    def __init__(self):
        self.lista_carpetas = []

    def carpeta1(self):
        doc1 = Documento("Documento 1", "Texto", 10)
        doc2 = Documento("Documento 2", "Imagen", 20)
        link1 = Link("Link 1", "Documento 1")
        carpeta1 = Carpeta("Carpeta 1")
        carpeta1.agregar(doc1)
        carpeta1.agregar(doc2)
        carpeta1.agregar(link1)
        self.lista_carpetas.append(carpeta1)
    
    def carpeta2(self):
        doc3 = Documento("Documento 3", "Video", 10)
        doc4 = Documento("Documento 4", "CSV", 20)
        link2 = Link("Link 2", "Documento 4")
        carpeta2 = Carpeta("Carpeta 2")
        carpeta2.agregar(doc3)
        carpeta2.agregar(doc4)
        carpeta2.agregar(link2)
        self.lista_carpetas.append(carpeta2)