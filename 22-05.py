#waf to check givin how many vowel in a giving string.
# def vowel_count(a):
#     c=0
#     for i in a:
#         if i in "aeiou":
#            c+=1
#     return c
# res=vowel_count("souravsingh")
# print(res)

#local variable vs global variable
#name="sourav"              #global variable
# def msg():
#     name ="sourav"
#     print("inside:",name)
# msg()
# print("outside :",name)


#wap to coount char "p" in "python programming" return total occurence.
# def find(dest):
#     c=0
#     for i in dest:
#         if i in f:
#             c+=1
#     return c

# dest="python programming"
# f="p"
# res=find(dest,f)
# print(res)

## WAF (Write a Function) to return sum of string indexes

def sum_indexes(a):
    c = 0
    
    for i in range(len(a)):
        c=c+i
    
    return c 

# Example
text = "soura"

result = sum_indexes(text)

print("Sum of indexes =", result)