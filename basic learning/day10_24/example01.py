# 刮刮乐
reward_info = ['谢谢惠顾', '一等奖', '三等奖', '谢谢惠顾',
               '谢谢惠顾', '三等奖', '二等奖', '谢谢惠顾']
flag = True
while flag:
    num = int(input("请输入要刮奖的编号(1~8): "))
    if 0 < num <= len(reward_info):
        prize = reward_info[num - 1]
        print(prize)
        flag = False
    else:
        print("您的输入不符合要求请重新输入")