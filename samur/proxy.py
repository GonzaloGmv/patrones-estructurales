from samur.composite import DocumentoComponent, Documento
import pandas as pd

class Proxy(DocumentoComponent):
    def __init__(self, real_component: DocumentoComponent):
        self._real_component = real_component

    def _verificar(self, usuario, contrasena):
        autorizados = pd.read_csv("samur/csv/usuarios.csv")
        # Verifica si el usuario existe
        if usuario in autorizados['Usuario'].values.tolist():
            # Verifica si la contraseña coincide
            index = autorizados.index[autorizados['Usuario'] == usuario].tolist()[0]
            contrasena_real = autorizados.at[index, 'Contraseña']
            if contrasena == contrasena_real:
                print('Inicio de sesión exitoso. ¡Bienvenido de nuevo!')
                return True
            else:
                print('La contraseña no coincide.')
                return False
        else:
            print('El usuario no está autorizado.')
            return False
        
    def acceso_documento(self):
        usuario = input("Ingrese el usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        
        if self._verificar(usuario, contrasena):
            self._real_component.acceso_documento(usuario)
            return True
        else:
            print(f"Acceso denegado para el usuario {usuario}.")
            return False
        
    def mostrar_info(self, autorizado):
        if autorizado:
            self._real_component.mostrar_info()

    def obtener_tamano(self, autorizado):
        if autorizado:
            return self._real_component.obtener_tamano()
    
    def mostrar_contenido(self, autorizado):
        if autorizado:
            self._real_component.mostrar_contenido()
    
    def agregar(self, autorizado):
        if autorizado:
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
            self._real_component.agregar(documento)
    
    def eliminar(self, autorizado):
        if autorizado:
            self._real_component.eliminar()
    