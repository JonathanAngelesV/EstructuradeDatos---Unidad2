#Silumacion de una cola de clientes en una tienda donde solamente existe 1 caja
#Angeles Valadez Jonathan - 15211883
#Fecha: 10/5/2018
class tienda:
    def __init__(self):
        self.fila = ["Vacio","Vacio","Vacio","Vacio","Vacio"]
        
    def hacerfila(self,item):
        espera = len(self.fila)-1
        while espera >= 0:
            
            if self.fila[espera] == "Vacio":
                self.fila.pop(espera)
                item = input("Introduzca el nombre del cliente: ")
                self.fila.insert(espera,item)
                espera = espera-1
                break
            
            elif self.fila[0] != "Vacio":
                print("------LA FILA ESTA LLENA!!!------")
                break
            espera = espera-1
            
    def atender(self):
        espera = len(self.fila)-1
        while espera >= 0:
            
            if self.fila[espera] != "Vacio":
                self.fila.pop(espera)
                self.fila.insert(espera, "Vacio")
                while espera >= 0:
                    indiceant = espera -1
                    if indiceant > 0:
                        sigelemento = self.fila[indiceant]
                        self.fila.pop(espera)
                        self.fila.insert(espera,sigelemento)
                    else:
                        self.fila.pop(espera)
                        self.fila.insert(espera,"Vacio")
                    espera = espera - 1
                break
            
            elif self.fila[4] == "Vacio":
                print("------LA FILA ESTA VACIA!!!------")
                break
            espera = espera-1
            
    def mostrarfila(self):
        for clientes in self.fila:
            print(clientes)
t = tienda()

class Clientes:
    
    while True:
        print("")
        print("Clientes actuales")
        print(t.mostrarfila())
        print("---Menu---")
        print("Hacer Fila: 1")
        print("Atender: 2")
        print("Renunciar y dejar la tienda: 3")
        opcion = input("Que desea realizar?: ")
        if opcion == "1":
            t.hacerfila(0)
        elif opcion == "2":
            t.atender()
        elif opcion == "3":
            break
