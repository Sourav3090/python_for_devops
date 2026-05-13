#wap to sum of the indices of a string : "python"
#wap to print the factorial from 1 to 8.
#wap to print only prime number from 1 to 15.

# s=0
# size=(len("python"))
# for i in range (size):
#     s= s + i
#     print(s)




# num=1
# for i in range (1 , 9):
#     num = num*i
#     print(f"factorial of{i} = {num}")


# for i in range (1 , 15):
#     if i % i ==0 and i % 2 != 0:
#         print(i) 



for num in range (1 ,16):

    if num > 1:
        for i in range (2, num): 
            if num % i == 0:
                break
        else:
            print(num)

####


