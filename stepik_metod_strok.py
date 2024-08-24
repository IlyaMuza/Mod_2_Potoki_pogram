a = 'jygvysdgvouygsdvjgsdvg SFGOGY'.lower()
b = ''
for j in 'e', 'y', 'u', 'i', 'o', 'a':
    a = a.replace(j, '')
#for i in range(0, len(a)):
#    b = b + '.' + a[i]
for i in range(0,len(a)):
    b = b + '.' + a[i]

print(b)
