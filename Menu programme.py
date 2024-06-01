Employee=[]

def Add():
    EmpD={}
    EmpD["Empid"]=int(input("Enter id: "))
    EmpD["Name"]=input("Enter Name: ")
    EmpD["Department"]=input("Enter Department: ")
    EmpD["Salary"]=int(input("Enter Salary: "))
    EmpD["Designation"]=input("Enter Designation: ")
    Employee.append(EmpD)

def Display():
    for i in Employee:
        print("Empid: ",i["Empid"],"Name: ",i["Name"],"Department: ",i["Department"],"Salary: ",i["Salary"],
              "Designation: ",i["Designation"])

def Search():
    cmd=[
        "1=>Search by id",
        "2=>Search by Name"
        ]
    for i in cmd:
        print(i)
    inp1=int(input("Select from menu "))
    if(inp1==1):
        id=int(input("enter the id: "))
        for i in Employee:
            if(i["Empid"]==id):
                print("Empid: ",i["Empid"],"Name: ",i["Name"],i["Department"],i["Salary"],i["Designation"])
                break
    if(inp1==2):
        Name=input("enter the Name ")
        for i in Employee:
            if(i["Name"]==Name):
                print("Empid: ",i["Empid"],"Name: ",i["Name"],"Department: ",i["Department"],"Salary: ",i["Salary"],
                      "Designation: ",i["Designation"])
                break
def Update():
    inp2=int(input("Enter the id: "))
    for i in Employee:
        if(i["Empid"]==inp2):  
            i["Empid"]=int(input("Enter id: "))
            i["Name"]=input("Enter Name: ")
            i["Department"]=input("Enter Department: ")
            i["Salary"]=int(input("Enter Salary: "))
            i["Designation"]=input("Enter Designation: ") 
            break

def Delete():
    inp3=int(input("Enter the id:"))
    for i in Employee:
        if(i["Empid"]==inp3): 
            Employee.remove(i)
            break
    
    
def Menu():
    Commands=[
       "1=>Add an employee detail",
       "2=>Display Employee details",
       "3=>Search the employee detail",
       "4=>Update Employee detail",
       "5=>Delete a Record",
       "6=>Exit"
       ]
    for i in Commands:
        print(i)
    ip=int(input("Select from menu: "))
    return ip

inp=Menu() 

while(1):
    if(inp==1):
        Add()
    elif(inp==2):
        Display()
    elif(inp==3):
        Search()
    elif(inp==4):
        Update()
    elif(inp==5):
        Delete()
    elif(inp==6):
        break
    else:
        print("wrong input")
    inp=Menu()
print("Bye")