#Python
#Ejercicio 1
#print('Hola Mundo')
#Ejercicio 2
#Saludo = '¡Hola Mundo!'
#print(Saludo)
#Ejercicio 3
#print('Hola, ¿Cuál es tu nombre?')
#Nombre = input()
#print('Hola, ' + Nombre + '!')
#Ejercicio 4
#print(((3+2)/(2*5))**2)
#Ejercicio 5
#print('Ingrese el Número de horas trabajadas')
#HorasTrabajadas = float(input())
#print('Ingrese el Costo por hora del lugar donde trabaja')
#CostoPorHora = float(input())
#Pago = str(HorasTrabajadas*CostoPorHora)
#print('El pago que le corresponde es de $' + Pago + ' Pesos.')
#Ejercicio 6
#print('Ingrese un número entero positivo')
#N = int(input())
#Resultado = ((N*(N+1))/2)
#print(Resultado)
#Ejercicio 7
#print('Indique su peso (En kg)')
#Peso = input()
#print('Ahora, Indique su Estatura (En M)')
#Estatura = input()
#MasaCorporal = round(float(Peso)/float(Estatura)**2,2)
#print('Tu Índice de Masa Corporal es', MasaCorporal)
#Ejercicio 8
#print('Escribe dos números enteros')
#N = int(input())
#M = int(input())
#C = str(N/M) 
#print('El Resultado es: ', C)
#R = str(N%M)
#print('Residuo: ', R)
#Ejercicio 9
#print('A continuación digite la cantidad a invertir')
#Inversion = float(input())
#print('Ahora, el interés anual')
#Interes = round(float(input()))
#print('Y por último, los años')
#Años = int(input())
#CapitalObtenido = str(round(Inversion*(Interes/100+1)**Años,2))
#print('Capital obtenido en la Inversión:', CapitalObtenido)
#Ejercicio 10
#hola
#Ejercicio 1
#print('Ingrese un número entero positivo')
#N = int(input())
#Resultado = ((N*(N+1))/2)
#if Resultado > 20 :
#  print('El resultado es:', Resultado, ', es un gran número!')
#else:
#  print('El resultado es', Resultado)
#Ejercicio 2
#print('Escribe dos números enteros')
#N = int(input())
#M = int(input())
#C = (N/M)
#print('El Resultado es: ', C)
#R = str(N%M)
#print('Residuo: ', R)
#if C<1 : print('El divisor es mayor al dividendo.')
#if C>1 : print('El divisor es menor que el dividendo.')
#if C==1 : print('El divisor y el dividendo son iguales.')
#Ejercicio 3 ''(Corregir)'':
#print('A continuación digite la cantidad a invertir')
#Inversion = float(input())
#print('Ahora, el interés anual')
#Interes = round(float(input()))
#print('Y por último, los años')
#Años = int(input())
#CapitalObtenido = str(round(Inversion*(Interes/100+1)**Años,2))
#if CapitalObtenido < str(100000) : print('Capital obtenido en la Inversión:' , str(CapitalObtenido) , '(Baja Rentabilidad)')
#if CapitalObtenido > 10000 and CapitalObtenido< 1000000 : print('Capital obtenido en la Inversión:', str(CapitalObtenido), '(Rentabilidad Moderada)')
#if CapitalObtenido > 1000000 : print('Capital obtenido en la Inversión:', str(CapitalObtenido), '(Es una buena Inversión)')
#Ejercicio 4 'Corregir':
#PesoPayaso = 112
#PesoMuñeca = 75
#print('Ingrese el número de payasos vendidos en el último pedido')
#PayasosVendidos = int(input())
#print('Ingrese el número de muñecas vendidas en el último pedido')
#MuñecasVendidas = int(input())
#PesoPayasosVendidos = PayasosVendidos*PesoPayaso
#PesoMuñecasVendidas = MuñecasVendidas*PesoMuñeca
#PesoVenta = PesoPayasosVendidos + PesoMuñecasVendidas
#if PesoVenta > 3000000 : input('Desea enviarlo?') 
#Respuesta = input('Está Seguro?')
#if Respuesta == 'Si' : print('Contenedor enviado')
#if Respuesta == 'No' : print('Contenedor no enviado')
#Ejercicio 1
#print('Escribe el primer número')
#numero1 = int(input())
#print('Escribe el segundo número')
#numero2 = int(input())
#def suma (numero1,numero2):
#  return (numero1+numero2)
#suma1y2 = suma(numero1,numero2)
#print('El resultado de la suma es' , suma1y2)
#Ejercicio2
#print('Escribe el primer número')
#numero1 = int(input())
#print('Escribe el segundo número')
#numero2 = int(input())
#def resta (numero1,numero2):
#  return (numero1-numero2)
#resta1y2 = resta(numero1,numero2)
#print('El resultado de la resta es' , resta1y2)
#Ejercicio3
#print('Escribe el primer número')
#numero1 = int(input())
#print('Escribe el segundo número')
#numero2 = int(input())
#def multi (numero1,numero2):
#  return (numero1*numero2)
#multi1y2 = multi(numero1,numero2)
#print('El resultado de la multiplicación es' , multi1y2)
#Ejercicio4 correjir division por cero
#print('Escribe el primer número')
#print('Escribe el segundo número')
#numero2 = int(input())
#def divi (numero1,numero2):
#  return (numero1/numero2)
#divi1y2 = divi(numero1,numero2)
#if numero1 == 0 : print('El resultado no está definido')
#elif numero2 == 0 : print('El resultado no está definido')
#else: print('El resultado de la división es' , divi1y2)
#Ejercicio 5 calculadorano terminado 
#print('Escribe el primer número')
#numero1 = int(input())
#print('Escribe el segundo número')
#numero2 = int(input())
#print('Qué operación desea realizar? 1 (Suma), 2 (Resta), 3 (Multiplicación), 4 (División)')
#def sumar (numero1,numero2):
  #return (numero1+numero2)
