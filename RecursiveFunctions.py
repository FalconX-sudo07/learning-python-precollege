# the most simplest recursive function
def shortest():
    shortest()
    
shortest()

#
def shortestWithBaseCase(makeRecursiveCall):
    print('shortestWithBaseCase(%s) called.'%makeRecursiveCall)
    if not makeRecursiveCall:
        # BASE CASE
        print('Returning from base case')
        return
    else:
        # RECURSIVE CASE
        shortestWithBaseCase(False)
        print('Returning from recursive case.')
        return
print('Calling shortestWithBaseCase(False):')
shortestWithBaseCase(False)     #returns code from 'if not makeRecursiveCall:' since makeRecursiveCall is called false
print()
print('Calling shortestWithBaseCase(True):')
shortestWithBaseCase(True)

#countDownAndUp example
def countDownAndUp(number):
    print(number)
    if number == 0:
        #BASE CASE
        print('Reached the base case.')    
    else:
        #RECURSIVE CASE
        countDownAndUp(number-1)
        print(number,'returning')
        return
countDownAndUp(3)

#The Iterative Factorial Algorithm
def factorial(number):
    product = 1
    for i in range(1,number+1):
        product = product * i
    return product
print(factorial(5))

#The Recursive Factorial Algorithm
def factorial(number):
    if number == 1:
        #BASE CASE
        return 1
    else:
        #RECURSIVE CASE
        return number*factorial(number-1)
print(factorial(997))

#The Iterative Fibonacci Algorithm
def fibonacci(number):
    a,b = 1,1
    print('a=%s,b=%s'%(a,b))
    for i in range(1,number):
        a,b = b,a+b
    return a
print(fibonacci(10)) 

# The Recursive Fibonacci Algorithm
def fibonacci(number):
    print('fibonacci(%s) returning 1.'%(number))
    if number == 1 or number == 2:
        print('Call to fibonacci(%s) returning 1.'%(number))
        return 1
    else:
        #RECURSIVE CASE
        print('calling fibonacci(%s) and fibonacci(%s).'%(number-1,number-2))
        result = fibonacci(number - 1) + fibonacci(number - 2)
        print('Call to fibonacci(%s) returning %s.' % (number, result))
        return result
    print(fibonacci(10))

#The Iterative Exponential Algorithm
def exponentByIteration(a,n):
    result = 1
    for i in range(n):
        result*=a
    return result
print(exponentByIteration(3,6))

#The Recursive Exponential Algorithm
def exponentByRecursion(a,n):
    if n==1:
        #BASE CASE
        return a
    elif n%2==0:
        #RECURSIVE CASE WHEN n IS EVEN
        result = exponentByRecursion(a,n//2)
        return result*result
    elif n%2==1:
        #RECURSIVE CASE WHEN n IS ODD
        result = exponentByRecursion(a,n//2)
        return result*result*a    
print(exponentByRecursion(3,6))
print(exponentByRecursion(2,9))

# Summing Numbers in an Array
def sum(numbers):
    if len(numbers)==0:
        #BASE CASE
        return 0
    else:
        #RECURSIVE CASE
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)
print(sum([2,3,4,5,6]))

# Reversing a String
def rev(theString):
    if len(theString) == 0 or len(theString) == 1:
        #BASE CASE
        return theString
    else:
        #RECURSIVE CASE
        head = theString[0]
        tail = theString[1:]
        return rev(tail)+head
print(rev('abcdef'))

# Detecting Palindromes
def isPalindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        #BASE CASE
        return True
    else:
        head = theString[0]
        middle = theString[1:-1] #imp here, -1 means until the -1th element where its not included
        last = theString[-1]
        # if head == last:
        #     isPalindrome(middle)
        #     return True           this is wrong, since this line is directly taken and the above line is not considered. so,
        if head ==last:
            return isPalindrome(middle)
        else:
            return False
        # return head == last and isPalindrome(middle)  a more advanced way of writing that above thing
text = 'abcda'
print(isPalindrome(text))

# Solving the Tower of Hanoi
