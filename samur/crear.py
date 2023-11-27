from samur.composite import Documento, Link, Carpeta
import pandas as pd

class CrearCarpetas():
    def __init__(self, df):
        self.df = df
        self.lista_carpetas = []

    def crear_carpetas(self):
        # Crear carpetas iniciales
        carpeta1 = Carpeta("Carpeta 1")
        carpeta2 = Carpeta("Carpeta 2")

        # Leer archivo csv y añadir documentos a las carpetas
        df = pd.read_csv(self.df)
        for index, row in df.iterrows():
            carpeta_nombre, nombre, tipo, tamano, vinculo = row

            if carpeta_nombre == "Carpeta 1":
                self._añadir_a_carpeta(carpeta1, nombre, tipo, tamano, vinculo)
            elif carpeta_nombre == "Carpeta 2":
                self._añadir_a_carpeta(carpeta2, nombre, tipo, tamano, vinculo)

        # Añadir carpetas a la lista
        self.lista_carpetas.append(carpeta1)
        self.lista_carpetas.append(carpeta2)

    # Funcion privada para añadir documentos a las carpetas
    def _añadir_a_carpeta(self, carpeta, nombre, tipo, tamano, vinculo):
        if isinstance(vinculo, str) and vinculo.strip() != "":
            # Crear enlace
            documento_vinculado = next((elemento for elemento in carpeta.elementos if isinstance(elemento, Documento) and elemento.nombre == vinculo), None)
            if documento_vinculado is not None:
                link = Link(nombre, documento_vinculado)
                carpeta.add(link)
        else:
            # Crear documento
            documento = Documento(nombre, tipo, int(tamano))
            carpeta.add(documento)