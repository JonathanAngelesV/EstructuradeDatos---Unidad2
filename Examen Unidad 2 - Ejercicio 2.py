#Forma recursiva de elevar 2 a la n potencia
#Angeles Valadez Jonathan - 15211883
#Fecha: 10/5/2018
def potencia(numero):
    potenciaN = input("A que potencia deseas elevar 2?: ")
    Num = int(potenciaN)
    operacion = pow(2,Num)
    print(str(operacion))
    print(" ")
    potencia(numero)
           
potencia(0)
