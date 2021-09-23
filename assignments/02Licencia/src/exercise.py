
def main():
   edad = int(input("Ingresa tu edad: "))
   
   if edad >= 18:
       identificacion=(input("¿Tienes identificación oficial? (s/n): "))
      
       if identificacion == "n" or identificacion == "N":
         print("No cumples requisitos")
       elif identificacion == "s" or identificacion == "S":
         print("Trámite de licencia concedido")
       else:
         print("Respuesta incorrecta")

   elif edad <18:
        print("No cumples requisitos")
 
 

if __name__ == '__main__':
    main()
