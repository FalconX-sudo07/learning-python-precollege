def bubbleSort(A):
    for passnum in range(len(A)-1,0,-1):    #start,stop,step    
        for i in range(passnum):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
    return A
                
a = [10,14,12,200,6767,1,3]
temp = bubbleSort(a)
print(temp)