#suma1y2 = sumar(numero1,numero2)
#if input('1') : print('El resultado de la suma es' , suma1y2)
#Ejercicio 6
#def intereses(inv):
  #d= inv
  #if (d>0 and d<1000000):
    #return 2
  #elif(d>=1000000 and d < 2000000):
    #return 5
  #else:
    #return 7

#def calBalance(int, inv):
  #n=int
  #d=inv
  #return round((d*(1+(n/100))),2)

#def ctaAhorro():
  ##inversion,interes,b1,b2,b3 = 0.0
  #inversion = float(input('Ingrese el valor de la inversión: '))
  #interes=intereses(inversion)
  #b1=calBalance(interes,inversion)
  #b2=calBalance(interes,b1)
  #b3=calBalance(interes,b2)
  #print('Balance año 1: ' + str(b1) + ' Balance año 2: ' + str(b2) +  'Balance año 3: ' + str(b3))

#ctaAhorro()
#Ejercicio1
#def calAreaTri(base,altura):
  #area = (base * altura)/2
  #return area

#def calAreaCua(lado):
  #area = (lado * lado)
  #return area

#def calAreaCir(radio):
  #area = (math.pi * (radio)**2)
  #return area

#def main():
  #figura = input('¿Qué figura desea calcular? (triangulo/cuadrado/circulo): ')
  #if figura == 'triangulo':
      #base= float(input('Ingrese la base del triangulo'))


##profe
#def areaTriangulo(b,a):
  #return(b*a)/2

#def areaCuadrado(bc,ac):
  #return bc*ac

#def areaCirculo(r):
  #return(3.14159*(r**2))

#def areaFig():
  #area=0.0
  #figura=''
  #figura = input('Escriba la figura a la que se le desea calcular el área: ')
  
  #if (figura.lower()=='triangulo'):
    #base=0.0
    #altura=0.0
    #base = float(input('Ingrese la base '))
    #altura = float(input('Ingrese la altura '))
    #area = areaTriangulo(base,altura)
    #print('El área del triangulo es: ' , area)

#areaFig()
#Ejercicio3
#def maximo(a,b):
  #if x>y:
    #return x
  #else:
    #return y

#def minimo(a,b):
  #if x<y:
    #return x
  #else:
    #return y

#programa principal
#x=int(input('Un número: '))
#y=int(input('Otro número: '))
#print(maximo(x-3, minimo(x+2, y-5)))
#Ejercicio 4
#precioSinIVA = float(input('Ingrese el precio sin IVA del estéreo'))
#marca = input('Ingrese la marca del estéreo')

