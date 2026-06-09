#wap to calculATE  the space in this programme
# c=0
# a= "This is python"
# for i in a:
#     if i == " ":
#         c+=1
# print(c)


#wap to swap the first  value of list with last value of list'
# my_list=[10,11,20,31,30,33,40,55,50,60,70,80]
# elm1=my_list[0]
# last_elm=my_list[-1]
# my_list[-1]=elm1
# my_list[0]=last_elm

# print(my_list)

#wap to find the sum of all elements in the list 
# my_list=[10,20,30,40,50]
# print(sum(my_list))

#wap to find the sum of only even element in the list :[10,3,4,6,22,31,33,55,40]
# my_list=[10,3,4,6,22,31,33,55,40]
# total=0
# for i in my_list:
#     if i%2==0:
#         total=total+i
# print(total)
#wap to find the sum of only odd elements in the list ;[10,3,4,6,22,31,33.35,55,40]
my_list=[10,3,4,6,22,31,33,35,55,40]
total=0
for i in my_list:
    if i%2!=0:
        total=total+i
print(total)
#wap to find the count of how many int values and how many str in the list [70,"aman",50,10,30,"rohan","iq-india"].
list = [70, "aman", 50, 10, 30, "rohan", "iq-india"]

int_count = 0
str_count = 0

for item in list:
    if isinstance(item, int):
        int_count += 1
    elif isinstance(item, str):
        str_count += 1

print("Integer values:", int_count)
print("String values:", str_count)
