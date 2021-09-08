
def main():
    edad = int(input("Ingresa tu edad: "))
    identificacion = str(input("Tienes identifecacion oficial s/n?: "))



    if edad >= 18:
        if identificacion =="s":
            print("Tramite de licencia concedido")
        elif identificacion == "n":
            print("No cumple los requisitos")
        else:
             print("respuesta incorrecta")
    elif edad <=17:
       print("No cumples los requisitos")
    else: 
        print("respuesta incorrecta")


if __name__ == '__main__':
    main()
