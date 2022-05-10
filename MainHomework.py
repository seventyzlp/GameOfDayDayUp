# 本质上算是之前修仙模拟器的续集，这一次尝试更加完美地还原mud游戏的体验，如果有余力，那么会进行视窗画面的制作

# 角色的初始化设定
ability = 1
BonusExpPercent = 0.01
year = 365


# 开始学习,使用函数形式不用重置变量值

# 问题1：连续学习365天
def Question1(ability, year, BonusExpPercent):
    for i in range(1, year + 1, 7):
        for j in range(i + 1, i + 8):
            if j - i <= 3 and j <= year + 1:
                continue
            elif j - i >= 4 and j <= year + 1:
                ability *= (1 + BonusExpPercent)
            else:  # 考虑到剩下的时间不足365天的情况
                continue
    print("连续学习一年后的能力值为：" + str(ability))


# 问题2.1：10天休息一次
def Question2_1(ability, year, BonusExpPercent):
    for i in range(1, year + 1, 10):
        for j in range(i + 1, i + 11):  # 枚举得出周期为10
            if 4 <= j - i <= 7 and j <= year + 1:
                ability *= (1 + BonusExpPercent)
            else:
                continue
    print("在一年中，每10天休息一次后的能力为：" + str(ability))


# 问题2.2：15天休息一次
def Question2_2(ability, year, BonusExpPercent):
    for i in range(1, year + 1, 15):
        for j in range(i + 1, i + 16):  # 枚举得出周期为15
            if (4 <= j - i <= 7 or 11 <= j - i <= 14) and j <= year + 1:
                ability *= (1 + BonusExpPercent)
            else:
                continue
    print("在一年中，每15天休息一次后的能力为：" + str(ability))


# 程序输出
Question1(ability, year, BonusExpPercent)
Question2_2(ability, year, BonusExpPercent)
Question2_1(ability, year, BonusExpPercent)

