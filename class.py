#type casting and type conversion
n=10
m=10.5
print(n+m)           #jo jada bada hoga wo own karega yaha float bada tha to ye float me convert hogya#
# number or string ko add karege to nahi ho naam naam ko add kar sakte hai number ko number ke sath jor sakte hai
num="100"
name="sourav"
print(num+" "+name)  #concatilization add 2 strings


#jo apne aap ho jaaye wo conversoin jo programmer kare force fully casting
#type casting
var1=1000
print(type(var1))

var1=float(1000)
print(type(var1))
print(var1)
#forcefully int ko float me convert kiya isko type casting bolte hai

sum1="sourav"
print(type(sum1))

num1=50
num2=12000
print(num1+num2)

num1="50"
num2="51"
res=int(num1)+int(num2)
print(res)
print(type(res))

num1=50
num2=20
print(type(num1),type(num2))
res=str(num1)+str(num2)
print(res)
print(type(res))

num1=50.25
num2=25.36
res=int(num1)+int(num2)
print(res)