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

def listamaterias():
  materias = [Matemáticas, Física, Química, Historia y Lengua]
  