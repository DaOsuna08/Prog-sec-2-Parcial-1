#Ejerccio 1: Palabra Palíndromas

while True:
    pbra=list(input("Ingrese la palabra que desea evaluar, o ingrese 'stop' para detener el programa:\n"))
    pbra_eva=[]
    if "".join(pbra)=="stop":
        print("Adios")
        break
    else:
        for i in pbra:
            pbra_eva.insert(0,i)
        if pbra==pbra_eva:
            print("La palabra ingresada es palíndroma")
        else:
            print("La palabra ingresada no es palíndroma")