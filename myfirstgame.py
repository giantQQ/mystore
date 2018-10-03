import random
import sys
temp = input("猜猜我多大啦？")
guess = random.randint(0,10)
i=0
while i<3 :
    if(int(temp) == guess):
        print("哇塞你好牛逼啊\n")
        print("你是我肚子里的蛔虫嘛")
        break
    else :
        
        if(int(temp)>guess):
             temp = input("哎呀猜大啦，再试试看:\n")
        else :
             temp = input("哎呀猜small啦，再试试看:\n")
        i=i+1
print("不玩啦不玩啦")
print(len(sys.argv))
print(sys.argv[0])




            
