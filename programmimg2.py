L=["Sneha","Diya","Riya","Shreya","Tamashree"]
N=len(L)
for i in range(0,N):
    for j in range(0,N-i-1):
        if(len(L[j])>len(L[j+1])):
            L[j],L[j+1]=L[j+1],L[j]
print(L)