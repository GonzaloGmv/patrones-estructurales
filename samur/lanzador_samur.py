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

    numero = input("A que carpeta desea acceder?(1/2): ")
    if numero == "1":
        proxy_carpeta = Proxy(carpeta1)
        autorizado = proxy_carpeta.acceso()
    elif numero == "2":
        proxy_carpeta = Proxy(carpeta2)
        autorizado = proxy_carpeta.acceso()
    else:
        print("Opcion no valida")
    
    if autorizado:
        while True:
            print("¿Que desea hacer?")
            print("1. Acceder a un documento de la carpeta")
            print("2. Mostrar información de la carpeta")
            print("3. Mostrar contenido de la carpeta")
            print("4. Agregar un documento a la carpeta")
            print("5. Eliminar un documento de la carpeta")
            print("6. Salir")
            opcion = input("Ingrese la opción: ")
            if opcion == "1":
                proxy_carpeta.acceso_documento(autorizado)
            elif opcion == "2":
                proxy_carpeta.mostrar_info(autorizado)
            elif opcion == "3":
                proxy_carpeta.mostrar_contenido(autorizado)
            elif opcion == "4":
                proxy_carpeta.agregar(autorizado)
            elif opcion == "5":
                proxy_carpeta.eliminar(autorizado)
            elif opcion == "6":
                break