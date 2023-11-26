from samur.composite import DocumentoComponent, Carpeta

class Proxy(DocumentoComponent):
    def __init__(self, real_component: DocumentoComponent, usuarios_autorizados):
        self._real_component = real_component
        self.usuarios_autorizados = usuarios_autorizados

    def _verificar(self, usuario):
        # Comprueba que el usuario exista y que esté en la lista de usuarios autorizados
        if usuario and usuario in self.usuarios_autorizados:
            return True
        else:
            return False
        
    def acceso_documento(self):
        usuario = input("Ingrese el usuario: ")
        
        if self._verificar(usuario):
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
        
    