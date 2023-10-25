# info_dict = {1: "小明", 2: "小刚", 3: "小红", 4: "梨花"}
# print(info_dict)
# print(info_dict[1])
# str = "pyhton"
# print(str[0])
# dict01 = {"姐姐": "小红", "哥哥": "梨花", "妹妹": "小刚"}
# print(dict01["姐姐"])
# print(dict01["哥哥"])
# dict02 = {"家人": dict01}
# print(dict02["家人"]["姐姐"])
# dict_twice01 = {"u": "Tuesday", "h": "Thursday"}
# dict_twice02 = {"a": "Saturday", "u": "Sunday"}
# dict_once = {"m": "Monday", "w": "Wednesday", "f": "Friday", "t": dict_twice01, "s": dict_twice02}
# flag = True
# while flag:
#     str_screen01 = input("请输入第一个字母: ")
#     if str_screen01 == "t" or str_screen01 == "s":
#         str_screen02 = input("请输入第二个字母: ")
#         if str_screen02 in dict_twice01:
#             print(dict_twice01[str_screen02])
#         elif str_screen02 in dict_twice02:
#             print(dict_twice02[str_screen02])
#         else:
#             print("输入有误请重新输入")
#     elif str_screen01 in ["m", "w", "f"]:
#         print(dict_once[str_screen01])
#     else:
#         print("输入有误请重新输入")
#     str_screen03 = input("是否继续?: ")
#     if str_screen03 == "否":
#         flag = False
# dict_one = dict(哥哥 = "小刚", 妹妹 = "小美")
# print(dict_one)


# 1. 字典的二种添加元素的方式
# add_dict = {"姐姐": "小美", "哥哥": "小刚"}

# 第一种
# add_dict.update(弟弟 = "张三")
# print(add_dict)

# 第二种
# add_dict["student"] = "小丁"
# print(add_dict)


# 2. 修改字典元素
# 修改字典元素的本质是通过键值获得元素, 再重新对元素赋值
# 两种方式          1. update   2. 通过键来改变

# 1.update
# add_dict.update(student = "王五")
# print(add_dict)
# 2. 键
# add_dict["student"] = "李四"
# print(add_dict)


# 3. 删除字典中的元素

# 1. pop()
# dict_test = {"001": "小红", 2:"小米", 3: "小子"}
# print(dict_test.pop(1))
# # 删除成功, 返回目标元素的值
# print(dict_test)

# 2. popitem()随机删除字典的中的元素
# dict_test = {1: 1, 2: 2, 3: 3, 4: 4}
# print(dict_test.popitem())
# print(dict_test)

# 3. clear用于清空字典元素
# dict_test.clear()
# print(dict_test)

#
# print(dict_test)
# print(dict_test.items())
# for i in dict_test.items():
#     print(i)
# print(dict_test.clear())
# print(dict_test)
# print(dict_test.keys())
# for i in dict_test.keys():
#     print(i)
# print(dict_test.values())
# for i in dict_test.values():
#     print(i)
# list_one = [1, (1, 2), [1, 2]]
# print(list_one)
# list_one.append(2)
# print(list_one)
# list_one[2].append(3)
# print(list_one)
# set_one = set([1, 2, 4])
# set_one = set((1, 2, 3))
# print(set_one)
# set_two = {1, 2, "w"}
# print(set_two)
# set_one = frozenset([1, 2, 3])
# print(set_one)
# set_one = set()
# set_one.add("py")
# set_one.update("python")
# print(set_one)
# set_one = {1, 2, 3, 3}
# print(set_one)
# list_one = [1, 2, 3, 3]
# print(list_one)
dict_one = {1: "www", 2: "qqq", "03": "ccc"}
# print(dict_one)
# print(dict_one[2])
# dict_one.update({"03": "kkk"})
# print(dict_one)
# dict_one.update({"03": "ppp"})
# dict_one[2] = "rrr"
# print(dict_one)
set_one = {"a", "b", "c", "d"}
set_one.add("e")
print(set_one)