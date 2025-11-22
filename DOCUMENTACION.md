**Introducción**

Este proyecto tiene como objetivo desarrollar un algoritmo que busca los números primos en un rango de 1 a 100000, y posteriormente optimizarlo.

En el codigo original se estaba utilizando un algoritmo que va iterando numero por numero, dividiendo cada numero por los numeros anteriores desde 2
hasta n-1.

Este metodo si bien es algo sencillo de desarrollar, se vuelve complejo al aumentar el rango de busqueda, ya que el tiempo de ejecucion crecera a medida
que el rango lo haga, lo cual se puede volver inviable en rangos extremadamente grandes.

**Optimización**

Para realizar una optimizacion y mejorar los tiempos de busqueda se aplicaron las siguientes optimizaciones:

**-Iterar solo hasta la raíz cuadrada de n:**  esto quiere decir que si  un numero no es divisible por ningun valor hasta su raiz, significa que no tendra 
divisores mayores, permitiendo reducir las interaciones por numero.

**-List comprehensions:** esto es remplazar los bucles for que iteran uno a uno los numeros, por list comprehensions esto significa que python optimiza internamente
la creacion de listas, reduciendo la sobrecarga al llamar al metodo en cada iteración.

**-Numpy:** lo que se hizo fue vectorizar la busqueda eliminando los bubles, esto permite gestionar la memoria de mejor manera usando arrays de booleanos.

**Resultados**

 **Tiempo de ejecucion en consola del algoritmo original**
 
<img width="883" height="136" alt="tiempo de la version original" src="https://github.com/user-attachments/assets/a900b6d6-45c0-4aa4-a380-81b48c529e6f" />

**Tiempo de ejecucion en consola de los algoritmos optimizados**

<img width="332" height="192" alt="tiempos en consola" src="https://github.com/user-attachments/assets/53fa5831-e447-4b8c-9a2e-884a08f46b1d" />

**Grafico comparativo generado con Matplotlib**

<img width="1000" height="600" alt="comparacion de tiempos" src="https://github.com/user-attachments/assets/d605f0bb-0e31-4e93-afbd-26b40d2fe9a7" />

**Análisis de cProfile**

**-Código original:** tiene 132329 llamadas a funciones en 31,583 pero debemos tener en cuenta que en cada llamada de funcion el bucle for realiza muchas iteraciones y operaciones,
esto es lo que consume el tiempo del cpu en la busqueda.

**-Optimización con list comprehensions:** tiene 100081 llamadas a funciones, pero el tiempo se reduce significativamente ya que se reduce la iteraciones y operaciones en cada una de
las llamadas.

**-Numpy:** tiene solo 10 llamadas a funciones, ya que no realiza una llamada a funcion en cada verificacion, esto se debe a la vectorizacion , eliminando la sobrecarga del interprete.

**Conclusiones**

Podemos decir que si bien es cierto python es un lenguaje versatil que nos permite realizar muchos tipos de proyectos, es importante implementar tecnicas, librerias, etc, que nos permitan
sacar el maximo provecho a nuestras herramientas tecnologicas y obtener mejores resultados.

Otra conclusion es que herramientas como cProfile nos permiten entender como funcionan internamente los algoritmos, si bien es cierto fueron algoritmos parecidos en el numeros de lineas
de codigo, el funcionamiento interno y la logica de cada uno marcan la diferencia que se ve reflejada en el tiempo de ejecucion de cada uno.


**Link del repositorio:** https://github.com/JoseG9706/autonomo4.git
