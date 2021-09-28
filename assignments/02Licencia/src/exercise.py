
def main():
   edad = int(input("Ingresa tu edad: "))
   
   if edad <= 0:
     print("Respuesta incorrecta")
   elif edad >=18:
      id_oficial = input("¿Tienes identificación oficial? (s/n): " )
      if id_oficial == "s" or id_oficial == "S":
          print("Trámite de licencia concedido")
      elif id_oficial=="n" or id_oficial == "N":
          print("No cumples requisitos")
      else:
          print("Respuesta incorrecta")
   elif edad < 18:
     print("No cumples requisitos")
    
if __name__ == '__main__':
    main()
