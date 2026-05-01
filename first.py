a=47
b=97
c=a+b
print(a)
print(b)
print(c) 


n=10
print(id(n))


num1=4
num2=2
sum1=num1+num2

#print(f"{num1} and {num2} is equal {sum1}")
#print(f"{num1}+{num2}={sum1}")
print(num1,"+",num2,"=",sum1)

#multiply

multi=num1*num2
print(f"{num1} * {num2}={multi}")

#devide
divide=num2/num1
print(f"{num1} and  {num2}={divide}")

#power

power=num2**num1
print(f"{num1} and  {num2}={power}")  #kisi bhi velue ke power define karni ho to ** use karteb hai


#I/O : OPERATION
#by default input() return string type value.

##num1=input("enter your number1")
#num2=input("enter your number2")
#res=num1+num2
#print(res)         # isme ye values ko eak ke baad eak likh deta hai agar humko apne input ke according karna hai to aise karege




num1=int(input("enter your number1"))
num2=int(input("enter your number2"))
res=num1+num2
print(res)