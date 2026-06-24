emp_list=[]
for i in range(1,11):
    emp_list.append(i)
print(emp_list)

print([i for i in range(1,11)])

print([i if i%2==0 else 1 for i in range(1,11)])

print([str(i)+"EVEN" if i%2==0 else "ODD" for i in range(1,11)])


emp_name=["aman", "SHIVAM", "shubham"]
res=[n.lower() for n in emp_name]
res=[n.upper() for n in emp_name]
res=["-".join(n) for n in emp_name]
print(res)



fruit_list=["apple","mango","papaya","banana","oranges","grapes"]
user="p"
res=[i for i in fruit_list if user in i]
print(res)

res=[i.upper() for i in fruit_list if user in i]
print(res)



#wap to check odd_even number.
def odd_even(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

odd_even(1548745)





res=lambda x,y : x*y
print(res(10,20))