#descuento = 0.10
#if marca == 'NOSY':
    #descuento += 0.05

#if precioSinIVA >= 2000000:
  #precioConDescuento = precioSinIVA * (descuento)


#IVA = 0.20
#precioConIVA = precioSinIVA * (IVA)

#print(f'El cliente pagará ${precioConIVA} con IVA incluido')








'''año = int(input("Ingrese un año: "))

#los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí, Ejemplos de respuesta: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(año , "es bisiesto")
else:
    print(año , "no es bisiesto")'''



'''altura = float(input("Ingrese la altura del perro en cm: "))
peso = float(input("Ingrese el peso del perro en kg: "))

# El tamaño de los perros mestizos pequeños es determinado por la altura hasta 30 cm y su peso aproxima los 15 kilos. Los perros mestizos medianos, miden entre 30 y 40 cm de altura y pueden llegar pesar entre 15 y 25 kg. Y finalmente los perros mestizos grandes suelen medir entre 40 y 60 cm y pesar entre 25 y 45 kg.
if altura <= 30 and (peso >= 14.5 and peso < 16.5):
    print("El perro es pequeño")
elif altura > 30 and altura <= 40 and peso > 15 and peso <= 25:
    print("El perro es mediano")
elif altura > 40 and altura <= 60 and peso > 25 and peso <= 45:
    print("El perro es grande")
else:
    print("El tamaño del perro no se puede determinar")'''




'''# Kelvin a Celsius
def KaC(temperatura):
    return temperatura - 273.15

# Kelvin a Fahrenheit
def KaF(temperatura):
    return (temperatura - 273.15) * 9/5 + 32

# Celsius a Kelvin
def CaK(temperatura):
    return temperatura + 273.15

# Celsius a Fahrenheit
def CaF(temperatura):
    return (temperatura * 9/5) + 32

# Fahrenheit a Kelvin
def FaK(temperatura):
    return (temperatura - 32) * 5/9 + 273.15

# Fahrenheit a Celsius
def FaC(temperatura):
    return (temperatura - 32) * 5/9

temperatura = float(input("Ingrese la temperatura: "))
escalaActual = input("Ingrese la escala actual (K, C o F): ")
escalaConversion = input("Ingrese la escala a la que desea convertir (K, C o F): ")

if escalaActual == 'K':
    if escalaConversion == 'C':
        resultado = KaC(temperatura)
    elif escalaConversion == 'F':
        resultado = KaF(temperatura)
elif escalaActual == 'C':
    if escalaConversion == 'K':
        resultado = CaK(temperatura)
    elif escalaConversion == 'F':
        resultado = CaF(temperatura)
elif escalaActual == 'F':
    if escalaConversion == 'K':
        resultado = FaK(temperatura)
    elif escalaConversion == 'C':
        resultado = FaC(temperatura)


print("La temperatura convertida es: " , resultado , escalaConversion)'''





'''nombre = input("Ingrese el nombre del participante: ")
edad = int(input("Ingrese la edad del participante: "))


grupo = ""
costoBase = 0


if 10 <= edad <= 17:
    grupo = "Niños"
    costoBase = 25000
    if 10 <= edad <= 13:
        descuento = 0.15
    elif edad > 13 and edad <= 17:
        descuento = 0.08
elif 18 <= edad <= 50:
    grupo = "Adultos"
    costoBase = 35000
    if 18 <= edad <= 30:
        descuento = 0.11
    elif edad > 30 and edad <= 50:
        descuento = 0.09
elif edad > 50:
    grupo = "Adulto Mayor"
    costoBase = 50000
    if edad > 65:
        descuento = 0.40
else:
    print("El participante no califica para ningún grupo.")
    exit()

valorConDescuento = costoBase - (costoBase * descuento)

print("Nombre del participante: " , nombre)
print("Grupo: " , grupo)
print("Costo del grupo: $" , costoBase)
print("Valor a pagar con descuento: $" , valorConDescuento)'''








