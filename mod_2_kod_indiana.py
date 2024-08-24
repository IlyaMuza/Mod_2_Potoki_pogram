chislo = int(input()) # получаем число
max_delitel = int(chislo/2) # максимально число делится на половину себя, на само себя - будет отдельно
perebor_deliteley = [] # сюда запишем все числа на которые будем пытаться делить наше число
code_ne_sortirovan = [] # сюда запишем все слагаемые наших делителей
code_itog = ''
for i in range(3,max_delitel+1):
    perebor_deliteley.append(i)
perebor_deliteley.append(chislo) # очевидно число должно делиться и на себя тоже
for i in perebor_deliteley: # находим все числа, на которые может делиться наше число
    if chislo % i == 0: # если число делится на i без остатка, то i - один из делителей числа
        for j in range(1,i//2+1): # раскладываем число на слагаемые
            a = j
            b = i - j
            if a != b: code_ne_sortirovan.append((a,b)) # заполняем наш несортированный список
print(code_ne_sortirovan)
n = 1
for i in code_ne_sortirovan:
    flaska = 0
    for j in range(n,len(code_ne_sortirovan)):
        if i[0] > code_ne_sortirovan[j][0] or (i[0] == code_ne_sortirovan[j][0] and i[1] > code_ne_sortirovan[j][1]):
            k = code_ne_sortirovan[j]
            code_ne_sortirovan[j] = i
            if flaska >= n-1:
                code_ne_sortirovan[flaska] = k
                flaska = j
            else:
                code_ne_sortirovan[n-1] = k
                flaska = j

    code_itog += str(code_ne_sortirovan[n-1][0])+str(code_ne_sortirovan[n-1][1])
    n += 1

print(code_itog)