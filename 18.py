account='dst'
passwd='123456'
money=500
a=input('请输入帐号')
p=input('请输入密码')
if not (a==account and p== passwd):
    print('非法账户')
else:
    draw=int(input('请输入取款金额'))
    if money<draw:
        print('没钱取毛钱')
    else:
        print('您取了%d元，还剩%d元'%(draw,money-draw))