'''tipoRecipiente = input("Ingrese el tipo de recipiente (cubo, cilindro o esfera): ").lower()

if tipoRecipiente == "cubo":
    lado = float(input("Ingrese la longitud de un lado del cubo: "))
    volumenCubo = lado ** 3
    print("El volumen del cubo es: " , volumenCubo)
elif tipoRecipiente == "cilindro":
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    volumenCilindro = 3.14159 * radio**2 * altura
    print("El volumen del cilindro es: " , volumenCilindro)
elif tipoRecipiente == "esfera":
    radio = float(input("Ingrese el radio de la esfera: "))
    volumenEsfera = (4/3) * 3.14159 * radio**3
    print("El volumen de la esfera es: " , volumenEsfera)
else:
    print("Tipo de recipiente no válido. Por favor, ingrese cubo, cilindro o esfera.")'''




'''cantidadCubos = int(input("Ingrese la cantidad de cubos de Rubik a enviar: "))

tipoCaja = input("Ingrese el tipo de caja (pequeña, mediana, grande o extragrande): ").lower()


volumenCubo = 167

volumenCajaPequeña = 5000
volumenCajaMediana = 7000
volumenCajaGrande = 10000
volumenCajaExtragrande = 15000

cantidadCajasNecesarias = 0


if tipoCaja == "pequeña":
    cantidadCajasNecesarias = cantidadCubos * volumenCubo / volumenCajaPequeña
elif tipoCaja == "mediana":
    cantidadCajasNecesarias = cantidadCubos * volumenCubo / volumenCajaMediana
elif tipoCaja == "grande":
    cantidadCajasNecesarias = cantidadCubos * volumenCubo / volumenCajaGrande
elif tipoCaja == "extragrande":
    cantidadCajasNecesarias = cantidadCubos * volumenCubo / volumenCajaExtragrande

if cantidadCajasNecesarias > 0:
    print(f"Se necesitan {int(cantidadCajasNecesarias)} cajas {tipoCaja} para el envío.")
else:
    print("No se puede realizar el envío con la caja seleccionada debido al tamaño insuficiente.")'''


'''def intereses(inv):
  d= inv
  if (d>0 and d<1000000):
    return 2
  elif(d>=1000000 and d < 2000000):
    return 5
  else:
    return 7

def calBalance(int, inv):
  n=int
  d=inv
  return round((d*(1+(n/100))),2)

def ctaAhorro():
  inversion,interes,b1,b2,b3 = 0.0
  inversion = float(input('Ingrese el valor de la inversión: '))
  interes=intereses(inversion)
  b1=calBalance(interes,inversion)
  b2=calBalance(interes,b1)
  b3=calBalance(interes,b2)
  print('Balance año 1: ' + str(b1) + ' Balance año 2: ' + str(b2) +  'Balance año 3: ' + str(b3))

ctaAhorro()'''




'''#Parcial1
#Punto2
def intereses(inv):
  d= inv
  if (d>0 and d<1000000):
    return 2
  elif(d>=1000000 and d < 2000000):
    return 5
  else:
    return 7

def calBalance(int, inv):
  n=int
  d=inv
  return round((d*(1+(n/100))),2)

def ctaAhorro():
  #inversion,interes,b1,b2,b3 = 0.0
  inversion = float(input('Ingrese el valor de la inversión: '))
  interes=intereses(inversion)
  b1=calBalance(interes,inversion)
  b2=calBalance(interes,b1)
  b3=calBalance(interes,b2)
  print('Balance año 1: ' + str(b1) + ' Balance año 2: ' + str(b2) +  ' Balance año 3: ' + str(b3))

ctaAhorro()'''
'''#Ejercicio 3
def porcentaje(w,z):

    return (w*(1+(z/100)))

 

w=int(input("Ingrese valor: "))

z=int(input("Ingrese porcentaje: "))

print(round(porcentaje(w-20000, z+2),2))'''
'''#Ejercicio 4
panComprado = int(input("Ingrese la cantidad de Pan tajado comprado "))
arepasCompradas = int(input("Ingrese la cantidad de Arepas compradas "))
jamonesComprados = int(input("Ingrese la cantidad de Jamon comprado "))
valorjamonesComprados = jamonesComprados * 7000
valorpanComprado = panComprado *
valorarepasCompradas = arepasCompradas * 
if jamonesComprados == 2:
    descuento = 0.02
    if jamonesComprados >2 and jamonesComprados <=5:
        descuento = 0.05
    elif jamonesComprados > 5:
        valorJamonescomprados - 7000
if arepasCompradas >= 1:
    descuento = 0.03
if arepasCompradas >=1 and panComprado >=1 and jamonesComprados >=1:
  descuento = 0.02
  valorTotal * descuento'''


