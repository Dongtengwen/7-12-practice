height=int(input('请输入身高(cm)'))
price=int(input('请输入身价'))
score=int(input('请输入颜值分'))
if height>180 and price>1000000 and score>99:
    print('高富帅')
elif price>1000000 and score>99:
    print('富帅')
elif score>99:
    print('帅')
elif price<100 and score<60 and height<160:
    print('矮穷挫')
else:
    print('你是个普通人')

