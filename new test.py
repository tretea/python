menu="0.退出 1.添加 2.查看 3.更改 4.删除"
all_information={"小叶子":123456,"大周宝":123456,"小叶子爱喝粥":123456}
def add_information():
    user_name = input("请输入用户名:")
    while user_name in all_information.keys():
        user_name=input("用户名重复,请重新输入")
    user_password=input("请输入密码:")
    user_qpssword=input("请输入确认密码:")
    while user_qpssword!=user_password:
        user_qpssword=input("两次密码不同,请重新输入:")
    all_information[user_name]=user_password
    print("-"*30+"添加成功"+"-"*30)
def examine():
    print("1.根据用户名查看信息\n2.查看所有信息")
    select=input("请输入选项")
    while select!="1" and select!="2":
        select=input("选项有误,请重新输入")
    if select=="1":
        keys=all_information.keys()
        key=input("请输入用户名:")
        while key not in keys:
            select=input("该用户未被注册,请选择1.注册 2.重新输入用户名")
            while select != "1" and select != "2":
                select = input("选项有误,请重新输入")
            if select=="1":
                add_information()
                break
            else:
                key=input("请再次输入用户名")
        for index,x in all_information.items():
            if key==index:
                print(f"该用户的密码为:{x}")
    else:
        for index,x in all_information.items():
            print(f"用户名:{index} 密码:{x}")
def change():
    examine()
    keys = all_information.keys()
    key = input("请输入用户名:")
    while key not in keys:
        select = input("该用户未被注册,请选择1.注册 2.重新输入用户名")
        while select != "1" and select != "2":
            select = input("选项有误,请重新输入")
        if select == "1":
            add_information()
            break
        else:
            key = input("请再次输入用户名")
    all_information[key] = input("请输入修改后的密码:")
    print("-"*30+"修改成功"+"-"*30)
def dele():
    examine()
    print("1.根据用户名删除\n2.清空所有数据")
    select=input("请输入选项")
    while select!="1" and select!="2":
        select=input("输入无效,请重新输入:")
    if select=="1":
        key=input("请输入用户名")
        keys=all_information.keys()
        while key not in keys:
            select = input("该用户未被注册,请选择1.注册 2.重新输入用户名")
            while select != "1" and select != "2":
                select = input("选项有误,请重新输入")
            if select == "1":
                add_information()
                break
            else:
                key = input("请再次输入用户名")
        del all_information[key]
        print("-"*30+"删除成功"+"-"*30)
    else:
        all_information.clear()
        print("-"*30+"已清空"+"-"*30)
while True:
    print(menu)
    select = int(input("请输入选项:"))
    while select < 0 or select > 5:
        select = int(input("输入有误,请重新输入:"))
    if select == 1:
        add_information()
    elif select == 2:
        if all_information == {}:
            print("数据储存为空")
            break
        else:
            examine()
    elif select == 3:
        if all_information == {}:
            print("数据储存为空")
            break
        else:
            change()
    elif select == 4:
        if all_information == {}:
            print("数据储存为空")
            break
        else:
            dele()
    else:
        print("感谢使用,下次再会")
        break