#!/usr/bin/python3
#-*- coding:utf8 -*-
import random
class_dict={0:'吕浩亮',1:'陈禹兵',2:'柯鸿成',3:'黄辉',4:'柯康',5:'赵骏然',6:'郭飘',7:'严瑞哲',8:'徐佳伟',9:'方小静',10:'华豪',11:'彭文杰',12:'万华',13:'程明',14:'魏垚',15:'张一波',16:'刘洋华',17:'马勋',18:'吴文韬',19:'杨义龙',20:'范丽文',21:'林欢',22:'李行',23:'杨尚儒',24:'邓彭川',25:'周志勇',26:'张晶晶',27:'叶冲',28:'汪梦龙',29:'李论'}
xuehao=set()
# num=random.randint(0,29)
# name=class_dict[num]
num_peop=int(input('请输入要抽取的人数:'))
while 1:
    num=random.randint(0,29)
    xuehao.add(num)
    if len(xuehao) == num_peop:
        break
for x in xuehao:
    name=class_dict[x]
    print('%s恭喜你被抽中了'%(name))    
   

# print('%s恭喜你被抽中了'%(name))
