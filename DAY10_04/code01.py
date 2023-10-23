# input
# input()语句的功能是, 获取键盘输入的数据
# 可以使用: input(提示信息), 用以在使用者
# 演示Python的input语句
# name = input("请告诉我你是谁?")
# print("我知道了, 你是:%s" % name)
#
# # 输入数字类型
# num = input("请告诉我你的银行卡密码: ")
# # 数据类型转换
# # num = int(num)
# print("你的银行卡密码的类型是: ", type(num))
# result = 10 > 5
# print(f"10 > 5的结果是: {result}, 类型是{type(result)}")
# age = 10
# print(f"今天我已经{age}岁了")
# if age >= 18:
#     print("我已经成年了")
# print("时间过的真快")
# print("欢迎来到游乐园, 儿童免费, 成人收费")
# age = input("请输入您的年龄: ")
# age = int(age)
# if age >= 18:
#     print("您已经成年, 游玩需要票价20元")
# print("祝您玩的愉快!")
# height = input("请输入您的身高(cm): ")
# height = int(height)
# if height >= 120:
#     print("您的身高超过120cm, 游玩需要购票10元")
# else:
#     print("您的身高未超过120cm, 可以免费游玩")
# print("祝您玩得愉快")
# print("欢迎来到动物园")
# if int(input("请输入您的身高(cm): ")) > 120:
#     print("你的身高大于120cm, 不免费")
#     print("不过如果你的vip等级高于3, 可以免费游玩")
#
#     if int(input("请输入您的vip等级: ")) > 3:
#         print("条件合格, 可以免费游玩")
#     else:
#         print("条件不合格, 请支付门票")
# else:
#     print("祝您游玩愉快!")
# 公司要发放礼物, 条件是:
# 年龄限定18岁至30岁之间
# 同时入职时间需要满足大于两年, 或者级别大于3才可以领取
# age = int(input("请输入您的年龄: "))
# year = int(input("请输入您的入职时间(year): "))
# level = int(input("请输入您的级别: "))
# if age >= 18:
#     print("成年人符合, 继续判定")
#     if age <=30:
#         print("年龄达标继续判定")
#         if year > 2:
#             print("不大于30岁且入职超过两年可以领取")
#         else:
#             print("因为您的入职时间没有达到要求, 不符合领取条件")
#     elif level > 3:
#         print("符合级别要求")
#     else:
#         print("不符合级别要求")
# else:
#     print("您的年龄没有满足要求")
# import random
# num = random.randint(1, 10)
# num01 = int(input("请输入您猜的数字: "))
# if 10 >= num01 >= 1:
#     if num01 == num:
#         print("猜对了")
#     elif num01 > num:
#         print("猜大了")
#         num01 = int(input("请输入您猜的数字: "))
#         if 10 >= num01 >= 1:
#             if num01 == num:
#                 print("猜对了")
#             elif num01 > num:
#                 print("猜大了")
#                 num01 = int(input("请输入您猜的数字: "))
#                 if 10 >= num01 >= 1:
#                     if num01 == num:
#                         print("猜对了")
#                     elif num01 > num:
#                         print("猜大了")
#                     elif num01 < num:
#                         print("猜小了")
#             elif num01 < num:
#                 print("猜小了")
#                 num01 = int(input("请输入您猜的数字: "))
#                 if 10 >= num01 >= 1:
#                     if num01 == num:
#                         print("猜对了")
#                     elif num01 > num:
#                         print("猜大了")
#                     elif num01 < num:
#                         print("猜小了")
#     elif num01 < num:
#         print("猜小了")
#         num01 = int(input("请输入您猜的数字: "))
#         if 10 >= num01 >= 1:
#             if num01 == num:
#                 print("猜对了")
#             elif num01 > num:
#                 print("猜大了")
#                 num01 = int(input("请输入您猜的数字: "))
#                 if 10 >= num01 >= 1:
#                     if num01 == num:
#                         print("猜对了")
#                     elif num01 > num:
#                         print("猜大了")
#                     elif num01 < num:
#                         print("猜小了")
#             elif num01 < num:
#                 print("猜小了")
#                 num01 = int(input("请输入您猜的数字: "))
#                 if 10 >= num01 >= 1:
#                     if num01 == num:
#                         print("猜对了")
#                     elif num01 > num:
#                         print("猜大了")
#                     elif num01 < num:
#                         print("猜小了")
# print("游戏结束")
