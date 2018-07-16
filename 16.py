name=input('请输入您的名字')
print('编号    星座    日期')
print('1    水瓶    1月20～2月18')
print('2    双鱼    2月19～3月20')
print('3    白羊    3月21～4月19')
print('4    金牛    4月20～5月20')
print('5    双子    5月21～6月21')
print('6    巨蟹    6月22～7月22')
print('7    狮子    7月23～8月22')
print('8    处女    8月23～9月22')
print('9    天秤    9月23～10月23')
print('10   天蝎    10月24～11月22')
print('11   射手    11月23～12月21')
print('12   魔羯    12月22～1月19')
number=int(input('请根据如上提示选择对应编号（例如：水瓶座请输入：1）'))
if number==1:
    constellation='水瓶'
    date='1月20～2月18'
    nature='XXX'
if number==2:
    constellation='双鱼'
    date='2月19～3月20'
    nature='XXX'
if number==3:
    constellation='白羊'
    date='3月21～4月19'
    nature='XXX'
if number==4:
    constellation='金牛'
    date='4月20～5月20'
    nature='XXX'
if number==5:
    constellation='双子'
    date='5月21～6月21'
    nature='XXX'
if number==6:
    constellation='巨蟹'
    date='6月22～7月22'
    nature='XXX'
if number==7:
    constellation='狮子'
    date='7月23～8月22'
    nature='XXX'
if number==8:
    constellation='处女'
    date='8月23～9月22'
    nature='XXX'
if number==9:
    constellation='天秤'
    date='9月23～10月23'
    nature='XXX'
if number==10:
    constellation='天蝎'
    date='10月24～11月21'
    nature='XXX'
if number==11:
    constellation='射手'
    date='11月22～12月21'
    nature='XXX'
if number==12:
    constellation='魔羯'
    date='12月22～1月19'
    nature='XXX'
print('%s,您好！%s星座的您分析结果：日期是%s,性格是%s'%(name,constellation,date,nature))
