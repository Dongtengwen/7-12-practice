print('欢迎使用10086自助查询系统！')
print('余额查询请按1,流量查询请按2,通话时间查询请按3')
userInput=int(input())
balance=10
flow=1.58
timeRemain=150
if userInput==1:
    print('您当前的余额是%d元'%balance)
elif userInput==2:
    print('您流量剩余%.2fG'%flow)
elif userInput==3:
    print('您的通话时长剩余%d分钟'%timeRemain)
else:
    print('请按提示输入1,2或者3')

