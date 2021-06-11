def main():
    #escribe tu código abajo de esta línea
    promedio = 0
    numero = -1
    contador = 0
    while(numero != 0):
        numero = int(input("Dame un número: "))
        promedio += numero
        contador += 1 if numero != 0 else 0
    promedio /= contador
    print(f"El promedio de los números es: {promedio}")

if __name__=='__main__':
    main()
