def saludar():
    print("Bienvenido al programa de operaciones matemáticas y estadísticas.")

def pedir_flotantes(n, mensaje="Ingrese un número: "):
    return [float(input(mensaje)) for _ in range(n)]

def pedir_enteros(n, mensaje="Ingrese un número entero: "):
    return [int(input(mensaje)) for _ in range(n)]

def analizar_lista(nums):
    suma = sum(nums)
    promedio = suma / len(nums)
    positivos = sum(1 for x in nums if x > 0)
    negativos = sum(1 for x in nums if x < 0)
    ceros = nums.count(0)
    mult3 = sum(1 for x in nums if x % 3 == 0)
    return suma, promedio, positivos, negativos, ceros, mult3

def area_rect(base, altura): return base * altura
def perimetro_rect(base, altura): return 2 * (base + altura)
def es_primo(numero):

  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True

saludar()

while True:
    print("\n=== MENÚ DE OPERACIONES ===")
    print("1. Analizar lista de números reales")
    print("2. Área y perímetro de rectángulo")
    print("3. Verificar número primo")
    print("4. Análisis de calificaciones")
    print("5. Mayor, menor y frecuencia en lista")
    print("6. Calculadora básica")
    print("7. Salir")
    op = input("Seleccione una opción (1-7): ")

    match op:
        case "1":
            n = int(input("Cantidad de números: "))
            nums = pedir_flotantes(n)
            s, prom, pos, neg, ceros, m3 = analizar_lista(nums)
            print(f"Suma: {s}, Prom: {prom}, +: {pos}, -: {neg}, 0: {ceros}, Múltiplos de 3: {m3}")

        case "2":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            print(f"Área: {area_rect(b,h)}, Perímetro: {perimetro_rect(b,h)}")

        case "3":
            num = int(input("Número entero: "))
            print("Es primo." if es_primo(num) else "No es primo.")