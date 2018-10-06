#Estructura de Datos que lleve el control de las diferentes versiones
#de un proyecto de una empresa
#Angeles Valadez Jonathan - 15211883
#Fecha: 10/5/2018
class empresa:
    def __init__(self):
        self.migraciones = []

    def agregarMigra(self,item):
        item = input("Introduzca el nuevo nombre de la version del proyecto: ")
        self.migraciones.append(item)
        print(" ")

    def sacarmigra(self):
        ultimamigracion = len(self.migraciones)
        print(self.migraciones.pop(ultimamigracion-1))
        print(" ")

    def peekMigra(self):
        mtotales = len(self.migraciones)
        ultimamigracion = len(self.migraciones)
        print("--------- Menu revisar versiones ------------")
        print("Ver todas las migraciones: 1")
        print("Ver la ultima migracion hecha: 2")
        print("----------------------------------------------")
        print("La cantidad de migraciones existentes son: " + str(mtotales))
        print(" ")
        opcion = input("Que desea realizar?: ")

        if(opcion == "1"):
            print(" ")
            print("------ Versiones ------")
            if (mtotales == 0):
                print("No existen versiones!!")
                print(" ")
            
            for index in reversed(self.migraciones):
                print(index)
            
            
        elif(opcion == "2"):
            print("------ Ultima version ------")
            if (mtotales == 0):
                print("No existen versiones!!")
                print(" ")
            version = self.migraciones[ultimamigracion-1]
            print(str(version))
            print(" ")
        
e = empresa()
class Menu:
    while True:
        print("----------- Menu de opciones -----------")
        print("Agregar una version: 1")
        print("Revisar versiones: 2")
        print("Sacar la ultima version: 3")
        print("Salir: 4")
        print(" ")
        opcion = input("Que desea realizar?: ")
        print(" ")

        if(opcion == "1"):
            e.agregarMigra(0)
            
        elif(opcion == "2"):
            e.peekMigra()

        elif(opcion == "3"):
            e.sacarmigra()
        
        elif(opcion == "4"):
            break
