import math
segundo=input("Introduce el numero x²:")
primer=input("Introduce el numero :")
zero=input("Introduce el numero normal:")
num_raiz=(math.pow(int(primer), 2)-4*int(segundo)*int(zero))
raiz=math.sqrt(num_raiz)
abajo=2*int(segundo)
resul=((-int(primer)+raiz)/abajo)
resul_n=((-int(primer)-raiz)/abajo)


print("Resultado positivo: ", resul)
print("Resultado negativo: ", resul_n)
