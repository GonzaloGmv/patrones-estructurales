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


# Ejercicio 2. Samur

En primer lugar tenemos el patrón composite que modela la estructura de documentos. Además las hojas tienen unas funciones para mostrar la informacion y la clase carpeta tiene unas funciones para mostrar el contenido, añadir documentos o eliminarlos y para acceder a ellos. 

Para crear la carpeta con los archivos hay una clase CrearCarpetas que lee un csv donde están los archivos y los crea usando el composite. 

Por último, por medio del proxy se comprueba si el usuario está autorizado o no y se le da permiso a acceder a las carpetas.

## Pruebas unitarias del Samur

Para empezar pregunta a qué carpeta se desea acceder, y si el usuario no da un número o da un número que no sea el de ninguna carpeta, no le da acceso:

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/f35d7017-d5c4-4a39-9a72-b5d0b26b14dd)

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/7912dff8-d1b4-40ea-8628-65031aa8b0af)

Después de esto le pide el usuario y la contraseña y se comprueba si ese usuario está en el csv, en caso de que no esté significa que no está autorizado. En caso de que ese usuario esté en el csv luego se comprueba si la contraseña coincide.

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/44d0e4ba-d51d-4ae4-970f-73182f9c41ea)

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/a3de17b4-04a3-41e1-8715-a7e7e342219c)

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/276d702a-aacd-4df5-b577-e84b2c88ca42)

Una vez se haya iniciado sesión correctamente y el usuario sea autorizado se le pregunta que desea hacer. En caso de que el usuario escriba algo que no se le pide se le vuelve a preguntar.

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/ee954ada-7e7e-467a-9841-01c8c867ebb1)

Una vez el usuario escoja una acción que hacer, se realizará esta acción y se le preguntará otra vez por si desea hacer algo más.

1. Acceder a un documento de la carpeta: Se le pregunta el nombre del archivo al que desea acceder. Si el documento no existe se le devolverá un mensaje diciéndoselo. Si el documento sí que existe se le devolverá la información de este documento. 

    ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/3bdfb4ce-d6cb-4c43-8528-55094d5828fe)

    ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/99999958-746a-42ba-ab1a-41eea64459c6)

    Si ese documento es un link,, se le devolverá la información de ese link y del archivo vinculado.
   
   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/c965ce3f-6236-40bd-aa6e-b9bb1dd0c3f0)

2. Mostrar información de la carpeta: Devuelve el nombre de la carpeta y el tamaño de esta.

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/7f90b5bc-e392-4f13-9d30-254877da1c3d)

3. Mostrar contenido de la carpeta: Muestra los archivos que hay dentro de esta carpeta.

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/4646bcd4-576e-4963-971a-3e21a654bce9)

4. Agregar un documento a la carpeta: Pide si quiere añadir un enlace o un documento. En caso de añadir un documento se le pedirá el nombre, el tipo y el tamaño, pero el tamaño sebe ser un número.

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/605f808a-d2de-422f-a974-8d17967d85d5)

   En caso de añadir un enlace se le pedirá el nombre de este y el nombre del archivo vinculado. En caso de que el archivo vinculado no exista, no se creará el enlace.

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/82f46806-038d-41d0-9cec-d5e95689d928)

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/751232ea-aecf-4385-b0a4-e73488599dc5)

   Ahora si mostramos el contenido de esta carpeta podemos ver como han sido creados con éxito y como el Link de Prueba enlazado a un documento inexistente no ha sido creado.

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/e77477e2-a4e3-4654-9fa2-7d4bb076dd37)

   También podemos acceder al enlace para ver que ha sido creado correctamente

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/474a0db3-9ded-4777-b6c4-037dc2c8a459)


5. Eliminar un documento de la carpeta. Pregunta el nombre del documento que se desea eliminar. Si este documento no existe mostrará un mensaje y no hará nada.

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/94e7fc31-d17b-4399-b039-c241ad4ee99d)

   En caso de que el documento exista e eliminará.

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/5513da2a-8cb4-4072-b532-b210bb565a10)

   Podemos mostrar el contenido de la carpeta y veremos como no existe ya el documento eliminado.

   ![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/514a06ac-1a72-4e1f-aff7-cbe06566ae71)

6. Salir. Sale del programa.

Una vez hemos salido, si ejecutamos otra vez el programa y mostramos el contenido de la carpeta modificada podemos ver como los cambios se han guardado correctamente aún habiendo cerrado el programa.

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/78e54577-eebf-4270-9609-3522964dff6e)

Si vemos, el csv de archivos se ha actualizado.

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/ba81c145-0460-4d28-8bf6-162e81e2283f)

Y en el csv con los registros se han registrado las operaciones realizadas, incluida la hora.

![image](https://github.com/GonzaloGmv/patrones-estructurales/assets/91721237/7cfee002-ad53-4b9c-affd-dff94b62bf2b)






