import random
# 随机分配办公室
list_peo = ["赵老师", "王老师", "李老师", "孙老师", "周老师", "郑老师", "冯老师", "何老师"]
list_off = [[], [], []]
for i in list_peo:
    list_off[random.randint(0, 2)].append(i)
print(list_off)
print(f"1号办公室的人数有{len(list_off[0])}人, 分别为{list_off[0]}")
print(f"2号办公室的人数有{len(list_off[1])}人, 分别为{list_off[1]}")
print(f"3号办公室的人数有{len(list_off[2])}人, 分别为{list_off[2]}")