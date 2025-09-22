# Ejemplo en Python Español
def saludar(nombre):
    print(f"¡Hola, {nombre}!")
    return "Saludado"

for i in range(5):
    if i % 2 == 0:
        print(f"Número par: {i}")
    else:
        print(f"Número impar: {i}")

nombre = input("¿Cómo te llamas? ")
resultado = saludar(nombre)

if len(nombre) > 5:
    print("Tienes un nombre largo")
elif len(nombre) == 0:
    print("No ingresaste un nombre")
else:
    print("Tienes un nombre corto")
