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
        
    def acceso(self):
        usuario = input("Ingrese el usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        
        if self._verificar(usuario, contrasena):
            self._real_component.acceso(usuario)
            return usuario
        else:
            return 0
    
    def acceso_documento(self, autorizado):
        if autorizado != 0:
            self._real_component.acceso_documento(autorizado)
        
    def mostrar_info(self, autorizado):
        if autorizado != 0:
            self._real_component.mostrar_info(autorizado)

    def obtener_tamano(self, autorizado):
        if autorizado != 0:
            return self._real_component.obtener_tamano(autorizado)
    
    def mostrar_contenido(self, autorizado):
        if autorizado != 0:
            self._real_component.mostrar_contenido(autorizado)
    
    def agregar(self, autorizado):
        if autorizado != 0:
            self._real_component.agregar(autorizado)
    
    def eliminar(self, autorizado):
        if autorizado != 0:
            self._real_component.eliminar(autorizado)
    