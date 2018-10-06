#Forma recursiva de sumar los numeros 1,2,3,4,5,6,7,8,9
#Angeles Valadez Jonathan - 15211883
#Fecha: 10/5/2018
def suma9(suma9N):
    if len(suma9N) == 1:
        return suma9N[0]
    else:
        return suma9N[0] + suma9(suma9N[1:])

print(suma9([1,2,3,4,5,6,7,8,9]))
