def main():
    #escribe tu código abajo de esta línea

 altura = float(input("Ingresa la altura (m):"))
 peso = float(input("Ingresa tu peso (kg):"))

 imc = peso / ((altura/100) * (altura/100))
 
 if imc <= 1:
    print("Revisa tus datos, alguno de ellos es erróneo.")
 elif imc < 20 :
    print("PESO BAJO")
 elif imc < 25 :
    print("PESO NORMAL")
 elif imc < 30 :
    print("SOBRE PESO")
 elif imc < 35 :
    print("OBESIDAD")
 elif imc < 40 :
    print("OBESIDAD MORBIDA")
 



if __name__=='__main__':
    main()