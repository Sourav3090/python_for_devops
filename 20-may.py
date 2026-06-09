#wap to check number pass by argument is odd or even 
# def num(n):
#     if n%2 ==0:
#         print("it is even number ")
#     else:
#         print("it is odd number")
# num()


#waf to check which number is greater and two number bt user.

#waf to check the cherecter pass by user is vowel or consonant.
# def letter(char):
#     if char  in "aeiou":
#         print ("its a vowel")
#     else:
#         print("its a consonant")

# letter("b")

#waf to check completly divide by 2 and 3 and return 
#"yes number is completely divide"
#"no number is not completely divide"

# def check_num(n):
#     if n%2==0 and n%3==0:
#         return "yes number is com divide"
#     else:
#         return "no number is not comp devide"
# res=check_num(6)
# print(res)


#waf to return lenght of a string pass by user without using len().
def len_string(s):
    c=0
    for i in s:
        c=c+1
    return c
res=len_string("python")
print(res)