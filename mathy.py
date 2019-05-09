import math
responses=["Welcome To This Smart Calculator","My Name is Smarty Calculator Call Me 'MUNNA'","Thanks For Using Me","Sorry,This Is Beyond My Ability"]
def numberExtractor(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def LCM(a,b):
    L=a if a>b else b
    while(L<=a*b):
        if(L%a==0 and L%b==0):
            return int(L)
        L+=1
def Factorial(a,b):
    return (math.factorial(int(a)))
def HCF(a,b):
    return(math.gcd(int(a),int(b)))
def Add(a,b):
    return(a+b)
def Sub(a,b):
    return(a-b)
def Multiply(a,b):
    return(a*b)
def Division(a,b):
    return(a/b)
def end():
    print(responses[2])
    input("Enter any Key To Exit")
    exit()
def Sorry():
    print(responses[3])
def myName():
    print(responses[1])
operations={"PLUS":Add,"FACTORIAL":Factorial,"+":Add,"-":Sub,"/":Division,"*":Multiply,"SUM":Add,"ADDITION":Add,"ADD":Add,"SUBSTRACTION":Sub,"MINUS":Sub,"MULTIPLY":Multiply,"MULTIPLICATION":Multiply,"DIVISION":Division,"DIVIDE":Division,"LCM":LCM,"HCF":HCF}
commands={"NAME":myName,"EXIT":end,"END":end,"CLOSE":end}


