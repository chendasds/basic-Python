
# 列表与元组
# 列表的创建
# list_one = []
# list_two = ["a", 'f', 'd', 22]
# for i in list_two:
#     print()
# print(isinstance())
# from collections import Iterable
# print(isinstance([], Iterable))
# from collections.abc import Iterable
#
# print(isinstance([], Iterable))
# list_one = ["java", 'c++', "python", "PHP"]
# print(list_one[0])
# print(list_one[2])
# print(list_one[-1])
# print(list_one[1:])
# print(list_one[:])
# print(list_one[:2])
# print(list_one[0:3:2])
# print(len(list_one))
# reward_info = ['谢谢惠顾', '一等奖', '三等奖', '谢谢惠顾',
#                '谢谢惠顾', '三等奖', '二等奖', '谢谢惠顾']
# flag = True
# while flag:
#     num = int(input("请输入要刮奖的编号(1~8): "))
#     if 0 < num <= len(reward_info):
#         prize = reward_info[num - 1]
#         print(prize)
#         flag = False
#     else:
#         print("您的输入不符合要求请重新输入")

# 列表的遍历
# list_name = ['小美', '梨花', '小国', '小霞']
# for i in list_name:
#     print(f"{i}你好")

# list_one = [1, 3, 55, 33, 2, 9, 5]
# list_two = [2, 3, 7, 1, 3, 44, 5]
# list_three = ['wwrr', 'www', 'wrarf', 'w']
# list_one.sort()
# list_two.sort(reverse=True)
# list_three.sort(key=len, reverse=True)
# print(list_one)
# print(list_two)
# print(list_three)
# sorted(list_one)
# print(list_one)
# 输出结果没有改变, 因为sorted的返回值是排序后的结果
# list_test = sorted(list_one)
# print(list_test)
# print(list_one)
# list_one.reverse()
# print(list_one)
# list_one.append(2)
# list_one.extend(list_three)
# print(list_one)
# import random
# num = random.randint(0,1)
# print(num)
# import random
#
# i = 0
# while i<= 8:
#     print(random.randint(1, 4))
#     i += 1
# print(list_three[2])
# # list_three = ['wwrr', 'www', 'wrarf', 'w']
# name = input()
# for i in list_three:
#     if name == i:
#         print(i)
# count = 0
# for i in list_one:
#
#     count += 1
#     print(count)
# import random
# list_one  = [1, 2, 3, 4, 5, 6]
# for i in list_one:
#     print(random.randint(0, 10))
# list_one = list([1, 2, 3])
# for i in list_one:
#     print(list_one)
# tuple_one = ("abc", "www", [1, 2, 3])
# print(tuple_one)
# tuple_one[2][1] = 6
# tuple_one[2][2] = 10
# print(tuple_one)
# str1 = "python"
# print(str1[1])
# # print(str[1, 2])
# print(str1[1], str1[2])
# uppercase_numbers = ("零", "壹", "贰", "叁", "肆","伍",
# "陆", "柒", "捌", "玖")
# number = input("请输入一个数字：")
# for i in range(len(number)):
#     print(uppercase_numbers[int(number[i])], end="")
# tuple_one = ("python", "java")
# print(tuple_one)
tuple_one = ("q")
print(tuple_one)
tuple_two = ("q",)
print(tuple_two)