'''A = 0
while A < 10:
  print(A) 
  A = A + 1'''


'''print('************************* Menu')

input('Selecione Opción:')'''


'''numerousuario = int(input('Ingrese un Número: '))

for tabla in range (1,11,1):
    print(numerousuario*tabla)'''

'''def factorial():
  numero = int(input('Ingresa un Número: '))
  factorial = 1

for i in range (1 + numerodado + 1):
     factorial *= i
  
  print('El Factorial de', numero, 'es', factorial)

factorial()'''
'''lista=['pato','gallina']
lista.append('perro')
lista.index(0)
lista.remove('perro')
lista.sort()'''

'''print('Ingrese 5 caracteres para enlistarlos')
primero=input()
segundo=input()
tercero=input()
cuarto=input()
quinto=input()

lista=[primero , segundo , tercero , cuarto , quinto]

print(lista)'''

'''def listanumeros():
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  for i in range(1,11):
      print(numeros[-i], end=', ')

listanumeros()'''

'''def listamaterias():
  materias = [Matemáticas, Física, Química, Historia y Lengua]'''

'''# agregar nuevo contacto 1
def agregar_contacto(lista_contactos, nombre, telefono, correo):
    nuevo_contacto = [nombre, telefono, correo]
    lista_contactos.append(nuevo_contacto)
    print(f"Contacto '{nombre}' agregado con éxito.")

# buscar nombre 2
def buscar_contacto_por_nombre(lista_contactos, nombre):
    for contacto in lista_contactos:
        if contacto[0] == nombre:
            print("Información del contacto:")
            print(f"Nombre: {contacto[0]}")
            print(f"Teléfono: {contacto[1]}")
            print(f"Correo electrónico: {contacto[2]}")
            return
    print(f"El contacto '{nombre}' no se encontró en la lista.")

# mostrar contactos 3
def mostrar_contactos(lista_contactos):
    if not lista_contactos:
        print("No hay contactos almacenados.")
    else:
        print("Lista de contactos:")
        for i, contacto in enumerate(lista_contactos, start=1):
            print(f"{i}. Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Correo: {contacto[2]}")

# almacenar los contactos
lista_de_contactos = []

while True:
    print("\n--- GESTIÓN DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        correo = input("Ingrese el correo electrónico: ")
        agregar_contacto(lista_de_contactos, nombre, telefono, correo)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        buscar_contacto_por_nombre(lista_de_contactos, nombre)
    elif opcion == "3":
        mostrar_contactos(lista_de_contactos)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4).")'''

 #multiplicar matrices
