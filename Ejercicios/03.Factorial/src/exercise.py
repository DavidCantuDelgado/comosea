def factorial(num):
    if(num == 0): return 1
    return num*factorial(num-1)

def main():
    #escribe tu código abajo de esta línea
    numero = int(input("Dame un número: "))
    print(f"El factorial es: {factorial(numero)}")

if __name__=='__main__':
    main()
