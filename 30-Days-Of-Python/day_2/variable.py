# Day 2: 20 Days of python programming
#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md

##Exercise: Level 1
First_name = "Joel"
Last_name = "Villacis"
full_name = "Joel Villacis"
country = "Ecuador"
city = "Quito"
age = 26
year = 2023
is_married = False
is_true = False
is_light_on = True
dog_name, dog_name2 = "Ghost", "Luce"


"""
#Exercise: Level 2 
print("El tipo de variable de Firt_name es: ", type(First_name))
print("El tipo de variable de Last_name es: ", type(Last_name))
print("El tipo de variable de full_name es: ", type(full_name))
print("El tipo de variable de country es: ", type(country))
print("El tipo de variable de city es: ", type(city))
print("El tipo de variable de age es: ", type(age))
print("El tipo de variable de year es: ", type(year))
print("El tipo de variable de is_married es: ", type(is_married))
print("El tipo de variable de is_married es: ", type(is_true))
"""
"""
def mostrar_tipo_variable(*args):
    for variable in args:
        print(f"Variable '{variable}' es de tipo: {type(variable).__name__}")

mostrar_tipo_variable(city, First_name, age)
"""
"""
#len() no admite int, por lo que se hace la siguiente validación
def obtener_longitud_variable(*args):
    for variable in args:
        if hasattr(variable, '__len__'):
            print(f"La longitud de {variable} es de tipo: {len(variable)}")
        else:
            print(f"La variable {variable} no admite la función len()")

obtener_longitud_variable(city, First_name, age)
"""

num_one = 5
num_two = 4 

total = num_one + num_two 
diff = num_one - num_two
produc = num_one * num_two
divide = num_one / num_two
remainder  = num_one % num_two
exp  = num_one ** num_two
print(exp)