'''

def multiplicar_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplicar_matrices(matriz1, matriz2)
print(resultado)'''
'''
#adivinar numero
import random
def adivina():
  numero_secreto = random.randint(1, 100)
  adivinado = False

  while not adivinado:
      intento = int(input('Adivina el número: '))
      if intento == numero_secreto:
          print('¡Correcto! Has adivinado el número.')
          adivinado = True
      elif intento < numero_secreto:
          print('El número es mayor.')
      else:
          print('El número es menor.')

adivina()'''
'''
#ejerciciodivisachatgpt
# Crear el diccionario con las divisas y sus símbolos
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Solicitar al usuario una divisa
divisa = input("Introduce una divisa: ")

# Comprobar si la divisa está en el diccionario
if divisa in divisas:
    simbolo = divisas[divisa]
    print(f"El símbolo de {divisa} es {simbolo}")
else:
    print("La divisa no está en el diccionario.")

'''
'''
#ejericiodivisaprofe
def divisaSimbol():
  monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
  moneda = input('Introduce una divisa: ')
  if moneda.title() in monedas:
      print(monedas[moneda.title()])
  else:
      print('La divisa no está.')

divisaSimbol()
'''
'''
#cuadradoschatgpt
# Solicitar al usuario un número
numero = int(input("Introduce un número: "))

# Crear un diccionario con claves y valores cuadrados
diccionario = {i: i**2 for i in range(1, numero + 1)}

# Imprimir el diccionario
print(diccionario)

#cuadradosprofe
'''
'''
def numeroCuadrado():
  numero = int(input('Dime un número:'))
  cuadrados = ()

  for num in range(1,numero+1):
      cuadrados[num] = num ** 2
  for num, valor in cuadrados.items():
      print('%d -> %d' %  (num,valor))

numeroCuadrado()
'''
'''
#cadenachatgpt
# Solicitar al usuario una cadena
cadena = input("Introduce una cadena: ")

# Crear un diccionario para contar las apariciones de caracteres
conteo = {}

# Iterar a través de la cadena y contar las apariciones
for caracter in cadena:
    if caracter in conteo:
        conteo[caracter] += 1
    else:
        conteo[caracter] = 1

# Imprimir el diccionario de conteo
print(conteo)
'''
#cadenaprofe
'''
def cadenaRep():
  cadena = input('Dame una cadena:')
  for caracter in cadena:
    if caracter in dict:
      dict[caracter]+=1
    else:
      dict[caracter]=1

  for caracter, valor in dict.items():
    print(caracter, valor)

cadenaRep()
'''
'''
#ejercicionombrelohiceyo
nombre = input("Introduce tu nombre: ")
edad = input('Introduce tu edad: ')
direccion = input('Introduce tu dirección: ')
telefono = input('introduce tu teléfono: ')

diccionario = {'Nombre': 'nombre', 'Edad': 'edad', 'Direccion': 'direccion', 'Telefono': 'telefono'}

print(nombre, 'tiene', edad, 'años, vive en', direccion, 'y su número de teléfono es',  telefono)
#correccion, podrías definir primero todo en una función y al final solo ejecutar la función
'''

#ejerciciofrutas

'''diccionario = {'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input('Introduce el nombre de una fruta: ')
kilos = input('Introduce el número de kilos de fruta: ')
precio = diccionario[fruta.title()] * kilos
print('El precio total de las frutas es:', precio)
if fruta in diccionario:
  print(kilos, 'kilos de', fruta, 'valen', '$', diccionario[fruta.title()])'''

#faltacorregir

#triqui 

