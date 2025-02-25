<h1 align="center">
    El proposito de este ejercicio es debbugear con el debuggerPython las funciones paso a paso para poder encontrar el error y a su vez una solución.
</h1>

1.- divide_numbers

    R.- Con el debugger atravez de la función y siguiendo paso a paso cada linea
    nos damos cuenta que cuando b == 0, y se intenta divir result = a / b, salta 
    un error debido al ZeroDivisionError, que se controla con el try/except y con
    un if preguntado si b == 0 para generar un raise

2.- get_element_by_index

    R.- Aqui el error esta en que a la funcion get_element_by_index se le pasa una lista a iterar my_list = [1, 2, 3] y un index = 5, con los print nos damos cuenta del valor de cada uno de ellos, nos damos cuenta que el index > my_list, y por lo tanto no es iterable, lo controlamos con un if preguntado si index >= len(my_list)
    asi controlamos que no supere el tamaño del my_list, y lo mismo creando un raise generamos un error con el try/except

3.- concatenate_strings

    R.- concatenate_strings recibe dos variables str1, str2, a la funcion le pasamos "hola" y 123, y al intentar concatenarlos result = str1 + str2, da un error por unir una variable de tipo str con una de tipo int, lo que haecmos es preguntar 
    si el type != int, se convierte a str: str1 = str(str1), de igual forma con un try/except se controla cualquier otro error. 

4.- print_numbers

    R.- De igual manera en esta función le llega una variable llamada n, le pasan "5"
    y se intenta iterar en un for i in range(n), error esta en que iteramos en un str
    de igual forma que arriba se convierte a str, preguntando por su type, y controlamos cualquier error con un try/except.

5.- calculate

    R.- En calculate le pasan 2 y "5", los almacena en operand1 y operand2, y al intentar generar la operacion = "+" da error por sumar int + str, lo que tenemos que hacer es convertir a int operant(1)(2) = int(operand(1)(2)) asi cualquier operacion de ints no tendra problema

6.- En resumen

    R.- El depurador de Python es una herramienta muy útil para detectar y solucionar errores en tus programas. Python ofrece varios depuradores, siendo uno de los más populares el llamado "pdb" (Python Debugger).

    El depurador de Python te permite ejecutar tu programa paso a paso, deteniéndote en puntos específicos para examinar el estado de las variables, verificar el flujo de ejecución y encontrar posibles 