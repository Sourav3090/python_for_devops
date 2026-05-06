#identity opr
a=10
b=10
print(id(a))
print(id(b))
print (a is b)     #jab tak address same aayega tab tak true aata rahega.


#conditional statement

a=0
if a:
    print("yes")
else:
    print("no")


#wap to check number give by user in odd or even number
num=23
if num % 2 == 0:
    print("Even")
else:
    print("false")




#wap to print the last digit of and number is 456735
print(456735%10000)    #if you want last digits of the value the use % and 10,100,1000,10000,100000. its depends on you tumhe
#jitne number chahiye utna zero laga do.



num1=3
num2=9
num3=12

#wap to find largest 
#wap to find smallest



num1=3
num2=9
num3=12

num1 = 3
num2 = 9
num3 = 12

# Find largest

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is greatest")

if num2>=num1 and num2>=num3:
    print(f"{num2} is greatest")

if num3>=num2 and num3>=num1:
    print(f"{num3} is greatest")



if num1 <= num2 and num1 <= num3:
    print(f"{num1} is smallest")

if num2<=num1 and num2<=num3:
    print(f"{num2} is smallest")

if num3<=num2 and num3<=num1:
    print(f"{num3} is smallest")



#conditional stattement:
# if else













n=100
if n>50:
    print("yes1")

elif n>60:
    print("yes2")

elif n>70:
    print("yes3")