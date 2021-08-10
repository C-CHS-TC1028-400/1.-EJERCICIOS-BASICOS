import math
def main():
    #escribe tu código abajo de esta línea
    phi = (1 + math.sqrt(5)) / 2
    f = float(input("Número: "))
    k = int(input("Decimales a mostrar: "))

    resultado = round(phi * f, k)

    print(f"Razón áurea: {resultado}")

if __name__ == '__main__':
    main()
