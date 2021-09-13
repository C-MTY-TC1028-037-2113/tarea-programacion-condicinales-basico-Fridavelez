def main():
    #escribe tu código abajo de esta línea

 altura = float(input("Ingresa la altura (m):"))
 peso = float(input("Ingresa tu peso (kg):"))

 imc = peso / ((altura/100) * (altura/100))

 if imc <= 1:
    print("Revise sus datos, alguno esta erroneo")
 elif imc < 20 :
    print("Usted esta en el PESO BAJO")
 elif imc < 25 :
    print("Usted esta en el PESO NORMAL")
 elif imc < 30 :
    print("Usted esta en el SOBRE PESO")
 elif imc < 35 :
    print("Usted esta en la OBESIDAD")
 elif imc < 40 :
    print("Usted esta en la OBESIDAD MORBIDA")
 



if __name__=='__main__':
    main()