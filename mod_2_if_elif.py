a,b,c = map(int,input().split())
if a==b and b==c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)