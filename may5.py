#1.arthmatic operators
#2.assignment operators
#3.comparision/relation operators
#4.logical operators
#5.membership operators
#6.identity operators
#7.bit wise operators

 
# membership opr
#str1="thisn is python for devops"
#find="this"
#print(find in str1)


#num1="4567"    #ye number ke liye kaam nahi karta hai iss liye isko string banana padta hai
#print ("4"in num1)

#email="souravsingh@gmail.com"
#find="#"
#print(find in email)


 #   email="abc@gmail.com"
  #  if "@gmail.com" in email:
   #     print("valid google mail ID")
    #else:
   #     print("invalid Email")





#user is eligble for votimg
min_age=18
nationality="INDIAN"
user_age=int(input("enter your age :"))
user_id=input("enter your identity (ex.INDIAN) :")
if user_age >= min_age and user_id==nationality:
    print("user is eligible for voting")
else:
    print("user is not eligible for voting")    
        