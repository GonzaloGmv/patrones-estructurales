from samur.composite import Documento, Link, Carpeta
from samur.proxy import Proxy
from samur.crear import CrearCarpetas

def main_samur():
    # Crear carpetas
    carpetas = CrearCarpetas()
    carpetas.carpeta1()
    carpetas.carpeta2()
    carpeta1 = carpetas.lista_carpetas[0]
    carpeta2 = carpetas.lista_carpetas[1]

    # Crear los proxy para controlar el acceso a las carpetas
    proxy_carpeta1 = Proxy(carpeta1, usuarios_autorizados=["usuario1", "usuario2"])
    proxy_carpeta2 = Proxy(carpeta2, usuarios_autorizados=["usuario1", "usuario2"])

    autorizado1 = proxy_carpeta1.acceso_documento()
    proxy_carpeta1.mostrar_info(autorizado1)
    proxy_carpeta1.obtener_tamano(autorizado1)
    proxy_carpeta1.mostrar_contenido(autorizado1)

    autorizado2 = proxy_carpeta2.acceso_documento()
    proxy_carpeta2.mostrar_info(autorizado2)
    proxy_carpeta2.obtener_tamano(autorizado2)
    proxy_carpeta2.mostrar_contenido(autorizado2)