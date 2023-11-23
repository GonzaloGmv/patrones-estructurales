from pizzeria.menus.patron_composite import MenuComposite, MenuCompuesto, Elemento

# funcion para elegir bebida
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
    
def pedir_menu():
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
                    menu.agregar(Elemento(elegir_bebida(), 1))
                    break
                elif eleccion_menu == "2":
                    menu = menu_basico
                    menu.agregar(Elemento(elegir_bebida(), 1))
                    break
                elif eleccion_menu == "3":
                    menu = menu_queso
                    menu.agregar(Elemento(elegir_bebida(), 1))
                    break
                elif eleccion_menu == "4":
                    menu = menu_carbonara
                    menu.agregar(Elemento(elegir_bebida(), 1))
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
            break
        elif eleccion_tipo_menu == "C":
            # Mostrar opciones de menús compuestos. Al precio de cada menú se le suma 2 € por las bebidas que se añadirán después
            print("\nMenús Compuestos disponibles:")
            print("1. Menu Compuesto Carnívoro")
            print("2. Menu Compuesto Vegetariano")
            
            # Pedir al usuario que elija un menú compuesto
            while True:
                eleccion_menu_compuesto = input("\nElige una opción (1, 2): ")
                if eleccion_menu_compuesto == "1":
                    menu_bbq.agregar(Elemento(elegir_bebida(), 1))
                    menu_carbonara.agregar(Elemento(elegir_bebida(), 1))
                    menu = MenuCompuesto("Menu Compuesto A", menu_bbq, menu_carbonara)
                    break
                elif eleccion_menu_compuesto == "2":
                    menu_basico.agregar(Elemento(elegir_bebida(), 1))
                    menu_queso.agregar(Elemento(elegir_bebida(), 1))
                    menu = MenuCompuesto("Menu Compuesto B", menu_basico, menu_queso)
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    return menu

def precio(menu):
    return menu.obtener_precio()