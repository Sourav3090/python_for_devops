#wap to takes  start point and end point form user input and print all number divisble by 2 and 3.

start_num=int(input("ENTER YOUR NUMBER :"))
end_num=int(input("ENTER YOUR NUMBER :"))

for i in range(start_num, end_num):
    if i%2 == 0 and i%3 ==0:
        print(f"ALL NUMBER ARE DIVISBLE BY 2 & 3:{i}")
    