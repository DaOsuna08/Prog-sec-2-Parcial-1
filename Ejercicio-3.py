#Ejercicio 3:Codififcación y Decodificación con números primos

abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
abc_prim=[]
#se generan los numeros primos
lim_prim=0
prove=2

for i in range(3,105):
    divisor=2
    if lim_prim<25:
        while divisor<i:
            if i%divisor==0:
                break
            else:
                divisor+=1
                prove+=1
                if divisor==i-1:
                    abc_prim.append(i)
                    break
while True:
