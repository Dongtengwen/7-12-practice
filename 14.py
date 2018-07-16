import random

ranGen=random.randint(1,10)
playerInput=int(input('请输入一个1到10之间的数字'))
if ranGen==playerInput:
    print('胜利')
else:
    print('失败，你是一个loser')

