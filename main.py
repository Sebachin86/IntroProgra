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
print('Escribe el primer número')
numero1 = int(input())
print('Escribe el segundo número')
numero2 = int(input())
print('Qué operación desea realizar? 1 (Suma), 2 (Resta), 3 (Multiplicación), 4 (División)')
def sumar (numero1,numero2):
  return (numero1+numero2)
suma1y2 = sumar(numero1,numero2)
if input('1') : print('El resultado de la suma es' , suma1y2)
