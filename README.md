# patrones-estructurales

El link a este repositorio es: [github](https://github.com/GonzaloGmv/patrones-estructurales)

## Ejercicio 1. Pizzería

Lo nuevo de este ejercicio está implementado casi todo en la carpeta menus.

En primer lugar está el patrón composite, que consta de una clase abstracta componente y una clase hojas y clases compuestas que heredan de la clase componente. Este patrón de diseño está implementado para crear los menús, que se crean en la función pedir_menu() de la clase Menu. En esta función, en primer lugar se crea cada objeto menú y se le van añadiendo los elementos con la función agregar(). A continuación el usuario elige el menú y se le añade la/s bebida/s a dicho menú. Además gracias a este patrón podemos calcular el precio de cada menú sumando el precio de cada componente.

En la clase Menu también estan otras 2 funciones encargadas de guardar el número del menú pedido por el cliente. Además hay dos funciones que se encargan de devolver los menús pedidos anteriores pedidos por el cliente.

En la clase cliente están las funciones encargadas de enviar la lista de números de pedidos anteriores a las funciones que devuelven la lista con los elementos de estos pedidos.

A continuación los códigos para las pizzas personalizadas. Estos códigos se hicieron en la práctica anterior y no había que tocar mucho más.

### Patrón Builder:
```
from __future__ import annotations
from abc import ABC, abstractmethod
from collections import Counter

# Abstract Builder
class Builder(ABC):
    @property
    @abstractmethod
    def pizza(self):
        pass

    # Definición de métodos abstractos para construir partes de la pizza
    @abstractmethod
    def produce_masa(self):
        pass

    @abstractmethod
    def produce_salsa(self):
        pass

    @abstractmethod
    def produce_ingredientes(self):
        pass

    @abstractmethod
    def produce_coccion(self):
        pass

    @abstractmethod
    def produce_presentacion(self):
        pass

    @abstractmethod
    def produce_borde(self):
        pass

    @abstractmethod
    def produce_extra(self):
        pass

# Clase ConcreteBuilder que implementa la interfaz Builder
class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._pizza = Pizza()

    @property
    def pizza(self):
        pizza = self._pizza
        self.reset()
        return pizza

    # Implementación de métodos para construir partes de la pizza
    def produce_masa(self):
        while True:
            print("\n Seleccione el número correspondiente al tipo de masa de pizza:")
            print("1. Masa Fina")
            print("2. Masa Gruesa")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self._pizza.add("Masa Fina")
                print('\n')
                break
            elif opcion == "2":
                self._pizza.add("Masa Gruesa")
                print('\n')
                break
            else:
                print("Opción no válida. Por favor, seleccione un número válido. \n")

    def produce_salsa(self):
        while True:
            print("Seleccione el número correspondiente al tipo de salsa de pizza:")
            print("1. Salsa de Tomate")
            print("2. Salsa de Pesto")
            print("3. Salsa Barbacoa")
            print("4. Salsa Ranch")
            print("5. Salsa Alfredo")
            print("6. Salsa Carbonara")
            print("7. Ninguna")


            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self._pizza.add("Salsa de Tomate")
                print('\n')
                break
            elif opcion == "2":
                self._pizza.add("Salsa de Pesto")
                print('\n')
                break
            elif opcion == "3":
                self._pizza.add("Salsa Barbacoa")
                print('\n')
                break
            elif opcion == "4":
                self._pizza.add("Salsa Ranch")
                print('\n')
                break
            elif opcion == "5":
                self._pizza.add("Salsa Alfredo")
                print('\n')
                break
            elif opcion == "6":
                self._pizza.add("Salsa Carbonara")
                print('\n')
                break
            elif opcion == "7":
                print('\n')
                break
            else:
                print("Opción no válida. Por favor, seleccione un número válido. \n")

    def produce_ingredientes(self, cliente, pedido):
        ingredientes_principales = ["Jamón", "Pepperoni", "Champiñones", "Aceitunas", "Pimientos", "Cebolla", "Tomate", "Maíz","Pollo", "Salchichas", "Atún", "Pavo", "Anchoas", "Espinacas", "Albóndigas", "Broccoli", "Huevos", "Alcaparras", "Piña", "Rúcula", "Chorizo", "Carne de res", "Carne de cerdo","Aguacate", "Camarones", "Ajo", "Ricotta", "Jalapeños", "Queso Mozzarella", "Queso Cheddar", "Queso Parmesano", "Queso Gouda", "Ingrediente especial: La 33", "Queso Provolone", "Queso Feta"]

        # Bucle para seleccionar los ingredientes. En caso de que seleccione más de 8, se le pide que seleccione de nuevo
        while True:
            print("Seleccione hasta 8 ingredientes principales para su pizza (ingrese números separados por comas, máximo 8):")
            # Imprime los ingredientes
            for i, ingrediente in enumerate(ingredientes_principales, 1):
                print(f"{i}. {ingrediente}")

            # Llama a la funcion acceder_pedidos para obtener los ingredientes de los pedidos anteriores del cliente
            ingredientes_anteriores = cliente.acceder_pizzas(pedido)
            # Cuenta la frecuencia de cada ingrediente
            contador_ingredientes = Counter(ingredientes_anteriores)
            # Obtiene los 5 ingredientes más comunes
            ingredientes_repes = contador_ingredientes.most_common(5)
            # Imprime los ingredientes más comunes
            if ingredientes_repes:
                print("\nNuestras sugerencias basándonos en tus anteriores pedidos:", ", ".join(f"{ingrediente}" for ingrediente, frecuencia in ingredientes_repes))

            opcion = input("\nIngrese los números de los ingredientes deseados: ")
            ingredientes_elegidos = []

            if opcion:
                try:
                    seleccion = [int(x) for x in opcion.split(',')]
                    # Lee los números ingresados y los añade a una lista
                    for num in seleccion:
                        if 1 <= num <= len(ingredientes_principales):
                            ingredientes_elegidos.append(ingredientes_principales[num - 1])
                        else:
                            print(f"Opción {num} no válida. Se omitirá.")
                    # Verifica que no se hayan seleccionado más de 8 ingredientes
                    if len(ingredientes_elegidos) <= 8:
                        self._pizza.add("Ingredientes " + "/".join(ingredientes_elegidos))
                        print('\n')
                        break
                    else:
                        print("Seleccione un máximo de 8 ingredientes principales. \n")
                except ValueError:
                    print("Entrada no válida. Inténtelo de nuevo.")
            else:
                print("No se seleccionaron ingredientes principales. \n")
    
    def produce_coccion(self):
        while True:
            print("Seleccione el número correspondiente al grado de cocción de la pizza:")
            print("1. Poco hecha")
            print("2. En su punto")
            print("3. Muy hecha")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self._pizza.add("Poco Hecha")
                print('\n')
                break
            elif opcion == "2":
                self._pizza.add("En su Punto")
                print('\n')
                break
            elif opcion == "3":
                self._pizza.add("Muy Hecha")
                print('\n')
                break
            else:
                print("Opción no válida. Por favor, seleccione un número válido. \n")

    def produce_presentacion(self) -> None:
        while True:
            print("Seleccione el número correspondiente a la opción de presentación de la pizza:")
            print("1. En plato")
            print("2. En caja")
            print("3. Para llevar")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self._pizza.add("En Plato")
                print('\n')
                break
            elif opcion == "2":
                self._pizza.add("En Caja")
                print('\n')
                break
            elif opcion == "3":
                self._pizza.add("Para Llevar")
                print('\n')
                break
            else:
                print("Opción no válida. Por favor, seleccione un número válido. \n")

    
    def produce_borde(self):
        while True:
            print("Seleccione el número correspondiente al tipo de borde de la pizza:")
            print("1. Borde de queso")
            print("2. Borde relleno de jamón y queso")
            print("3. Borde de ajo y mantequilla")
            print("4. Borde clásico")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self._pizza.add("Borde de Queso")
                print('\n')
                break
            elif opcion == "2":
                self._pizza.add("Borde Relleno de Jamón y Queso")
                print('\n')
                break
            elif opcion == "3":
                self._pizza.add("Borde de Ajo y Mantequilla")
                print('\n')
                break
            elif opcion == "4":
                self._pizza.add("Borde Clásico")
                print('\n')
                break
            else:
                print("Opción no válida. Por favor, seleccione un número válido. \n")

    def produce_extra(self):
        extras = ["Trufas", "Queso de cabra", "Setas", "Caviar", "Salmón Ahumado"]

        while True:
            print("Seleccione hasta 3 extras gourmet para su pizza (ingrese números separados por comas, máximo 3):")
            print("Precio de cada extra: 2€")
            
            for i, extra in enumerate(extras, 1):
                print(f"{i}. {extra}")

            opcion = input("Ingrese los números de los extras deseados: ")
            extras_elegidos = []

            if opcion:
                try:
                    seleccion = [int(x) for x in opcion.split(',')]
                    # Lee los números ingresados y los añade a una lista
                    for num in seleccion:
                        if 1 <= num <= len(extras):
                            extras_elegidos.append(extras[num - 1])
                        else:
                            print(f"Opción {num} no válida. Se omitirá.")
                    # Verifica que no se hayan seleccionado más de 3 extras
                    if len(extras_elegidos) <= 3:
                        self._pizza.add("Extras " + "/".join(extras_elegidos))
                        print('\n')
                        break
                    else:
                        print("Seleccione un máximo de 3 extras gourmet.")
                except ValueError:
                    print("Entrada no válida. Inténtelo de nuevo. \n")
            else:
                print("No se seleccionaron extras gourmet. Continuar sin extras. \n")

# Clase que representa una pizza y mantiene un registro de sus partes
class Pizza():
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

# Clase Director que coordina la construcción de la pizza
class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_full_featured_product(self, cliente, pedido):
        self.builder.produce_masa()
        self.builder.produce_salsa()
        self.builder.produce_ingredientes(cliente, pedido)
        self.builder.produce_coccion()
        self.builder.produce_presentacion()
        self.builder.produce_borde()
        self.builder.produce_extra()
```

### Clase Pedido para las pizzas personalizadas
```
import pandas as pd

# Clase Pedido
class Pedido():
    def __init__(self, builder):
        # Inicializa la pizza
        self.pizza_pedido = builder.pizza
    
    # Funcion que genera el numero de pedido
    def numero_pedido(self):
        try:
            pedidos_df = pd.read_csv('pizzeria/personalizadas/pizzas.csv')
            if not pedidos_df.empty:
                ultimo_id = pedidos_df['numero'].max()
                nuevo_id = ultimo_id + 1
            else:
                nuevo_id = 1
        except FileNotFoundError:
            nuevo_id = 1

        return nuevo_id
    
    # Funcion que crea un diccionario con las partes de la pizza
    def diccionario(self):
        pedido_dict = {'Masa': [part for part in self.pizza_pedido.parts if 'Masa' in part],
                    'Salsa': [part for part in self.pizza_pedido.parts if 'Salsa' in part],
                    'Ingredientes': [part for part in self.pizza_pedido.parts if 'Ingredientes' in part],
                    'Cocción': [part for part in self.pizza_pedido.parts if 'Poco Hecha' in part or 'En su Punto' in part or 'Muy Hecha' in part],
                    'Presentación': [part for part in self.pizza_pedido.parts if 'En Plato' in part or 'En Caja' in part or 'Para Llevar' in part],
                    'Borde': [part for part in self.pizza_pedido.parts if 'Borde de Queso' in part or 'Borde Relleno de Jamón y Queso' in part or 'Borde de Ajo y Mantequilla' in part or 'Borde Clásico' in part],
                    'Extras Gourmet': [part for part in self.pizza_pedido.parts if 'Extra' in part]}
        # Cada valor del diccionario es una lista, por lo que se convierte a string
        for key in pedido_dict:
            pedido_dict[key] = ' '.join(pedido_dict[key])
        # Elimina las palabras Ingredientes y Extras Gourmet del valor del diccionario
        pedido_dict['Ingredientes'] = pedido_dict['Ingredientes'][13:]
        pedido_dict['Extras Gourmet'] = pedido_dict['Extras Gourmet'][7:]
        return pedido_dict

    # Funcion que guarda el pedido en un archivo csv a partir del diccionario
    def guardar(self):
        # Llama a la funcion diccionario para obtener el diccionario
        pedido_dict = self.diccionario()
        try:
            pedidos_df = pd.read_csv('pizzeria/personalizadas/pizzas.csv')
        except FileNotFoundError:
            pedidos_df = pd.DataFrame(columns=pedido_dict.keys())

        # Crea una nueva clave-valor en el diccionario con el numero de pedido. Para ello llama a la funcion numero_pedido
        pedido_dict['numero'] = self.numero_pedido()

        # Concatea el diccionario con el DataFrame de pedidos y lo guarda en el archivo CSV
        pedidos_df = pd.concat([pedidos_df, pd.DataFrame([pedido_dict])], ignore_index=True)
        pedidos_df['numero'] = pedidos_df['numero'].astype(int)
        pedidos_df.to_csv('pizzeria/personalizadas/pizzas.csv', index=False)
    
    # Funcion que accede a unos pedidos dada una lista de id y devuelve una lista con los ingredientes
    def ingredientes_anteriores(self, lista_id):
        pedidos_df = pd.read_csv('pizzeria/personalizadas/pizzas.csv')
        if lista_id == 0:
            return []
        else:
            ingredientes = []
            for num in lista_id:
                num = int(float(num))
                # Accede a la fila del DataFrame que corresponde al numero de pedido y obtiene los ingredientes de esa fila
                ingredientes_num = pedidos_df[pedidos_df['numero'] == num]['Ingredientes'].iloc[0]
                # Separa los ingredientes por /
                ingredientes.extend(ingredientes_num.split('/'))
            return ingredientes
    
    # Muestra el pedido en la terminal
    def mostrar(self):
        print("Esta es tu pizza: ")
        pedido_dict = self.diccionario()
        for key, value in pedido_dict.items():
            print(f'{key}: {value}')
```


A continuación se adjuntarán los códigos de las nuevas clases implementadas. Tanto del patrón composite como de la clase Menu:

### Patrón Composite
```
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
```

### Clase Menu:
```
import pandas as pd
from pizzeria.menus.patron_composite import MenuComposite, MenuCompuesto, Elemento

class Menu:
    def __init__(self):
        self.simple = False

    # funcion para elegir bebida
    def elegir_bebida(self):
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
        
    def pedir_menu(self):
        # Crear menús simples
        menu_bbq = MenuComposite("Menu Simple BBQ")
        menu_bbq.agregar(Elemento("Patatas", 5))
        menu_bbq.agregar(Elemento("Pizza Barbacoa", 12))
        menu_bbq.agregar(Elemento("Helado", 4))

        menu_basico = MenuComposite("Menu Simple Básico")
        menu_basico.agregar(Elemento("Croquetas", 5))
        menu_basico.agregar(Elemento("Pizza Margarita", 10))
        menu_basico.agregar(Elemento("Sorbete", 4))

        menu_queso = MenuComposite("Menu Simple Queso")
        menu_queso.agregar(Elemento("Ensalada", 3))
        menu_queso.agregar(Elemento("Pizza 4 Quesos", 12))
        menu_queso.agregar(Elemento("Tarta de Queso", 4))

        menu_carbonara = MenuComposite("Menu Simple Carbonara")
        menu_carbonara.agregar(Elemento("Alitas de Pollo", 5))
        menu_carbonara.agregar(Elemento("Pizza Carbonara", 13))
        menu_carbonara.agregar(Elemento("Tiramisú", 4))

        # Preguntar al usuario si desea un menú simple o uno compuesto
        while True:
            print("\nTipos de Menús Simples disponibles:")
            print(f"\nMenu Simple BBQ: {menu_bbq.obtener_precio() + 1} €")
            for elemento in menu_bbq.elementos:
                    print(f"- {elemento.nombre}")
            print(f"\nMenu Simple Básico: {menu_basico.obtener_precio() + 1} €")
            for elemento in menu_basico.elementos:
                print(f"- {elemento.nombre}")
            print(f"\nMenu Simple Queso: {menu_queso.obtener_precio() + 1} €")
            for elemento in menu_queso.elementos:
                print(f"- {elemento.nombre}")
            print(f"\nMenu Simple Carbonara: {menu_carbonara.obtener_precio() + 1} €")
            for elemento in menu_carbonara.elementos:
                print(f"- {elemento.nombre}")

            print("\nTipos de Menús Compuestos disponibles:")
            print(f"\nMenu Compuesto Carnívoro: {menu_bbq.obtener_precio() + menu_carbonara.obtener_precio() + 2} €")
            print("- Menu Simple BBQ + Menu Simple Carbonara")
            print(f"\nMenu Compuesto Vegetariano: {menu_basico.obtener_precio() + menu_queso.obtener_precio() + 2} €")
            print("- Menu Simple Básico + Menu Simple Queso")

            eleccion_tipo_menu = input("\n¿Deseas un menú simple (S) o uno compuesto (C)? ").upper()
            if eleccion_tipo_menu == "S":
                self.simple = True
                # Mostrar elementos de los menús. Al precio de cada menú se le suma 1 € por la bebida que se añadirá después
                print("\nMenús simples disponibles:")
                print("1. Menu Simple BBQ")
                print("2. Menu Simple Básico")
                print("3. Menu Simple Queso")
                print("4. Menu Simple Carbonara")

                # Pedir al usuario que elija un menú simple
                while True:
                    eleccion_menu = input("\nElige un número de menú: ")
                    if eleccion_menu == "1":
                        menu = menu_bbq
                        menu.agregar(Elemento(self.elegir_bebida(), 1))
                        break
                    elif eleccion_menu == "2":
                        menu = menu_basico
                        menu.agregar(Elemento(self.elegir_bebida(), 1))
                        break
                    elif eleccion_menu == "3":
                        menu = menu_queso
                        menu.agregar(Elemento(self.elegir_bebida(), 1))
                        break
                    elif eleccion_menu == "4":
                        menu = menu_carbonara
                        menu.agregar(Elemento(self.elegir_bebida(), 1))
                        break
                    else:
                        print("Opción no válida. Intenta de nuevo.")
                break
            elif eleccion_tipo_menu == "C":
                self.simple = False
                # Mostrar opciones de menús compuestos. Al precio de cada menú se le suma 2 € por las bebidas que se añadirán después
                print("\nMenús Compuestos disponibles:")
                print("1. Menu Compuesto Carnívoro")
                print("2. Menu Compuesto Vegetariano")
                
                # Pedir al usuario que elija un menú compuesto
                while True:
                    eleccion_menu_compuesto = input("\nElige una opción (1, 2): ")
                    if eleccion_menu_compuesto == "1":
                        menu_bbq.agregar(Elemento(self.elegir_bebida(), 1))
                        menu_carbonara.agregar(Elemento(self.elegir_bebida(), 1))
                        menu = MenuCompuesto("Menu Compuesto A", menu_bbq, menu_carbonara)
                        break
                    elif eleccion_menu_compuesto == "2":
                        menu_basico.agregar(Elemento(self.elegir_bebida(), 1))
                        menu_queso.agregar(Elemento(self.elegir_bebida(), 1))
                        menu = MenuCompuesto("Menu Compuesto B", menu_basico, menu_queso)
                        break
                    else:
                        print("Opción no válida. Intenta de nuevo.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        return menu

    def numero_pedido(self):
        if self.simple:
            archivo = 'pizzeria/menus/menus_simples.csv'
        else:
            archivo = 'pizzeria/menus/menus_compuestos.csv'
        try:
            menu_df = pd.read_csv(archivo)
            if not menu_df.empty:
                ultimo_id = menu_df['Numero'].max()
                nuevo_id = ultimo_id + 1
            else:
                nuevo_id = 1
        except FileNotFoundError:
            nuevo_id = 1
        return nuevo_id

        
    def guardar_menu(self,menu):
        # obtener el numero de menu
        numero = self.numero_pedido()

        # guardar el menu en el archivo CSV
        if self.simple:
            try:
                menu_df = pd.read_csv('pizzeria/menus/menus_simples.csv')
            except FileNotFoundError:
                menu_df = pd.DataFrame(columns=['Menu', 'Entrante', 'Pizza', 'Postre', 'Bebida', 'Precio', 'Numero'])
            menu_df = pd.concat([menu_df, pd.DataFrame([{'Menu': menu.nombre, 'Entrante': menu.elementos[0].nombre, 'Pizza': menu.elementos[1].nombre, 'Postre': menu.elementos[2].nombre, 'Bebida': menu.elementos[3].nombre, 'Precio': menu.obtener_precio(), 'Numero': numero}])], ignore_index=True)
            menu_df.to_csv('pizzeria/menus/menus_simples.csv', index=False)
        else:
            try:
                menu_df = pd.read_csv('pizzeria/menus/menus_compuestos.csv')
            except FileNotFoundError:
                menu_df = pd.DataFrame(columns=['Menu', 'Menu 1', 'Bebida 1', 'Menu 2', 'Bebida 2', 'Precio', 'Numero'])
            menu_df = pd.concat([menu_df, pd.DataFrame([{'Menu': menu.nombre, 'Menu 1': menu.menu1.nombre, 'Bebida 1': menu.menu1.elementos[3].nombre, 'Menu 2': menu.menu2.nombre, 'Bebida 2': menu.menu2.elementos[3].nombre, 'Precio': menu.obtener_precio(), 'Numero': numero}])], ignore_index=True)
            menu_df.to_csv('pizzeria/menus/menus_compuestos.csv', index=False) 

    # Funcion que accede a unos menus simples dada una lista de id y devuelve una lista con los elementos
    def obtener_elementos_simples(self, lista_id):
        menu_df = pd.read_csv('pizzeria/menus/menus_simples.csv')
        if lista_id == 0:
            return []
        else:
            elementos = []
            i = 0
            for num in lista_id:
                elementos.append([])
                num =int(float(num))
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Menu'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Entrante'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Pizza'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Postre'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Bebida'].iloc[0])
                i += 1
            return elementos

    # Funcion que accede a unos menus compuestos dada una lista de id y devuelve una lista con los elementos
    def obtener_elementos_compuestos(self, lista_id):
        menu_df = pd.read_csv('pizzeria/menus/menus_compuestos.csv')
        if lista_id == 0:
            return []
        else:
            elementos = []
            i = 0
            for num in lista_id:
                elementos.append([])
                num =int(float(num))
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Menu'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Menu 1'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Bebida 1'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Menu 2'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Bebida 2'].iloc[0])
                i += 1
            return elementos
```

Ahora se adjunta el código de la clase cliente, que tiene funciones para crear el cliente y para recibir los pedidos anteriores, tanto de las pizzas personalizadas como de los menús:

### Clase Cliente
```
import pandas as pd
import numpy as np
import warnings
from pizzeria.menus.menu import Menu

# Clase Cliente
class Cliente():
    def __init__(self):
        # Inicializa las variables vacias que luego se llenaran
        self.usuario = ''
        self.contraseña = ''
        self.telefono = ''
        self.domicilio = ''
        self.pedidos = []
        # Lee el archivo CSV clientes.csv y lo guarda en una variable
        self.clientes_df = pd.read_csv('pizzeria/clientes.csv')

    # Funcion para iniciar sesion o crear un nuevo usuario
    def iniciar(self):
        # Bucle para iniciar sesion o crear un nuevo usuario
        while True:
            nuevo = input('¿Eres un cliente nuevo? (S/N): ')
            if nuevo.lower() == 's':
                # Si es un nuevo cliente, lo registra
                self.telefono = input('Teléfono: ')
                self.domicilio = input('Dirección: ')
                self.usuario = input('Usuario: ')
                self.contraseña = input('Contraseña: ')
                # Crea un DataFrame con los datos del nuevo cliente
                nuevo_cliente = pd.DataFrame({'Usuario': [self.usuario], 'Contraseña': [self.contraseña], 'Telefono': [self.telefono], 'Domicilio': [self.domicilio]})
                # Concatena el nuevo DataFrame con el DataFrame de clientes
                self.clientes_df = pd.concat([self.clientes_df, nuevo_cliente], ignore_index=True)
                # Guarda el DataFrame actualizado en el archivo CSV
                self.clientes_df.to_csv('pizzeria/clientes.csv', index=False)
                break
            elif nuevo.lower() == 'n':
                # Si no es un nuevo cliente, inicia sesion
                self.usuario = input('Usuario: ')
                self.contraseña = input('Contraseña: ')
                # Verifica si el usuario existe
                if self.usuario in self.clientes_df['Usuario'].values.tolist():
                    # Verifica si la contraseña coincide
                    index = self.clientes_df.index[self.clientes_df['Usuario'] == self.usuario].tolist()[0]
                    stored_password = self.clientes_df.at[index, 'Contraseña']
                    if self.contraseña == stored_password:
                        print('Inicio de sesión exitoso. ¡Bienvenido de nuevo!')
                        break
                    else:
                        print('La contraseña no coincide. Intenta de nuevo.')
                else:
                    print('El usuario no existe. Intenta de nuevo.')
            else:
                print('Opción no válida. Intenta de nuevo.')
    
    # Funcion que obtiene el numero de pedido de la pizza, menú simple o menú compuesto y lo guarda en el archivo CSV
    def pedido_pizzas(self, pedido, tipo):
        if tipo == 'Pizzas':
            n_pedido = pedido.numero_pedido() -1
        else:
            n_pedido = pedido.numero_pedido() -1
        n_pedido = str(n_pedido)
        user_index = self.clientes_df[self.clientes_df['Usuario'] == self.usuario].index[0]
        pedidos_anteriores = self.clientes_df.at[user_index, tipo]
        # Verifica si el cliente tiene pedidos anteriores
        if pd.notna(pedidos_anteriores):
            nuevos_pedidos = f"{pedidos_anteriores}/{n_pedido}"
        else:
            nuevos_pedidos = n_pedido

        # Suprime temporalmente las advertencias FutureWarning
        warnings.simplefilter(action='ignore', category=FutureWarning)
        # Actualiza la columna 'Pedidos' con los nuevos pedidos
        self.clientes_df.at[user_index, tipo] = nuevos_pedidos
        warnings.resetwarnings()

        # Guarda el DataFrame actualizado en el archivo CSV
        self.clientes_df.to_csv('pizzeria/clientes.csv', index=False)
    
    # Funcion que obtiene las pizzas anteriores del cliente y devuelve los ingredientes de estas
    def acceder_pizzas(self, pedido):
        # Obtiene los pedidos anteriores del cliente
        user_index = self.clientes_df[self.clientes_df['Usuario'] == self.usuario].index[0]
        pedidos_anteriores = self.clientes_df.at[user_index, 'Pizzas']
        # Verifica si el cliente tiene pedidos anteriores
        if pd.isna(pedidos_anteriores):
            numero_ped = 0
        else:
            # Verificar si hay solo un pedido
            if isinstance(pedidos_anteriores, (int, np.int64)):
                numero_ped = [pedidos_anteriores]
            else:
                # Si hay mas de un pedido, los separa
                numero_ped = str(pedidos_anteriores).split('/')
        # Llama a la funcion ingredientes_anteriores de la clase Pedido que le devuelve los ingredientes
        ingredientes = pedido.ingredientes_anteriores(numero_ped)
        return ingredientes
    
    # Funcion que obtiene los menus simples anteriores del cliente
    def acceder_menu_simple(self, menu):
        # Obtiene los pedidos anteriores del cliente
        user_index = self.clientes_df[self.clientes_df['Usuario'] == self.usuario].index[0]
        pedidos_anteriores = self.clientes_df.at[user_index, 'Menus Simples']
        # Verifica si el cliente tiene pedidos anteriores
        if pd.isna(pedidos_anteriores):
            numero_ped = 0
        else:
            # Verificar si hay solo un pedido
            if isinstance(pedidos_anteriores, (int, np.int64)):
                numero_ped = [pedidos_anteriores]
            else:
                # Si hay mas de un pedido, los separa
                numero_ped = str(pedidos_anteriores).split('/')
        # Llama a la funcion elementos que le devuelve los elementos del menu
        lista_menus = menu.obtener_elementos_simples(numero_ped)
        return lista_menus
    
    # Funcion que obtiene los menus compuestos anteriores del cliente
    def acceder_menu_compuesto(self, menu):
        # Obtiene los pedidos anteriores del cliente
        user_index = self.clientes_df[self.clientes_df['Usuario'] == self.usuario].index[0]
        pedidos_anteriores = self.clientes_df.at[user_index, 'Menus Compuestos']
        # Verifica si el cliente tiene pedidos anteriores
        if pd.isna(pedidos_anteriores):
            numero_ped = 0
        else:
            # Verificar si hay solo un pedido
            if isinstance(pedidos_anteriores, (int, np.int64)):
                numero_ped = [pedidos_anteriores]
            else:
                # Si hay mas de un pedido, los separa
                numero_ped = str(pedidos_anteriores).split('/')
        # Llama a la funcion elementos que le devuelve los elementos del menu
        lista_menus = menu.obtener_elementos_compuestos(numero_ped)
        return lista_menus
```

Por último tenemos el lanzador final de la pizzería. En primer lugar te pregunta si quieres crear una pizza y luego lo mismo con el menú. A continuación muestra el precio total del pedido, y por último te pregunta si quieres ver los menús pedidos anteriormente.

### Lanzador de la Pizzaría:
```
import pizzeria.personalizadas.patron_builder as patron_builder
import pizzeria.personalizadas.pedido_pizzas as guardar_pedido
import pizzeria.cliente as cliente
from pizzeria.menus.menu import Menu
import pandas as pd

def main_pizzeria():
    print('Bienvenido a la Pizzeria Delizioso')
    precio_pizza = 0
    precio_menu = 0

    # Crea un cliente
    mi_cliente = cliente.Cliente()
    # Llama a la funcion iniciar e inicia sesion
    mi_cliente.iniciar()

    # Pregunta si desea crear una pizza personalizada
    while True:
        pedir_pizza = input("Desea crear una pizza (S/N): ")
        if pedir_pizza.lower() == "s":
            print("Precio estandar pizza personalizada 15€")
            
            # Crea el director y el builder
            director = patron_builder.Director()
            builder = patron_builder.ConcreteBuilder()
            director.builder = builder
            
            # Construye una pizza con todos los atributos
            director.build_full_featured_product(mi_cliente, guardar_pedido.Pedido(builder))

            # Guarda el pedido y lo muestra
            pedido = guardar_pedido.Pedido(builder)
            pedido.guardar()
            pedido.mostrar()
            # Guarda el numero de pedido en el archivo CSV clientes.csv
            mi_cliente.pedido_pizzas(pedido, 'Pizzas', 0)

            # Lee el archivo CSV pedidos.csv y lo guarda en una variable
            pedidos_df = pd.read_csv('pizzeria/personalizadas/pizzas.csv')
            # Obtiene el ultimo pedido
            ultimo_pedido = pedidos_df.iloc[-1]
            # Obtiene la parte de extras del pedido
            extras = ultimo_pedido['Extras Gourmet']
            # Cuenta el numero de extras
            n_extras = len(extras.split("/"))
            
            # Calcula el precio total del pedido
            precio_pizza = 15 + n_extras * 2
            break

        elif pedir_pizza.lower() == "n":
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
    
    # Pregunta si quiere pedir un menú
    while True:
        pedir_menu = input("\nDesea pedir un menú (S/N): ")
        if pedir_menu.lower() == "s":
            menus = Menu()
            menu = menus.pedir_menu()
            precio_menu = menu.obtener_precio()
            menus.guardar_menu(menu)
            # Guarda el numero de pedido en el archivo CSV clientes.csv
            individual = menus.simple
            if individual:
                mi_cliente.pedido_pizzas(menus, 'Menus Simples')
            else:
                mi_cliente.pedido_pizzas(menus, 'Menus Compuestos')
            print(f"El precio total de su pedido es de {precio_pizza + precio_menu} €")
            break
        elif pedir_menu.lower() == "n":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    
    # ver si la variable menus existe
    try:
        menus
    except NameError:
        menus = Menu()
    # Pregunta si desea ver los elementos de los menus simples anteriores:
    elementos_simples = mi_cliente.acceder_menu_simple(menus)
    if elementos_simples != []:
        while True:
            ver_elementos = input("\nDesea ver sus menus simples anteriores (S/N): ")
            if ver_elementos.lower() == "s":
                for menu in elementos_simples:
                    for elemento in menu:
                        print(elemento)
                    print()
                break
            elif ver_elementos.lower() == "n":
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
    
    # Pregunta si desea ver los elementos de los menus compuestos anteriores:
    elementos_compuestos = mi_cliente.acceder_menu_compuesto(menus)
    if elementos_compuestos != []:
        while True:
            ver_elementos = input("\nDesea ver sus menus compuestos anteriores (S/N): ")
            if ver_elementos.lower() == "s":
                for menu in elementos_compuestos:
                    print(menu[0], ":")
                    for i in range(1, len(menu), 2):
                        print(menu[i], "con", menu[i + 1])
                    print()
                break
            elif ver_elementos.lower() == "n":
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    print("Gracias por su visita. Hasta pronto!")
```
