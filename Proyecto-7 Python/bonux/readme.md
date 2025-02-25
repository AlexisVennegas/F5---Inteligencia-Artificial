<p align="center">
  <img src="https://openexpoeurope.com/wp-content/uploads/2023/05/logo-factoria-f5.png" alt="FactoriaF5"/>
</p>


<h1 aligh="center">Explicacion de los ejercicios</h1>

1.- Args

    R.-  *args permite pasar un número variable de argumentos posicionales a una función. 
         El * indica que se recibirá un número variable de argumentos posicionales y se almacenarán en una tupla.

    ```

    def mi_funcion(*args):
        for arg in args: # args son todos los argumentos que se le introducen a la funcion
            print(arg)   # se imprimen los argumentos de uno en uno

    mi_funcion(1, 2, 3)


    ## **kwargs permite pasar un número variable de argumentos con nombre a una función.
    ## el ** indica que se recibirá un número variable de argumentos con nombre y se almacenarán en un diccionario.

    def mi_funcion(**kwargs):
        for kwarg in kwargs:
            print(kwarg, "=>", kwargs[kwarg])

    mi_funcion(nombre="Alexis", apellido="Venegas")

    ```

2.- Ejercicio 1: Funciones más avanzadas


        R.- - la funcion submit() recoje los datos atravez de los inputs, se checkan si son datos correctos
            - Si son correctos los datos pasan a greetings(con los parametros de name, age, y year)
            
            - Los datos de primera pasan a errorMan() una funcion que devuelve un numero dependiendo el error para despues procesarlo

            - A su vez errorman() envia a errorHandler() esta funcion dependiendo el valor que le llegue la evalua y checa los errores, devuelve un numero dependiendo el error

            - Si pasa este errorMan() se comprueba que el año ingresado sea el año actual con la funcion datetime.now(), si no se cambia al actual

            - Despues se cambia el formato del nombre a un formato correcto para imprimirlo 

            - Al final se retorna el saludo concatenando las variables

            - se terminan imprimiendo en la ventana creada 

        ```
        from datetime import datetime
        import tkinter as tk

        class Errores(Exception):
            pass

        def ft_isDigit(value: str) -> int:

            """funcion que verifica si el valor es un numero"""""

            i = 0
            while i < len(value):
                if value[i] >= "0" and value[i] <= "9":
                    return 1
                i += 1
            return 0

        def errorHandler(value, error) -> int:
            
            """contol de errores para cada campo"""""

            try:
                if type(value) == str:
                    if(ft_isDigit(value) == 1):
                        return 1
                if type(value) == str and error == False:
                    return 1 if value is None or value == "" or len(value) <= 0 or type(value) != str or len(value) > 20 or value.isdigit() else 0 
                elif type(value) == int:
                    if(error == True):
                        return 2 if value is None or value == 0 or type(value) != int or value < 0 or value > 100 else 0
                    else:
                        return 3 if value is None or value == 0 or type(value) != int or value < 0 else 0
                else:
                    return 1
            except Exception as e:
                return 1
                
        def errorMan(value, error) -> int:

            """creacion de errores personalizados"""""
            try:
                error_code = errorHandler(value, error)
                if error_code == 1:
                    raise Errores("Error: el campo nombre es incorrecto")
                elif error_code == 2:
                    raise Errores("Error: el campo edad es incorrecto")
                elif error_code == 3:
                    raise Errores("Error: el campo año es incorrecto")
                else:
                    return ""  # Cambiar el valor de retorno a None cuando no hay error
            except Errores as e:
                return e

        def greetings(name: str = "desconocido", age: int = None, year: int = None) -> str:


            """Función que devuelve un saludo personalizado."""
            try:
                result_name = errorMan(name, False)
                result_age = errorMan(age, True)
                result_year = errorMan(year, False)
                if  result_name != "" or result_age != "" or result_year != "" :
                    return f"{result_name}  \n  {result_age} \n {result_year}"
                else:
                    if year != datetime.now().year:
                        year = datetime.now().year
                    name = name.lower() # primero se convierte a minúsculas
                    name = name.strip('"')
                    name = name.capitalize() # 
                    return f"Hola {name}, tienes {age} años y naciste en {year - age}"
            except Exception as e:
                return f"entre aqui: {e}"

        def submit():

            """Función que se ejecuta cuando se presiona el botón Enviar."""
            name = name_entry.get()
            age = age_entry.get()
            year = year_entry.get()

            try:
                age = int(age)
                year = int(year)
                result = greetings(name, age, year) # Llamar a la función greetings con los datos ingresados por el usuario
                result_label.config(text=result) # Mostrar el resultado de la función en la etiqueta result_label
            except ValueError:
                result_label.config(text="Error: los datos no son correctos") # Mostrar un mensaje de error en la etiqueta result_label

        # Crear la ventana
        window = tk.Tk()
        window.title("Programa de Saludos")
        window.geometry("1080x600")

        # imagen 
        imagen = tk.PhotoImage(file="../bonux/factoria-web.png")
        fondo = tk.Label(window, image=imagen)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)


        # Etiqueta y campo de entrada para el nombre
        name_label = tk.Label(window, text="Nombre:")
        name_label.pack()
        name_entry = tk.Entry(window)
        name_entry.pack()


        # Etiqueta y campo de entrada para la edad
        age_label = tk.Label(window, text="Edad:")
        age_label.pack()
        age_entry = tk.Entry(window)
        age_entry.pack()

        # Etiqueta y campo de entrada para el año actual
        year_label = tk.Label(window, text="Año Actual:")
        year_label.pack()
        year_entry = tk.Entry(window)
        year_entry.pack()

        # Botón de enviar
        submit_button = tk.Button(window, text="Enviar", command=submit)
        submit_button.pack() #

        # Etiqueta para mostrar el resultado
        result_label = tk.Label(window, text="")
        result_label.pack()


        # Ejecutar el bucle principal de la ventana
        window.mainloop()

        ``` 

