#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-l
phone_info = [
{'name':'vivox9', 'price':'1200', 'count':'30'},
 {'name':'iphone6', 'price':'2000', 'count':'55'},
{'name':'iphone6s', 'price':'2200', 'count':'120'},
{'name':'iphone7', 'price':'4000', 'count':'80'},
{'name':'iphone7s', 'price':'4200', 'count':'90'},
 {'name':'iphone8', 'price':'5200', 'count':'70'}
]
# 查看所有品牌的函数
# 设置一个形参is_detail.如果is_detaik的值为True，查询手机详细信息。如果值为Flase，查询简要信息
def select_all_phone(is_detail):
    for x in range(0,len(phone_info)):
        # 取出每一个字典
        phone_dict=phone_info[x]
        #is_detail是True，则查询信息详情(手机品牌，价格，库存)
        if is_detail==True:
            print('{0}.品牌{1}，价格{2},库存{3}'.format(x+1,phone_dict['name'],phone_dict['price'],phone_dict['count']))
        #如果is_detail不是True，那就是Flash，查询简要信息（手机品牌）
        else:
            print('{0}.品牌{1}'.format(x+1,phone_dict['name']))
# 定义查看某个品牌的详细信息或返回一个函数
def date_info_or_back():
    print('1-根据产品序号查看手机详细信息')
    print('2-返回')
    # 根据控制台输入的数字，来进行判断运行哪个选项
    select_operation=int(input('请输入你要操作的序号:'))
    # 循环检测用户输入的序号是否符合要求
    while select_operation!=1 and select_operation!=2:
        select_operation=int(input('输入有误，请重新输入你要操作的序号：'))
    # 如果用户输入的序号为1，则运行第一个功能选项
    if select_operation==1:
        select_all_phone(False)
        select_number=int(input('请输入要查询的手机详细信息的手机品牌序号：'))
        # 循环检测用户输入的手机品牌序号是否正确
        while select_number<1 or select_number>len(phone_info):
            select_number=int(input('输入序号有误，请重新输入要查询的手机详细信息的:手机品牌序号'))
        phone_dict=phone_info[select_number-1]
        print('{0}:品牌{1}，价格{2}，库存{3}'.format(select_number,phone_dict['name'],phone_dict['price'],phone_dict['count']))
        # 函数里面嵌套函数，因为用户选择序号1时，下面还有购买或者返回的操作，把购买和返回的操作单独进行
        buy_or_back(phone_dict)
    # 如果选择的不是序号1，那么就是序号2，返回。
    else:
        return
def buy_or_back(phone_dict):
    print("1_购买")
    print("2_返回")
    select_number=int(input("请选择要操作的编号:"))
    while select_number!=1 and select_number!=2:
        select_number=input("选择有误,请输入正确的选择")
    #选择1说明用户要购买手机
    if select_number==1:
        total_count=int(phone_dict["count"])
        print(f"当前库存{total_count}台")
        buy_count=int(input("请输入要购买的台数"))
        while buy_count<=0 or buy_count>int(phone_dict["count"]):
            buy_count=int(input("请重新输入要购买的数量:"))
        surplus_count=total_count-buy_count
        phone_dict["count"]=str(surplus_count)
        if int(phone_dict["count"])==0:
            phone_info.remove(phone_dict)
        print("购买成功!")
    else:
        return
def add_or_update_phone_info():
    print('1-添加新产品')
    print('2-修改原有产品')
    select_number=int(input('请输入要选择的序号：'))
    while select_number!=1 and select_number!=2:
        select_number=int(input('输入错误，请重新输入要选择的序号：'))
    if select_number==1:
        new_phone_name=input('请输入新产品名称：')
        new_phone_price=input('请输入新产品价格：')
        new_phone_count=input('请输入新产品库存：')
        new_phone_dict={'name':new_phone_name,'price':new_phone_price,'count':new_phone_count}
        phone_info.append(new_phone_dict)
    else:
        #调用selected_all_phone函数,参数设置为T.将所有手机详情信息全部打印出来,用户再根据对应的编号
        select_all_phone(True)
        print('1-根据产品序号修改产品信息')
        print('2-返回')
        select_number=int(input('请输入你要操作的序号：'))
        while select_number!=1 and select_number!=2:
            select_number=int(input('输入的序号有误，请重新输入要操作的序号：'))
        if select_number==1:
            phone_num=int(input('请输入要修改的手机序号：'))
            while phone_num <1 or phone_num>len(phone_info):
                phone_num=int(input('手机输入错误，请重新输入要修改的手机序号：'))
            update_dict = phone_info[phone_num - 1]
            update_name = input('请输入修改的名称：')
            update_price = input('请输入修改的价格：')
            update_count = input('请输入修改的库存：')
            update_dict['name'] = update_name
            update_dict['price'] = update_price
            update_dict['count'] = update_count
            print('修改成功！')
        else:
            return
def dele():
    print("1-根据索引删除元素")
    print("2-删除所有")
    select=int(input("请输入选项"))
    while select!=1 and select!=2:
        select=int(input("输入无效,请输入有效选项"))
    if select==1:
        select_all_phone(True)
        select_del=int(input("请输入要删除产品的序号"))
        while select_del<1 or select_del>len(phone_info):
            select_del=int(input("请输入有效序号"))
        del phone_info[select_del-1]
    else:
        phone_info.clear()
while True:
    print("1-查看产品\n2-增添和修改产品信息\n3-删除产品信息\n4-结束程序")
    select=int(input("请输入选项"))
    while select<0 and select>3:
        select=int(input("请输入有效选项"))
    if select==1:
        if phone_info==[]:
            break
        else:
            date_info_or_back()
    elif select==2:
        add_or_update_phone_info()
    elif select==3:
        dele()
    else:
        print("感谢使用,下次再回")
        break






