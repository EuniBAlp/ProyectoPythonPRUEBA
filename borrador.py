print("Calculadora de Índice de Masa Corporal")
nombre=input("¿Cuál es tu nombre?")
ap= input("¿Cuál es tu apellido paterno?")
am=input("¿Cuál es tu apellido materno?")
edad=int (input("¿Cuántos años tienes?")) 
p=float (input("¿Cuánto pesas? Utiliza la unidad de medida en kg."))
e=float (input("¿Cuánto mides? Utiliza la unidad de medida en metros, por favor."))
print("Hola", nombre,ap,am)#Saluda
print ("Tu indice de masa corporal es el siguiente")#Agregaimc
IMC= p/e**2 #Se imprime el IMC
print ("IMC:"+str(IMC))
#Se hace validación
if IMC >=0 and IMC <= 18.5: print ("Peso bajo")
if IMC >=18.5 and IMC <= 24.9 : print ("Peso normal")
if IMC >=24.9 and IMC <= 29.9 : print ("Sobrepeso")
if IMC >=30 and IMC <= 34.9 :print ("Obesidad Tipo I")
if IMC >=35 and IMC <= 39.9 :print ("Obesidad Tipo II")
if IMC >= 40: print ("Obesidad Tipo III")
