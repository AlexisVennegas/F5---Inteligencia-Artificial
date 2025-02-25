

## POO Ejercicio 1:

import time

# 1. Crear una clase Car que tenga los siguientes atributos:
class Car:
    def __init__(self, number: int, var_total: int, var_relative: int, var_color: str = "black", var_matricula: str = 0): # 2. Crear un constructor que reciba como parámetros los atributos mencionados en el punto anterior.
        self.wheels = number
        self.km_total = var_total
        self.km_relative = var_relative
        self.color = var_color
        self.matricula = var_matricula
# 3. Crear los métodos move(km) y reset(km) que reciban como parámetro los kilómetros a moverse y actualice los kilómetros recorridos totales y relativos.
    def move(self, km: int):
        self.km_total += 10
        self.km_relative += 10

    def reset(self, km: int):
        if not self.km_relative:
            self.km_relative = 0
    
    def print_km(self):
        print("km_total:", self.km_total)
        print("km_relative:", self.km_relative)

# 4. Crear un método print_car() que imprima las características del auto.
objec = Car(4, 100, 0)
print("wheels:", objec.wheels)
print("km_total:", objec.km_total)
print("km_relative:", objec.km_relative)


# 5. Crear un método que reciba como parámetro una lista de autos y devuelva el auto con más kilómetros recorridos.
def increase_km(obj):
    while obj.km_total <= 300:
        obj.move(10)
        obj.print_km()
        time.sleep(1)
    if obj.km_total == 300:
        obj.reset(0)
        obj.print_km()
        time.sleep(1)
    return("finish")

increase_km(objec)




## Métodos mágicos:

import time
# definimos la clase Car con sus atributos y métodos correspondientes 
class Car:
    def __init__(self, number: int, var_total: int, var_relative: int, var_color: str = "black", var_matricula: str = 0) -> None: # definimos los atributos de la clase
        self.wheels = number                     # número de ruedas
        self.km_total = var_total                # kilometraje total
        self.km_relative = var_relative          # kilometraje relativo
        self.color = var_color                   # color del auto
        self.matricula = var_matricula           # matrícula del auto


# definimos los métodos de la clase Car 
    def print_todo(self):
        print("wheels:", self.wheels)
        print("km_total:", self.km_total)
        print("km_relative:", self.km_relative)
        print("color:", self.color)
        print("matricula:", self.matricula)

# llama a la clase Car y le asigna los valores a los atributos
objec2 = Car(4, 100, "black", 0)
objec2.print_todo()



## Encapsulación



import hashlib
# Crear una clase Login que tenga los siguientes atributos:
class Login:
    def __init__(self, var_name: str, var_password: str, var_email: str) -> None: # Crear un constructor que reciba como parámetros los atributos mencionados en el punto anterior.
        self.name = var_name
        self.__password = hashlib.sha256(var_password.encode()).hexdigest()
        self.email = var_email


# Crear los métodos get_password() y set_password() que permitan obtener y cambiar la contraseña del usuario, respectivamente.
    def get_password(self):
        return self.__password

    def set_password(self, var_password: str):
        self.__password = hashlib.sha256(var_password.encode()).hexdigest()


# Crear un método print_login() que imprima las características del usuario.
    def print_login(self):
        print("name:", self.name)
        print("password:", self.__password)
        print("email:", self.email)

# Solicitar los datos de entrada al usuario
input_name = input("Ingrese su nombre: ")

# Comprobar la contraseña
while True:
    input_password = input("Ingrese su contraseña (mínimo 6 caracteres, sin 'ñ'): ")
    if len(input_password) >= 6 and 'ñ' not in input_password:
        break
    print("Contraseña inválida. Asegúrese de que tenga al menos 6 caracteres y no contenga una 'ñ'.")

# Comprobar el correo electrónico
while True:
    input_email = input("Ingrese su correo electrónico: ")
    if '@' in input_email:
        break
    print("Correo electrónico inválido. Asegúrese de que contenga un '@'.")

# Crear objeto Login con los datos ingresados
object1 = Login(input_name, input_password, input_email)

# Imprimir contraseña inicial
print("Contraseña inicial:")
print(object1.get_password())
print("")

# Preguntar si desea cambiar la contraseña
change_password = input("¿Desea cambiar la contraseña? (Sí/No): ")

