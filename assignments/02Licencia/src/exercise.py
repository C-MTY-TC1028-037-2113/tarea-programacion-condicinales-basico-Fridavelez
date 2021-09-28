
def main():
   edad = int(input("Ingresa tu edad: "))
   
   if edad >= 0:
     print("Respuesta incorrecta")
   elif edad < 18:
     print("No cumples requisitos")
   else:
        id_oficial = input("¿Tienes identificación oficial? (s/n): " ).lower()
        if id_oficial == "s":
            print("Trámite de licencia concedido")
        elif id_oficial=="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")

if __name__ == '__main__':
    main()
