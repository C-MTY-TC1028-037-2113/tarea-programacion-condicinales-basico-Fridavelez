def main():
    #escribe tu código abajo de esta línea
 
 peso = float(input("Peso en kg: "))
 altura = float(input("Altura en m: "))

 if altura <= 0:
    print("Revisa tus datos, alguno de ellos es erróneo.")

 imc = peso/(altura**2)

 if imc < 20 :
    print("PESO BAJO")
 elif imc < 25 :
    print("NORMAL")
 elif imc < 30 :
    print("SOBRE PESO")
 elif imc < 35 :
    print("OBESIDAD")
 elif imc < 40 :
    print("OBESIDAD MORBIDA")


      


if __name__=='__main__':
    main()