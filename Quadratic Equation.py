import math

def quadeq(a,b,c):
    D=(b**2)-4*a*c
    if(D<0):
        print("Undetermined")
        return
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    formatstr="roots are: %-15s,%-15s"
    print(formatstr % (x1,x2))
    
# Main Program
#p=float(input("Enter first coefficient: "))
#q=float(input("Enter second coefficient: "))
#r=float(input("Enter third coefficient: "))
#quadeq(p,q,r)
#book=''
a=int(input("input any no. from 1-5:  "))
if(a==1):
    book=str(input("input book title  "))
    query = "select *from MyBooks where Name =" + "'"  + book + "'"
elif(a==2):
    book=str(input("input book author  "))
    query = "select *from MyBooks where author = '"  + book + "'"
elif(a==3):
    book="three"
elif(a==4):
    book="four"
elif(a==5):
    book="five"
print(query)    
    