X=int(input("Enter a no.:" ))
L=[]
while(X!=0):
    R=X%10
    X=X//10
    L.append(R)
y=len(L)
S=""
for i in range(y-1,-1,-1):
    var=L[i]
    if(var==1):
        S=S+"one "
    elif(var==2):
        S=S+"two "
    elif(var==3):
        S=S+"three "
    elif(var==4):
        S=S+"four "
    elif(var==5):
        S=S+"five "
    elif(var==6):
        S=S+"six "
    elif(var==7):
        S=S+"seven "
    elif(var==8):
        S=S+"eight "
    elif(var==9):
        S=S+"nine "
    elif(var==0):
        S=S+"zero "
print("\"",S,"\"")