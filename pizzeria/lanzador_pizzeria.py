import pizzeria.patron_builder as patron_builder
import pizzeria.pedido as guardar_pedido
import pizzeria.cliente as cliente
import pizzeria.menu as menus
import pandas as pd

def main_pizzeria():
    print('Bienvenido a la Pizzeria Delizioso')
    precio_pizza = 0
    precio_menu = 0
    # Pregunta si desea crear una pizza personalizada
    while True:
        pedir_pizza = input("Desea crear una pizza (S/N): ")
        if pedir_pizza.lower() == "s":
            print("Precio estandar pizza personalizada 15€")
            # Crea un cliente
            mi_cliente = cliente.Cliente()
            # Llama a la funcion iniciar e inicia sesion
            mi_cliente.iniciar()

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
            mi_cliente.pedido_cliente(pedido)

            # Lee el archivo CSV pedidos.csv y lo guarda en una variable
            pedidos_df = pd.read_csv('pizzeria/pedidos.csv')
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
            menu = menus.pedir_menu()
            precio_menu = menu.obtener_precio()
            break
        elif pedir_menu.lower() == "n":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    print(f"El precio total de su pedido es de {precio_pizza + precio_menu} €")
    print("Gracias por su visita. Hasta pronto!")