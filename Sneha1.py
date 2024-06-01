
def tupleFun():
    t = tuple()
    n = 10
    for i in range(n) :
        a = input("Print  data: ")
        t = t+(a,)
    print(type(t))
    print(t)

def BubbleSort():
    L = [49,71,6,12,71,25,2,0,7,1234]
    n = len(L)
    for i in range(n-1):
        for j in range(i+1,n):
            if (L[i] > L[j]):
                L[i],L[j] = L[j],L[i]
    print(L)           
    
def InsertionSort():
    L2 = [49,71,6,12,71,25,2,0,7,1234]
    
    for i in L2:
        j=L2.index(i)
        while (j>0):
            if (L2[j-1] >L2[j]):
                L2[j-1],L2[j] = L2[j],L2[j-1]
            else:
                break
            j=j-1
    print(L2)   

def SelectionSort():
    L3 = [49,71,6,12,71,25,2,0,7,1234]
    n = len(L3)
    for i in range(n-1):
        min = L3[i]
        P = i
        for j in range(i+1,n):
            if (L3[j] < min):
                min = L3[j]
                P = j;
        L3[i],L3[P] = L3[P],L3[i]
    print(L3)   

#tupleFun()
BubbleSort()
InsertionSort()
SelectionSort()