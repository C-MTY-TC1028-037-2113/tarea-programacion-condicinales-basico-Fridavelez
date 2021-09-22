
def main():
   edad = int(input("Ingresa tu edad: "))
   
   if edad >= 18:
      identificacion = (input("¿Tienes identificación oficial? (s/n): "))
      
      if identificacion == "n":
         print("No cumples con los requisitos")
      
      if identificacion == "s":
         print("Tramite de licencia concedido")
             
   elif edad <=18:
         print("No cumples los requisitos")
   else: 
         print("Respuesta incorrecta")
 

if __name__ == '__main__':
    main()
