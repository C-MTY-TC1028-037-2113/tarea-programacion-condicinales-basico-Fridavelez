
def main():
   edad = int(input("Ingresa tu edad: "))
   
   if edad >= 18:
      identificacion = (input("¿Tienes identificación oficial? (s/n): "))
      
      if identificacion == ("n" or "N"):
         print("No cumples requisitos")
      elif identificacion == ("s" or "S"):
         print("Trámite de licencia concedido")
             
   elif edad <=18:
         print("No cumples requisitos")
   else: 
         print("Respuesta incorrecta")
 

if __name__ == '__main__':
    main()
