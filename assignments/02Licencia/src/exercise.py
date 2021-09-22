
def main():
   edad = int(input("Ingresa tu edad: "))
   


   if edad >= 18:
      identificacion = str(input("¿Tienes identificación oficial? (s/n): "))
      if identificacion == "s" or "S":
          print("Tramite de licencia concedido")
      elif identificacion == "n" or "N":
          print("No cumples los requisitos")
      else:
          print("Respuesta incorrecta")        
   elif edad <=18:
       print("No cumples los requisitos")
   else: 
        print("Respuesta incorrecta")
 

if __name__ == '__main__':
    main()