3.- ## Ejercicio 2: Control de excepciones

        R.- - Submit() recoje los numeros a partir de los inputs creados por la ventana y se envian a calculate()

            - En calculate() se pasan los parametros a checkNum() para comprobar que no llevan palabras
              con una expresión regular esto para controlar errores
            
            - Si todo esta okey, se genera un resultado apartir de num1 / num2, con el try/except se controla el caso del 0 / 0 mandando un error personalizado


        ```

        import tkinter as tk
        import re

        class Errores(Exception):
            pass

        def calculate(num1, num2) -> float:
            if num2 == 0:
                return "Error: no se puede dividir entre cero"
            result = num1 / num2
            return result


        import re

        def checkNum(value: str) -> bool:
            return bool(re.search(r'[a-zA-Z]', value))


        def submit():
            """Función que se ejecuta cuando se presiona el botón Enviar."""
            try:
                num1 = float(num1_entry.get())
                num2 = float(num2_entry.get())
                result = calculate(num1, num2)
                result_label.config(text=result)
            except ValueError:
                result_label.config(text="Error: los datos no son correctos")   
        # Crear la ventana
        window = tk.Tk()
        window.title("Programa de División")
        window.geometry("1080x700")

        imagen = tk.PhotoImage(file="../bonux/Why-learn-Python-4-.png")
        fondo = tk.Label(window, image=imagen)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)



        # Etiqueta y campo de entrada para el primer número
        num1_label = tk.Label(window, text="Primer número:")
        num1_label.pack()
        num1_entry = tk.Entry(window)
        num1_entry.pack()

        # Etiqueta y campo de entrada para el segundo número
        num2_label = tk.Label(window, text="Segundo número:")
        num2_label.pack()
        num2_entry = tk.Entry(window)
        num2_entry.pack()

        # Botón de enviar
        submit_button = tk.Button(window, text="Enviar", command=submit)
        submit_button.pack()

        # Etiqueta para mostrar el resultado

        result_label = tk.Label(window, text="")
        result_label.pack()

        # Ejecutar el bucle principal de la ventana
        window.mainloop()


        ```

4.- Ejercicio 3: List Comprehension


    R.- - Igualamos la variable a un [] y dentro la logica con el resultado del bucle
    
        - numeros_cuadrados_new = [dentro se genera una nueva lista]

        - dentro creamos una variable "i" se eleva al cuadraddo "**2" y se itera cada resutaldo
        
        - por cada "i**2" in numeros(la lista original) si ese resultado es menor a 50 que se agrege a   lista y se siga iterando


```

numeros = [1,2,3,4,5,6,7,8,9]
numeros_cuadrados_menoresque50 = []

def listComprehension() -> list:
    for i in numeros:
        if i**2 < 50:
            numeros_cuadrados_menoresque50.append(i**2)
    return numeros_cuadrados_menoresque50

##a una sola linea devolviendo una nueva lista 
numeros_cuadrados_new = [i**2 for i in numeros if i**2 < 50]

print(listComprehension())

numeros_cuadrados_new


```


5.- Funciones Lambda

    R.- - Submit() recoje los datos apartir de los inputs los almacena tanto en num1 y num2 a su vez lo pasan a la funcion testing()

        - Decidi tratarlo como str para poder  comprobar mas errores y al final convertirlos a tipo float para manejar todos los numeros asi que despues de testing pasan a checkNum() que comprueba si noe esta vacio, si el type es str, si no tiene un valor == None, etc

        - Si todo va bien se transformar a a tipo float y con una funcion lambda se hace el calculo de los dos numeros sum = lambda (aqui se toman los argumentos: a y b) : (la suma osea: a + b )

        - finaliza returnando el resultado de la funcion de la suma de los dos numeros

```

import tkinter as tk
import re

class Errores(Exception):
    pass


def checkNum(value: str, numCheck: int) -> int:
    if not isinstance(value, str) or not (re.search(r'[0-9]', value)) or value == "" or value is None or (re.search(r'[a-zA-Z]', value)):
        if(numCheck == 1):
            raise Errores("Error: el primer número no es correcto")
        else:
            raise Errores("Error: el segundo número no es correcto")
    else:
        return 0
    
def testing(a: str = "", b: str = "") -> int:

    """Función que devuelve un saludo personalizado."""
    try:
        result_num1 = checkNum(a, 1)
        result_num2 = checkNum(b, 2)
        if result_num1 != 0 or result_num2 != 0:
            return result_num1 or result_num2
        else:
            a = float(a)
            b = float(b)
            sum = lambda a, b : a + b
            return sum(a,b)
    except Exception as e:
        return e
    
def submit():

    """Función que se ejecuta cuando se presiona el botón Enviar."""
    num1 = str(num1_entry.get())
    num2 = str(num2_entry.get())
    try:
        result = testing(num1, num2)
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Error: los datos no son correctos")   

```

6.- Ejercicio 5: Generadores

    R.- ## como primera salida empezamos por check haciendo un for que recorra el generador
        ## num va tomar el primer valor de generador que es 1 y lo imprime
        ## en la funcion generador empezamos por el for que va a recorrer el rango de 1 a 20
        ## y va a ir devolviendo cada numero que se encuentre en el rango
        ## despues entramos en yield que va a devolver el valor de num
        ## check() recibe el valor de num y lo imprime
        ## despues yield vuelve a llamar a for con el siguiente numero del rango
        ## y asi sucesivamente hasta que se acabe el rango



```
def generador(limit: int )-> int:
    for num in range(1, limit + 1):
        yield num

def check():
   for num in generador(20):
         print(num)
```