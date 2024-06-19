s1 = input('Ingrese cadena:')
s2 = s1.replace(' ','')
dic = {}
for i in range(len(s2)):
    letra = s2[i]
    if letra in dic:
        dic[letra] += 1
    else:
        dic[letra] = 1

print('Análisis:','\'',s1,'\'')
for key in dic:
    print(key,'->',dic[key])

#resultado
'''Análisis: 'abc aac ede eea cba '
a -> 5
b -> 2
c -> 3
e -> 4
d -> 1
'''

#----------------------------------------

valores = input('Ingrese cadena:')
lst_valores = valores.split(' ')
lst_claves = [i for i in range(len(lst_valores))]
dic1 = dict(zip(lst_claves, lst_valores))
dic2 = {}
for key, value in dic1.items():
    if not value in dic2.values():
        dic2[key] = value

print(dic1)
print(dic2)


