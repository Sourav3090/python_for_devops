#use condication statement for making intelligence the programe
#name="sourav"
#if name:
 #   print(f"yes name {name} is provided")
  #  address="Noida"
  #  if address:
   #     print(f"yes address is : {address} provided")
   # else:
   #     print("address is not provided")

#else:
 #   print("name is note provided")




#num1=20
#if num1%2==0:
 #   print("even")
  #  mob=input("emter your number")
   # if len(mob) == 10









student_name=input("enter your name")
pre=int(input("enter your pre markes"))
if pre >= 400:
    print("your are pass in pre and eligble for main")
    mains = int(input("enter your mains marks"))
    if mains >= 600:
        print("your are pass in mains and eligble for interview")

        inter=int(input("enter your interview markes  : "))
        if inter >= 700:
            print(f"you are selected as ias mr {student_name}")
        else:
            print(f"you are fail in interview mr {student_name}")

            
    else:
        print("fail in mains")
else:
    print("better luck next time,pre failed🙈🙈🙈🙈")


