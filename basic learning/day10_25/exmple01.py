
# 单词识别
dict_twice01 = {"u": "Tuesday", "h": "Thursday"}
dict_twice02 = {"a": "Saturday", "u": "Sunday"}
dict_once = {"m": "Monday", "w": "Wednesday", "f": "Friday", "t": dict_twice01, "s": dict_twice02}
flag = True
while flag:
    str_screen01 = input("请输入第一个字母: ")
    if str_screen01 in ["t", "s"]:
        str_screen02 = input("请输入第二个字母: ")
        if str_screen02 in ["u", "h", "a"]:
            print(dict_once[str_screen01][str_screen02])
        else:
            print("输入有误, 请重新输入")
            continue
    elif str_screen01 in ["m", "w", "f"]:
        print(dict_once[str_screen01])
    else:
        print("输入有误, 请重新输入")
        continue
    str_screen03 = input("是否继续?('按inter键'继续/'否'退出): ")
    if str_screen03 == "否":
        break