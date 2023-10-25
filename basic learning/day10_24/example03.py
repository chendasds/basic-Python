# 好友管理系统
contact = []


# 好友管理系统菜单
def menu():
    print("欢迎使用好友管理系统")
    print("1: 添加好友")
    print("2: 删除好友")
    print("3: 备注好友")
    print("4; 展示好友")
    print("5: 退出")


# 添加好友
def addContact():
    flag = True
    while flag:
        add_name = input("请输入要添加的好友: ")
        contact.append(add_name)
        print("添加成功")
        print("1. 继续添加")
        print("2. 结束添加")
        while flag:
            num = int(input("请选择: "))
            if num == 2:
                return
            if num == 1:
                break
            else:
                print("选择有误, 请重新选择")


# 展示好友
def showContact():
    if len(contact) == 0:
        print("好友列表为空")
    else:
        count = 0
        for i in contact:
            count += 1
            print(f"{count} {i}")
    print()
    input("返回主菜单, 按enter键确定")
    return


# 备注好友
def markContact():
    flag = True
    while flag:
        mark_name = input("请输入要备注的好友姓名: ")
        count = 0
        for i in contact:
            if mark_name == i:
                mark_info = input("请输入要备注的信息: ")
                contact[count] = mark_info
                print(contact[count])
                print("备注成功")
                count += 1
                break
            else:
                print("要备注的好友不存在")
        while flag:
            print("1. 继续备注")
            print("2. 结束备注")
            num = int(input("请选择: "))
            if num == 1:
                break
            elif num == 2:
                return
            else:
                print("选择有误, 请重新选择")
            # test


# 删除好友
def delContact():
    flag = True
    while flag:
        del_name = input("请输入要删除的好友的姓名: ")
        count = 0
        for i in contact:
            if del_name == i:
                del contact[count]
                print("删除成功")
                count += 1
                break
            else:
                print("要删除的好友不存在")
        while flag:
            print("1. 继续删除")
            print("2. 结束删除")
            num = int(input("请选择: "))
            if num == 1:
                break
            elif num == 2:
                return
            else:
                print("选择有误, 请重新选择")

flag = True
while flag:
    menu()
    num = input("请输入您的选择: ")
    if num == "1":
        addContact()
    elif num == "2":
        delContact()
    elif num == "3":
        markContact()
    elif num == "4":
        showContact()
    elif num == "5":
        print("退出成功")
        flag = False
    else:
        print("输入有误")
        input("返回主菜单, 按enter键确定")
