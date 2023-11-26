from samur.composite import DocumentoComponent, Documento

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
    