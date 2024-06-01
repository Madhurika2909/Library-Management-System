L=["Sneha","Diya","Riya","Shreya","Tamashree"]
N=len(L)
for i in L:
    j = L.index(i)
    while (j>0):
        if(len(L[j-1])<len(L[j])):
            L[j-1],L[j]=L[j],L[j-1]
        else:
            break
        j = j-1
print(L)