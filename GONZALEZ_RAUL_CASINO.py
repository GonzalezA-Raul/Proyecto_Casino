import random
import time

base_datos_dados = []
accion = ""

# FUNCIONES

def menu():
    print("==========================")
    print("========= CASINO =========")
    print("==========================")
    print("(S) Salir")
    print("(T) Tirar dados")
    print("(M) Media Aritmética")
    print("(E) Estadisticas números")
    print("==========================")

def tirar_dado ():
    valor_dado_1 = random.randint (1,6)
    valor_dado_2 = random.randint (1,6)
    base_datos_dados.append ((valor_dado_1,valor_dado_2))
    dibujar_dado(valor_dado_1)
    dibujar_dado(valor_dado_2)
    

def dibujar_dado (n):
    print("*****")
    print(f"* {n} *")
    print("*****")

def media_aritmetica():
    suma = 0
    total_valores = 0
    for num in base_datos_dados:
        suma += num[0] + num[1]
        total_valores += 2
    print(f"La media aritmetica de las {total_valores/2} tiradas da un total de {suma/total_valores}") 

def estadisticas ():
    cont = [0] * 6
    tiradas = len(base_datos_dados)*2

    for (valor_dado_1, valor_dado_2) in base_datos_dados:
        cont[valor_dado_1 - 1] += 1
        cont[valor_dado_2 - 1] += 1
    print("Estadisticas de los números")
    for n in range (6):
        porcentaje = (cont[n]/tiradas)*100
        print(f"El {n + 1} ha salido {cont[n]} veces del total. Un {porcentaje}%")


while accion != "S":
    menu()
    accion = str(input("Que acción deseas realizar: ")).upper()
    if accion == "T":
        print("Lanzando...")
        time.sleep(2)
        tirar_dado()
        time.sleep(3)
    elif accion == "M":
        media_aritmetica()
        time.sleep(2)
    elif accion == "E":
        estadisticas()
        time.sleep(2)
    elif accion =="S":
        print("Saliendo del casino...")
        time.sleep(1)
        print("¡Hasta pronto!")
    else:
        print("Opción no válida. Ingresa de nuevo")
        time.sleep(1)
    