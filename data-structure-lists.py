#data strecture.
#data structure use to store data effeciently and make faster.
#for operations like read and write.
#list    list()
#string  str()
#dictionary dict()
#set    set()
#tuple   tuple()


# list
#list is a data strecture in python used to store multiple data in of different types in one variable.

#list can define by using square [],and data inside knows as element.

#list can be hetrogenous and homogenous.

#list are muteable (changeable)

#list supporat indexing, slicing and follows oredering seruence.


#total index  = lenght -1.



# marks_10th=[20,55,60,76,50,60,"hello",5.5]    #list ke andar ke data ko element bolte hai.
# print("before update : ", marks_10th)
# marks_10th[-2]=150
# #i=marks_10th[0]
# print("after update : ", marks_10th)

#1.list and its property
#2. creation of list
#3.updation of list
#4. indexing
#5.slicing
#6traversing
#7.in-built methods
#8.test
#9.assignments.



#slicing
# marks=[10,20,30,40,50,60,70,80]
# #[start-0:stop-1:step-1]
# sub_list=marks[::-1]
# print(sub_list)

#6. traversing.
# marks=[10,20,30,40,50,60,70,80]
# for i in range(len(marks)):
#     print(i)


# marks=[10,11,20,31,30,33,40,55,50,60,70,80]
# for i in marks:
#     if i%2==0:
#         print(f"this elm is even :{i}")
#     else:
#         print(f"this elm is odd : {i}")



marks=[10,20,30,40,50,60]
total=0
for i in marks:
    total=total+i
print(total)


# marks=[10,20,30,40,50,60,70,80,90,100]
# sub_list=marks[:3:-1]
# print(sub_list)




