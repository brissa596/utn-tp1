# ejercicio1
print("hola mundo!") 


# ejercicio2
nombre= input(" ingrese su nombre")
print(f"hola {nombre}, saludos") 


# ejercicio3
nombre=input("ingrese su nombre:")
apellido=input("ingrese su apellido:")
edad=int(input("ingrese su edad:"))
residencia=input("ingrese su residencia:")
print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#ejercicio4
radio=int(input("ingrese el radio de un circulo"))
pi= 3.1416
area= pi*(radio**2)
print(f"el area del circulo es ,{area}")

#ejercicio5
segundos=int(input("ingrese la cantidad de segundos:"))
horas= segundos/ 3600 
print(f"{segundos} segundos equivalen a {horas} horas")

#ejercicio6
numero=int(input("ingrese un numero :"))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#ejercicio7
numero1=int(input("ingrese un numero distinto a 0 :"))
numero2=int(input("ingrese otro numero distinto a 0 :"))
print("suma:",numero1+numero2)
print("resta :", numero1-numero2)
print("multiplicacion:", numero1*numero2)
print("division:", numero1/numero2)

#ejercicio8
altura=float(input("ingrese su altura:"))
peso=float(input("ingrese su peso:"))
imc= peso/altura*2
print(f"su masa corporal es :{imc}")

#Eejercicio9
celsius=float(input("ingrese la temperatura en grados celsius:"))
Fahrenheit=(9/5) * celsius + 32
print(f"la temperatura en grados Fahrenheit es :{Fahrenheit}")


#ejercicio10
numero1=int(input("ingrese un numero:"))
numero2=int(input("ingrese otro numero:"))
numero3=int(input("ingrese otro numero:"))
promedio = (numero1+numero2+numero3)/3
print(f"el promedio de los numeros es :{promedio}")