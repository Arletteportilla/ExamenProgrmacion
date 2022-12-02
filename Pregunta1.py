"""Crear un script que indique si el usuario es mayor de edad, 
menor de edad o es parte de la tercera edad.
 Puede utilizar la siguiente tabla."""


edad = int(input("Por favor ingrese su edad: "))
def edadCalcular(edad):
    if edad < 18:
        print("Es menor de edad")
    elif edad  >= 18 and edad <= 49:
        print("Es mayor de edad")
    elif edad > 49 and edad <= 120:
        print("Usted es parte de la 3ra Edad")    
    else:
        print("No existe rango")    

edadCalcular(edad)   