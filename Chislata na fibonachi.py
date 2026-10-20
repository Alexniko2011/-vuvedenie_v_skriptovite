n=int(input("kolko chisla iskash ot fibonachi: "))
a=1
b=1
print(a)
print(b)
i=3
while(i<=n):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1