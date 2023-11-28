# patrones-estructurales

El link a este repositorio es: [github](https://github.com/GonzaloGmv/patrones-estructurales)

# Ejercicio 1. Pizzería

Lo nuevo de este ejercicio está implementado casi todo en la carpeta menus.

En primer lugar está el patrón composite, que consta de una clase abstracta componente y una clase hojas y clases compuestas que heredan de la clase componente. Este patrón de diseño está implementado para crear los menús, que se crean en la función pedir_menu() de la clase Menu. En esta función, en primer lugar se crea cada objeto menú y se le van añadiendo los elementos con la función agregar(). A continuación el usuario elige el menú y se le añade la/s bebida/s a dicho menú. Además gracias a este patrón podemos calcular el precio de cada menú sumando el precio de cada componente.

En la clase Menu también estan otras 2 funciones encargadas de guardar el número del menú pedido por el cliente. Además hay dos funciones que se encargan de devolver los menús pedidos anteriores pedidos por el cliente.

En la clase cliente están las funciones encargadas de enviar la lista de números de pedidos anteriores a las funciones que devuelven la lista con los elementos de estos pedidos.

Por último tenemos el lanzador final de la pizzería. En primer lugar te pregunta si quieres crear una pizza y luego lo mismo con el menú. A continuación muestra el precio total del pedido, y por último te pregunta si quieres ver los menús pedidos anteriormente.


## Pruebas unitarias de la Pizzería:

A la hora de registrar un usuario podemos ver como si el usuario y la contraseña no existen o no coinciden no te deja entrar:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/0d379df2-6f0d-4a0b-a2e3-2de0f817570c)

Además podemos crear un usuario nuevo en caso de que este nunca se haya registrado:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/24bdc82e-e804-41dc-99bf-300f4cbccf3a)

A continuación te preguntará si desea pedir una pizza, y al igual que en todos los inputs de esta práctica, si el usuario no escribe una de las opciones sugeridas se lo preguntará de nuevo:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/a633a499-23d8-4b71-962f-1220120a90c8)

Si escribes s o S empezará, mediante el builder, a preguntarte por la masa, salsa, ingredientes, cocción, presentación, bordes y extras gourmet. Tanto en ingredientes como
en los extras gourmet te dejara pedir uno o más siempre y cuando lo separes por comas:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/3f4f91c2-6835-40f3-bb10-c1705970e128)

Una cosa a destacar es que si el usuario ya ha hecho más de un pedido, el programa accede a sus pedidos anteriores, y a la hora de elegir los ingredientes, se le sugieren los 5 ingredientes más pedidos por el:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/1cdc34fa-fa2e-4d2a-b477-333d19e17cc4)

Por último te devuelve tu pizza y la añade al csv:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/6e7d1c4a-24b6-40b9-9267-e3efc2fb28a0)

Al igual que antes, a continuación te pregunta si deseas pedir un menú y si le devuelves s o S te imprime los menús que hay y te pregunta si deseas el menú simple o compuesto:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/e9e98684-cec0-4ca1-b298-3d8ab357e974)

Si le devuelves una s o S te dará a elegir un menú simple y una bebida y por ultimo te devolverá el precio total del pedido, sumando el precio de la pizza y del menú si es que se han pedido los dos, o solo el precio de la pizza o del menú en caso de que sea solo uno de esos. En este caso se ha pedido menú simple y pizza personalizada.

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/f2a4d0d9-123d-449d-8034-a8a9e7e40a94)

Si lo que le devuelve el usuario es una c o C te preguntará por el menú compuesto que deseas pedir y luego preguntará por las bebidas que se añadirán a cada menú. Luego devuelve el precio total del pedido. En este caso sólo se ha pedido un menú compuesto.

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/25bf4fc7-36ba-4e29-9e0c-12154f786117)

Por último, si el cliente había pedido algún menú simple anteriormente le pregunta si desea ver los menús simples pedidos anteriormente y luego lo mismo con los menús compuestos.

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/8a52aa98-4d66-4c4a-86d1-3dd611c02aa2)

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/0cb8816f-bcfb-4183-9ed8-8c7c9cc08bde)

En el siguiente ejemplo podemos ver como el cliente sólo había pedido anteriormente un menú simple y ninguno compuesto, por lo que sólo se le pregunta si desea ver los menús simples anteriores:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/269eee91-2773-431a-a3d2-c4124ddfd970)


