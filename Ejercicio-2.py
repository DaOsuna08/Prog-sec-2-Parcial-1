#Ejercicio 2:Verificar Anagramas
print("Ingrese 2 palabras para evaluar si son anagramas")
pbra_1_list=list(input("Primera palabra: "))
pbra_2_list=list(input("Segunda palabra: "))
letras_similares=0
pbra_1_str="".join(pbra_1_list)
pbra_2_str="".join(pbra_2_list)
if len(pbra_1_list)==len(pbra_2_list):
    for i in range(len(pbra_1_list)):
        for j in range(len(pbra_2_list)):
            if pbra_1_list[i]==pbra_2_list[j]:
                letras_similares+=1
    if letras_similares==len(pbra_1_list):
        print("Las palabras '{}' y '{}' si son anagramas.".format(pbra_1_str,pbra_2_str))
    elif letras_similares!=len(pbra_1_list):
        print("Las palabras '{}' y '{}' no son anagramas.".format(pbra_1_str,pbra_2_str))
else:
    print("Las palabras '{}' y '{}' no tienen la misma cantidad de letras, por lo tanto no son anagramas.".format(pbra_1_str,pbra_2_str))
