n=int(input("enter the number="))
def fibo(n):
    n1=0
    n2=1
    i=1
    while i<n+1:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        i=i+1
fibo(n)
