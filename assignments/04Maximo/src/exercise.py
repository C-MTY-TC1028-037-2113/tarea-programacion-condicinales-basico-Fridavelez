def main():
    #escribe tu código abajo de esta línea

    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    if x > z and x > y:
        print(x)
    elif y > x and y > z:
        print(y)
    elif z > y and z > x:
        print(z)
     
if __name__=='__main__':
    main()
  