#Triqui
'''def inicializar_tablero():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    return tablero

def imprimir_tablero(tablero):
    filaT=0
    for fila in tablero:
        filaT=filaT+1
        print("|".join(fila))
        if filaT <= 2:
           print("-" * 5)

def realizar_jugada(tablero, jugador, fila, columna):
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador
        return True
    else:
        return False

def verificar_estado(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    # Verificar empate
    empate = all(tablero[i][j] != ' ' for i in range(3) for j in range(3))
    if empate:
        return 'Empate'

    return None

def jugar_triqui():
    tablero = inicializar_tablero()
    jugador_actual = 'X'

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")

        fila = int(input("Ingrese el número de fila (0, 1, o 2): "))
        columna = int(input("Ingrese el número de columna (0, 1, o 2): "))

        if realizar_jugada(tablero, jugador_actual, fila, columna):
            estado = verificar_estado(tablero)

            if estado:
                imprimir_tablero(tablero)
                if estado == 'Empate':
                    print("¡Es un empate!")
                else:
                    print(f"¡El jugador {estado} ha ganado!")
                break

            if jugador_actual == 'X':
              jugador_actual = 'O' 
            else: 
              jugador_actual= 'X'

jugar_triqui()
'''
#mazo
'''
import random

# Crear un mazo de cartas
def crear_mazo():
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    mazo = [{'valor': valor, 'palo': palo} for valor in valores for palo in palos]
    return mazo

# Barajar el mazo
def barajar_mazo(mazo):
    random.shuffle(mazo)

# Repartir cartas a los jugadores
def repartir_cartas(mazo, num_jugadores, cartas_por_jugador):
    manos = [[] for _ in range(num_jugadores)]

    for _ in range(cartas_por_jugador):
        for jugador in range(num_jugadores):
            carta = mazo.pop()
            manos[jugador].append(carta)

    return manos

# Mostrar las cartas que le quedaron a cada jugador
def mostrar_cartas(manos):
    for i, mano in enumerate(manos):
        print(f'Jugador {i + 1}:')
        for carta in mano:
            print(f" - {carta['valor']} de {carta['palo']}")

def main():
    mazo = crear_mazo()
    barajar_mazo(mazo)
    num_jugadores = 2
    cartas_por_jugador = 5

    manos = repartir_cartas(mazo, num_jugadores, cartas_por_jugador)
    mostrar_cartas(manos)

if __name__ == "__main__":
    main()
'''
# ejercicios
'''
#Crea un programa para llevar un registro de ventas diarias en una tienda. Cada venta se representa como una lista de listas con detalles como el producto vendido, la cantidad y el precio. Calcular el total de ventas diarias y mostrarlo en pantalla.

# Función para calcular el total de una venta
def calcular_total(venta):
    return venta[1] * venta[2]

# Función para calcular el total de ventas diarias
def calcular_total_ventas(ventas):
    total = 0
    for venta in ventas:
        total += calcular_total(venta)
    return total

# Función para mostrar el detalle de las ventas
def mostrar_ventas(ventas):
    for i, venta in enumerate(ventas, start=1):
        producto, cantidad, precio_unitario = venta
        total_venta = calcular_total(venta)
        print(f"Venta {i}:")
        print(f"Producto: {producto}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio Unitario: ${precio_unitario}")
        print(f"Total de la Venta: ${total_venta}")
        print("-" * 20)

def main():
    ventas_diarias = []
    while True:
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto == "fin":
            break
        cantidad = int(input("Ingrese la cantidad vendida: "))
        precio_unitario = float(input("Ingrese el precio unitario: "))
        venta = [producto, cantidad, precio_unitario]
        ventas_diarias.append(venta)

    print("\nRegistro de Ventas Diarias:")
    mostrar_ventas(ventas_diarias)
    total_ventas = calcular_total_ventas(ventas_diarias)
    print(f"Total de Ventas Diarias: ${total_ventas}")

if __name__ == "__main__":
    main()

#Crea un programa que permita sumar 2 matrices, que serán representadas como listas de listas, y guardar el resultado en una nueva matriz para ser mostrado en pantalla.

# Función para sumar dos matrices
def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("No se pueden sumar matrices de diferentes tamaños.")
        return None

    resultado = []

    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0]):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)

    return resultado

# Función para mostrar una matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

def main():
    # Definir las matrices
    matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    # Sumar las matrices
    resultado = sumar_matrices(matriz1, matriz2)

    if resultado:
        print("Matriz 1:")
        mostrar_matriz(matriz1)
        print("\nMatriz 2:")
        mostrar_matriz(matriz2)
        print("\nResultado de la suma:")
        mostrar_matriz(resultado)

if __name__ == "__main__":
    main()

# Crea una función que tome una matriz representada como una lista de listas y devuelva su matriz transpuesta. La matriz transpuesta se obtiene intercambiando filas por columnas.

# Función para calcular la matriz transpuesta
def matriz_transpuesta(matriz):
    # Obtener el número de filas y columnas de la matriz original
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    # Crear una matriz vacía para la matriz transpuesta
    matriz_transpuesta = []

    # Recorrer las columnas y crear filas en la matriz transpuesta
    for j in range(num_columnas):
        fila_transpuesta = []
        for i in range(num_filas):
            fila_transpuesta.append(matriz[i][j])
        matriz_transpuesta.append(fila_transpuesta)

    return matriz_transpuesta

# Función para mostrar una matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

# Ejemplo de uso
def main():
    matriz_original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matriz Original:")
    mostrar_matriz(matriz_original)

    matriz_transpuesta_resultante = matriz_transpuesta(matriz_original)

    print("\nMatriz Transpuesta:")
    mostrar_matriz(matriz_transpuesta_resultante)

if __name__ == "__main__":
    main()

# Crea una función que realice la multiplicación de dos matrices. La multiplicación de matrices implica multiplicar cada elemento de una fila de la primera matriz por cada elemento de una columna de la segunda matriz y sumar los resultados.

# Función para multiplicar dos matrices
def multiplicar_matrices(matriz1, matriz2):
    # Asegurarse de que las matrices sean multiplicables
    if len(matriz1[0]) != len(matriz2):
        print("No se pueden multiplicar las matrices debido a dimensiones incompatibles.")
        return None

    # Obtener el número de filas y columnas de las matrices
    num_filas_matriz1 = len(matriz1)
    num_columnas_matriz1 = len(matriz1[0])
    num_columnas_matriz2 = len(matriz2[0])

    # Crear una matriz vacía para el resultado
    resultado = [[0 for _ in range(num_columnas_matriz2)] for _ in range(num_filas_matriz1)]

    # Realizar la multiplicación de matrices
    for i in range(num_filas_matriz1):
        for j in range(num_columnas_matriz2):
            for k in range(num_columnas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

# Función para mostrar una matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

# Ejemplo de uso
def main():
    matriz1 = [[1, 2, 3], [4, 5, 6]]
    matriz2 = [[7, 8], [9, 10], [11, 12]]

    print("Matriz 1:")
    mostrar_matriz(matriz1)

    print("\nMatriz 2:")
    mostrar_matriz(matriz2)

    resultado = multiplicar_matrices(matriz1, matriz2)

    if resultado:
        print("\nResultado de la multiplicación:")
        mostrar_matriz(resultado)

if __name__ == "__main__":
    main()

#Crea una función que encuentre el elemento máximo en una matriz representada como una lista de listas.

# Función para encontrar el elemento máximo en una matriz
def encontrar_maximo_en_matriz(matriz):
    if not matriz:
        return None

    maximo = matriz[0][0]

    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento

    return maximo

# Ejemplo de uso
def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matriz:")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

    maximo = encontrar_maximo_en_matriz(matriz)

    if maximo is not None:
        print(f"El elemento máximo en la matriz es: {maximo}")
    else:
        print("La matriz está vacía.")

if __name__ == "__main__":
    main()

#Crea una función que realice el producto escalar de una matriz por un número. Debes multiplicar cada elemento de la matriz por el número dado y devolver la matriz resultante.

# Función para realizar el producto escalar de una matriz por un número
def producto_escalar(matriz, numero):
    resultado = []

    for fila in matriz:
        fila_resultado = [elemento * numero for elemento in fila]
        resultado.append(fila_resultado)

    return resultado

# Función para mostrar una matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

# Ejemplo de uso
def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    numero = 2

    print("Matriz Original:")
    mostrar_matriz(matriz)

    resultado = producto_escalar(matriz, numero)

    print(f"\nResultado del producto escalar por {numero}:")
    mostrar_matriz(resultado)

if __name__ == "__main__":
    main()






'''
#parcial 2

