def main():
    #escribe tu código abajo de esta línea
    numero = -1
    suma = 0
    while(numero != 0):
        numero = int(input("Dame un número: "))
        suma += numero
    print(f"Suma de los números: {suma}")

if __name__=='__main__':
    main()
