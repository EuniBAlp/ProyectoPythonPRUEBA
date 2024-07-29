print("Bienvenid@ a la Calculadora de Índice de Masa Corporal")
print ("Te pediremos unos datos, recuerda leer y contestar de forma precisa.")
nombre= str (input("¿Cuál es tu nombre?"))
while not nombre. isalpha (): print ("Nombre inválido, intenta de nuevo por favor.") 

ap= str(input("¿Cuál es tu apellido paterno?"))
while not ap. isalpha(): print ("Apellido inválido, intenta de nuevo por favor.")

am= str (input("¿Cuál es tu apellido materno?"))
while not am. isalpha(): ("Apellido inválido, intenta de nuevo por favor.")

edad=int (input("¿Cuántos años tienes?")) 
p=float (input("¿Cuánto pesas? Utiliza la unidad de medida en kg."))
e=float (input("¿Cuánto mides? Utiliza la unidad de medida en metros, por favor."))
print("Hola", nombre,ap,am)#Saluda
print ("Tu indice de masa corporal es el siguiente")#Agregaimc
IMC= p/e**2 #Se imprime el IMC
print ("IMC:"+str(IMC))
#Se valida imc
if IMC <= 18.5: print ("Peso bajo")
elif IMC >=18.5 and IMC <= 24.9 : print ("Peso normal")
elif IMC >=24.9 and IMC <= 29.9 : print ("Sobrepeso")
elif IMC >=30 and IMC <= 34.9 :print ("Obesidad Tipo I")
elif IMC >=35 and IMC <= 39.9 :print ("Obesidad Tipo II")
elif IMC >= 40: print ("Obesidad Tipo III")
