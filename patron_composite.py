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

# Crear menús
menu1 = MenuComposite("Menu 1")
menu1.agregar(Elemento("Patatas", 5))
menu1.agregar(Elemento("Pizza Barbacoa", 12))
menu1.agregar(Elemento("Helado", 4))

menu2 = MenuComposite("Menu 2")
menu2.agregar(Elemento("Patatas", 5))
menu2.agregar(Elemento("Pizza Margarita", 10))
menu2.agregar(Elemento("Helado", 4))

# Mostrar elementos de los menús. Al precio de cada menú se le suma 1 € por la bebida que se añadirá después
print("Menús disponibles:")
print(f"\n1. Menu 1:  {menu1.obtener_precio() + 1} €")
for elemento in menu1.elementos:
    print(f"- {elemento.nombre}")

print(f"\n2. Menu 2:  {menu2.obtener_precio() + 1} €")
for elemento in menu2.elementos:
    print(f"- {elemento.nombre}")

# Pedir al usuario que elija un menú
while True:
    eleccion_menu = input("\nElige un número de menú: ")
    if eleccion_menu == "1":
        menu = menu1
        break
    elif eleccion_menu == "2":
        menu = menu2
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

# Pedir al usuario que elija una bebida y agregarla al menú
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

menu.agregar((Elemento(bebida, 1)))

# Calcular y mostrar el precio total del menú
precio_total = menu.obtener_precio()
print(f"\nPrecio Total del Menú: {precio_total} €")
