from abc import ABC, abstractmethod

# Clase Component
class MenuComponent(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass

# Clase Leaf
class Elemento(MenuComponent):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

# Clase Composite
class MenuComposite(MenuComponent):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)

    def obtener_precio(self):
        precio_total = sum(elemento.obtener_precio() for elemento in self.elementos)
        return precio_total

# Clase Composite Compuesto por dos menús simples
class MenuCompuesto(MenuComponent):
    def __init__(self, nombre, menu1, menu2):
        self.nombre = nombre
        self.menu1 = menu1
        self.menu2 = menu2

    def obtener_precio(self):
        precio_total = self.menu1.obtener_precio() + self.menu2.obtener_precio()
        return precio_total
    
def elegir_bebida():
    print("\nBebidas disponibles:")
    print("1. Coca Cola")
    print("2. Zumo")
    print("3. Agua")
    while True:
        eleccion_bebida = input("Elige un número de bebida: ")
        if eleccion_bebida == "1":
            bebida = "Coca Cola"
            break
        elif eleccion_bebida == "2":
            bebida = "Zumo"
            break
        elif eleccion_bebida == "3":
            bebida = "Agua"
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    return bebida
    
# Crear menús
menu_a = MenuComposite("Menu 1")
menu_a.agregar(Elemento("Patatas", 5))
menu_a.agregar(Elemento("Pizza Barbacoa", 12))
menu_a.agregar(Elemento("Helado", 4))

menu_b = MenuComposite("Menu 2")
menu_b.agregar(Elemento("Patatas", 5))
menu_b.agregar(Elemento("Pizza Margarita", 10))
menu_b.agregar(Elemento("Helado", 4))

# Preguntar al usuario si desea un menú simple o uno compuesto
while True:
    eleccion_tipo_menu = input("¿Deseas un menú simple (S) o uno compuesto (C)? ").upper()
    if eleccion_tipo_menu == "S":
        # Mostrar elementos de los menús. Al precio de cada menú se le suma 1 € por la bebida que se añadirá después
        print("Menús simples disponibles:")
        print(f"\n1. Menu A:  {menu_a.obtener_precio() + 1} €")
        for elemento in menu_a.elementos:
            print(f"- {elemento.nombre}")

        print(f"\n2. Menu B:  {menu_b.obtener_precio() + 1} €")
        for elemento in menu_b.elementos:
            print(f"- {elemento.nombre}")

        # Pedir al usuario que elija un menú
        while True:
            eleccion_menu = input("\nElige un número de menú: ")
            if eleccion_menu == "1":
                menu = menu_a
                menu.agregar(Elemento(elegir_bebida(), 1))
                break
            elif eleccion_menu == "2":
                menu = menu_b
                menu.agregar(Elemento(elegir_bebida(), 1))
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

        break
    elif eleccion_tipo_menu == "C":
        print("Opciones para Menú Compuesto:")
        print(f"1. Menu Simple 1 + Menu Simple 1 {menu_a.obtener_precio() + menu_a.obtener_precio() + 2} €")
        print(f"2. Menu Simple 2 + Menu Simple 2 {menu_b.obtener_precio() + menu_b.obtener_precio() + 2} €")
        print(f"3. Menu Simple 1 + Menu Simple 2 {menu_a.obtener_precio() + menu_b.obtener_precio() + 2} €")
        eleccion_menu_compuesto = input("Elige una opción (1, 2, 3): ")
        if eleccion_menu_compuesto == "1":
            menu = MenuCompuesto("Menu Compuesto 1", menu_a, menu_a)
            menu.menu1.agregar(Elemento(elegir_bebida(), 1))
            menu.menu2.agregar(Elemento(elegir_bebida(), 1))
        elif eleccion_menu_compuesto == "2":
            menu = MenuCompuesto("Menu Compuesto 2", menu_b, menu_b)
            menu.menu1.agregar(Elemento(elegir_bebida(), 1))
            menu.menu2.agregar(Elemento(elegir_bebida(), 1))
        elif eleccion_menu_compuesto == "3":
            menu = MenuCompuesto("Menu Compuesto 3", menu_a, menu_b)
            menu.menu1.agregar(Elemento(elegir_bebida(), 1))
            menu.menu2.agregar(Elemento(elegir_bebida(), 1))
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

# Calcular y mostrar el precio total del menú
precio_total = menu.obtener_precio()
print(f"\nPrecio Total del Menú: {precio_total} €")