if change_password.lower() == "si":
    # Comprobar la nueva contraseña
    while True:
        new_password = input("Ingrese la nueva contraseña (mínimo 6 caracteres, sin 'ñ'): ")
        if len(new_password) >= 6 and 'ñ' not in new_password:
            object1.set_password(new_password)
            print("Contraseña cambiada exitosamente.")
            print("")
            break
        print("Contraseña inválida. Asegúrese de que tenga al menos 6 caracteres y no contenga una 'ñ'.")

# Imprimir contraseña actualizada
print("Contraseña actualizada:")
print(object1.get_password())
print("")

# Imprimir todos los atributos de la clase Login
print("Detalles del objeto Login:")
object1.print_login()



## Herencia


# Crear una clase Vehiculos que tenga los siguientes atributos:
class Vehiculos:
    def __init__(self, nombre, marca, modelo):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

# Crear los métodos arrancar(), acelerar() y frenar() que cambien los atributos correspondientes.
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
    
    def estado(self):
        print("Nombre: ", self.nombre, "\nMarca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

        

# Crear una clase Moto que herede de Vehiculos.
class Moto(Vehiculos):
    # pass signfica que no hace nada pero es necesario para que no de error
    pass

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada."
        else:
            return "La furgoneta no está cargada."
# Crear un objeto de la clase Moto.
obj1 = Moto("FZ", "Yamaha", "2019")

obt2 = Furgoneta("FZ", "Yamaha", "2019")

# Llamar a los métodos de la clase Moto.
obj1.estado()
obt2.estado()


## POO Ejercicio 4:

class Pokemon:
    def __init__(self, name, type_, attacks):
        self.name = name
        self.heal = 100
        self.type = type_
        self.attacks = ["arañazo", attacks, "atack3", "atack4"]

    def print_pokemon_info(self):
        print("Name:", self.name)
        print("Heal:", self.heal)
        print("Type:", self.type)
        print("Attacks:", self.attacks)


class TypeWater(Pokemon):
    def __init__(self, name, attacks):
        super().__init__(name, "Agua", attacks)
        self.weakness = "electric"
        self.strength = "fire"

    def print_pokemon_info(self):
        super().print_pokemon_info()
        print("Weakness:", self.weakness)
        print("Strength:", self.strength)


class TypeFire(Pokemon):
    def __init__(self, name, attacks):
        super().__init__(name, "Fuego", attacks)
        self.weakness = "water"
        self.strength = "grass"

    def print_pokemon_info(self):
        super().print_pokemon_info()
        print("Weakness:", self.weakness)
        print("Strength:", self.strength)


class TypePlant(Pokemon):
    def __init__(self, name, attacks):
        super().__init__(name, "Planta", attacks)
        self.weakness = "fire"
        self.strength = "water"

    def print_pokemon_info(self):
        super().print_pokemon_info()
        print("Weakness:", self.weakness)
        print("Strength:", self.strength)


# Crear instancias de las clases
obj1 = Pokemon("Pikachu", "Electrico", "Impactrueno")
obj2 = TypeWater("Squirtle", "Burbuja")
obj3 = TypeFire("Charmander", "Ascuas")
obj4 = TypePlant("Bulbasaur", "Látigo cepa")

# Llamar al método print_pokemon_info para imprimir la información de cada Pokémon
obj1.print_pokemon_info()
print("")
obj2.print_pokemon_info()
print("")
obj3.print_pokemon_info()
print("")
obj4.print_pokemon_info()


## Polimorfismo

class Tarea:
    def hacer_algo(self):
        print("primera funcion")

class Tarea2:
    def hacer_algo(self):
        print("segunda funcion")
    

def hacer_algo3(tarea):
    tarea.hacer_algo()

var_hacer_algo = Tarea2() # Tarea() o Tarea2() para cambiar la funcion que se ejecuta

hacer_algo3(var_hacer_algo)

## POO Ejercicio 5:

# Crear clases Vaca, Perro, Gato y Cerdo que implementen el método cantar() y hacer_cantar().
class Vaca:
    def cantar(self):
        print("Muuu")
    
class Perro:
    def cantar(self):
        print("Guau")
    
class Gato:
    def cantar(self):
        print("Miau")

class Cerdo:
    def cantar(self):
        print("Oink")

# Crear una función hacer_cantar() que reciba como parámetro un objeto y llame al método cantar() del mismo.

def hacer_cantar(animal):
    animal.cantar()

var_hacer_cantar = Perro() # Vaca(), Perro(), Gato() o Cerdo() para cambiar el animal que canta

hacer_cantar(var_hacer_cantar)
        