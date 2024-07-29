print("Bienvenid@ a la Calculadora de Índice de Masa Corporal")
print ("Te pediremos unos datos, recuerda leer bien y contestar de forma precisa.")
#TERMINA PRESENTACION
#COMIENZA RECOLECCION Y VALIDACIÓN DE DATOS
nombre= str (input("¿Cuál es tu nombre?"))
while not nombre. isalpha (): 
     print ("Entendemos que cometiste un error, intenta de nuevo por favor.") 
     nombre=str(input("¿Cuál es tu nombre?"))
ap= str(input("¿Cuál es tu apellido paterno?"))
while not ap. isalpha():
     print ("Entendemos que cometiste un error, ingresa de nuevo tu apellido paterno por favor.")
     ap=str(input("¿Cuál es tu apellido paterno?"))
am= str (input("¿Cuál es tu apellido materno?"))
while not am. isalpha():
     print ("Entendemos que cometiste un error, ingresa de nuevo tu apellido materno por favor.")
     am=str(input("¿Cuál es tu apellido materno?"))
edad=str (input("¿Cuántos años tienes?"))
while not edad.isdigit(): 
     print ("Entendemos que hayas cometido un error, por favor ingresa tu edad en números enteros")
     edad= str (input("¿Cuántos años tienes?"))
#AQUI HACE FALTA VALIDACION PARA NUMEROS DECIMALES
p=float (input("¿Cuánto pesas? Utiliza la unidad de medida en kg."))
e=float (input("¿Cuánto mides? Utiliza la unidad de medida en metros, por favor."))
#HASTA ACA VALIDACION DE NUMEROS DECIMALES
#TERMINA LA RECOLECCIÓN Y VALIDACIÓN DE DATOS
#PRESENTA DATOS E IMC
print(f"HOLA", nombre,ap,am)
print (f"Tienes {edad} años de edad") 
print (f"Pesas {p} kilogramos.")
print (f"Mides {e} metros.")
print ("Tu indice de masa corporal es el siguiente.")
#AGREGA IMC
IMC= p/e**2 
print ("IMC:"+str(IMC))
#IMC VALIDACION TXT
if IMC <= 18.5: 
     print ("Te encuentras con un peso bajo")
elif IMC >=18.5 and IMC <= 24.9 :
     print ("Te encuentras en un peso normal")
elif IMC >=24.9 and IMC <= 29.9 : 
     print ("Tienes sobrepeso")
elif IMC >=30 and IMC <= 34.9 :
     print ("Te encuentras en obesidad Tipo I")
elif IMC >=35 and IMC <= 39.9 :
     print ("Te encuentras en obesidad Tipo II")
elif IMC >= 40: 
     print ("Te encuentras en obesidad Tipo III")
