def show(n):
    if(n==-1):   #base case
        return

    print(n)
    show(n-1)
    
print(show(5))
 
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))

def nsum(n):
    if(n==1):
        return 1
    
    else:
        return n+nsum(n-1)
    
print(nsum(10))


def fibonacci(i):
    if(i <=1):
        return i
    else:
        return fibonacci(i-1)+fibonacci(i-2)


terms = int(input('enter no.terms in the fibonacci: '))

for i in range(0,terms+1):
    print(fibonacci(i))
