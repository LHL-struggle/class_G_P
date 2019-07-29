# 员工猜奖程序
import os
import random
'''
os.path.join(path,name)        # 连接路径和文件名
os.path.split()                # 返回路径的目录和文件名，输出格式为元组
os.path.realpath(__file__)     # 获取真实路径；其他文件调用时，仍是取这个路径，不会发生变化
str(dict)          #   将字典转换为字符串
eval(str)          #   将字符串转换为字典
'''

# 保存文件的路径及文件
path_names = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'names.txt')

# 写入函数
def write_in():
    f = open(path_names, 'w')
    f.write(str(dict))
    f.close()

# 读取函数
def read_out():
    f = open(path_names, 'r')
    dict_0 = eval(f.read())
    f.close()
    return dict_0

# 抽奖函数
def cj():
    keys_list = []
    xuehao = set()   # 集合无序，不重复的元素序列
    # 输入判断函数
    while 1:
            try:
                num_peop = int(input('请输入要抽取的人数:'))
            except:
                print('请输入数字:')
            else:
                if num_peop > len(dict):
                    print('请输入%s以内的数字' % (len(dict)))
                if num_peop <= len(dict):
                    break
    # 抽奖人数
    while 1:
        num = random.randint(0, len(dict)-1)
        xuehao.add(num)
        if len(xuehao) == num_peop:
            break
    # 存放字典所有 键的列表
    for y in dict.keys():
        keys_list.append(y)
    print(keys_list)
    return xuehao,keys_list

# 保存并退出
def save_quit():
    # 将字典信息保存到，文件中
    write_in()
    # 查看文件中的信息
    print(read_out())
    x = int(input('继续录入，还是退出到主页面，按0退到主页面：'))
    if x == 0:
        print('你已进入')
        return True

    # 创建文件夹

f = open(path_names ,'a')
f.close()
# 读取文件内容
dict = read_out()
print(dict.keys())

print('%s\n%s\n%s\n%s\n%s' % ('功能选择:', '0结束程序', '1添加公司员工', '2删除公司员工', '3进入抽奖模式'))
while 1:
    gn = int(input('请输入选择的功能：'))

    # 功能选择 添加员工信息
    if gn == 1:
        while 1:
            # 输入员工编号
            while 1:
                try:
                    empno = int(input('请输入员工编号:'))      # 员工编号
                except:
                    print('请输入数字编号:')
                else:
                    if empno in dict.keys():
                        print('编号已存在，请重新输入:')
                    else:
                        break
            # 录入员工信息，到字典
            # dict[empno] = [input('姓名:'), input('性别:'), input('年龄:'), input('身高:')]
            dict[empno] = [input('姓名:')]
            if save_quit():
               break

    # 功能选择 删除员工信息
    if gn == 2:
        # 输入员工编号
        while 1:
            try:
                empno = int(input('请输入要删除的员工编号:'))  # 员工编号
            except:
                print('请输入数字编号:')
            else:
                if empno in dict.keys():
                    del dict[empno]
                    if save_quit():
                        break
                else:
                    break

    # 功能选择 员工抽奖模式
    if gn == 3:
        print('**********进入抽奖模式**********\n'' 一等奖设置请按:1\n', '二等奖设置请按:2\n', '三等奖设置请按:3\n', '退出抽奖请按:0')
        while 1:

            # 抽奖模式
            c = int(input('请选择抽奖模式：'))
            if c == 1:
                print('*****进入一等奖抽取模式***')
                xuehao, keys_list = cj()
                # 输出
                for x in xuehao:
                    name = dict[keys_list[x]]
                    print('%s 恭喜你中奖了' % (name))
                    del dict[keys_list[x]]
                print('剩余抽奖人数：%s' % (len(dict)))

            if c == 2:
                print('*****进入二等奖抽取模式***')
                xuehao, keys_list = cj()
                # 输出
                for x in xuehao:
                    name = dict[keys_list[x]]
                    print('%s 恭喜你中奖了' % (name))
                    del dict[keys_list[x]]
                print('剩余抽奖人数：%s' % (len(dict)))

            if c == 3:
                print('*****进入三等奖抽取模式***')
                xuehao, keys_list = cj()
                # 输出
                for x in xuehao:
                    name = dict[keys_list[x]]
                    print('%s 恭喜你中奖了' % (name))
                    del dict[keys_list[x]]
                print('剩余抽奖人数：%s' %(len(dict)))
            if c == 0:
                break
        # 因为在抽奖的时候，改变了dict的值 所以恢复他
        dict = read_out()

    # 结束程序
    if gn == 0:
        break


