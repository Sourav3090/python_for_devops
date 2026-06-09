#what is function in python.
#1. every function has their won purpose.
# 2. function is a block of insturction (code) which execute inside its own block.
#3. function is reusable means define one time use manytimes(dry).
#4.function has two main part first function defination second function calling.
#5. in python by default return none

#how define function in python.
def add():
    a=20
    b=10
    c=a+b
    print(c)
add()

#function devide into four categogy.
#1. take something return nothing.
#2.take nothing returm something.
#3.take something return nothing.    
#4.take something return something.

#parameters (para) and arguments (args).
#positional parameter/argusment'
#default parameter
def add(a,b):
    c=a+b
    print(c)
add (20,30)


def table_print(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
table_print(14)

table_print(18)

table_print(27)



def sub(a=0,b=0):
    print(a-b)

def add(a=0,b=0):
    print=(a+b)

def multi(a=0,b=0):
    print(a*b)

def div(a=0,b=0):
    print(a/b)
num1=int(input("enter number 1 :"))
num2=int(input("enter number 2 :"))
opt=input(" choose option : +,-,*,/, :")
if opt=="+":
    add()
elif opt=="-":
    sub()
elif opt=="*":
    multi()
elif opt=="/":
    div()
else:
    print("aandha hai kya lawduu")


def add(a,b):
    return a+b
res=add (10,30)

def sub (a,c):
    return a-c
print(sub(10-res))


def user_name(a):
    return a
g=greet("namaste")

def user_name(a):
    return a