#clase
#ejercicio1(malo)
'''set1 = input
set1 = {hola, adios, buenas, chao}
set2 = {adios, chao}
if set2 in set1:
    print('El conjunto 2 está contenido en el conjunto 1')
'''
#ejercicio2
'''set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set1 = {x for x in set1 if x % 2 == 0}
print(set1)'''
#otra solucion
'''def eliminaImparSet():
  numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

  numbers = {x for x in numbers if x % 2 == 0}
  print(numbers)

eliminaImparSet()'''
#Ejercicio3
estudiantes_primaria = set()
estudiantes_secundaria = set()

# pedir nombres primaria
print("Ingrese los nombres de los estudiantes de primaria (digite 'salir' para salir):")
while True:
    nombre = input()
    if nombre == 'salir':
        break
    else:
        estudiantes_primaria.add(nombre)

# pedir nombres secundaria
print("Ingrese los nombres de los estudiantes de secundaria (digita 'salir' para salir):")
while True:
    nombre = input()
    if nombre == 'salir':
        break
    else:
        estudiantes_secundaria.add(nombre)

# mostrar nombres sin repetir de primaria y secundaria
print("Nombres de alumnos de primaria y secundaria sin repetir:")
print(estudiantes_primaria | estudiantes_secundaria)

# mostrar nombres que se repiten
print("Nombres de alumnos que se repiten:")
print(estudiantes_primaria & estudiantes_secundaria)

# mostrar nombres de primaria que no se repiten en secundaria
print("Nombres de alumnos de primaria que no se repiten en secundaria:")
print(estudiantes_primaria - estudiantes_secundaria)