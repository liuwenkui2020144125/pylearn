from random import randint
import time,sys

# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100



    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    def __repr__(self):
        return f'name:{self.name}:strength:{self.strength}'
        # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print("game beginning")

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification,end='')

print('\n')

time.sleep(1)
print("10 ",end=" ")
time.sleep(1)
print("9 ",end=" ")
time.sleep(1)
print("8 ",end=" ")
time.sleep(1)
print("7 ",end=" ")
time.sleep(1)
print("6 ",end=" ")
time.sleep(1)
print("5 ",end=" ")
time.sleep(1)
print("4 ",end=" ")
time.sleep(1)
print("3 ",end=" ")
time.sleep(1)
print("2 ",end=" ")
time.sleep(1)
print("1 \n",end=" ")#显示10S开始清屏
print("时间到，开始清屏")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")#清屏
print("回车开始游戏")
#初始化玩家
player=Player(1000)
print(f"您现在有{player.stoneNumber}灵石")
#显示灵石数量
laststone=1000
#雇佣战士
def hireWarriors():
    menu='''
    请选择雇佣兵种
    1—弓箭兵
    2—斧头兵
    0—选择完成，退出
    '''
    while 1:
        choice=input(menu)
        if choice not in ['0','1','2']:
            print("输入错误")
            continue

        if choice=='0':#退出雇佣流程
            return
        if choice=='1':
            hireClass=Archer
        else:
            hireClass=Axeman

        if hireClass.price>player.stoneNumber:
            print(f"灵石不足,您只有{player.stoneNumber}灵石")
            continue

        #给战士命名
        while 1:
            warriorName=input("给战士命名:")
            if not warriorName:#没有输入内容
                continue
            if warriorName in player.warriors:
                print("该名字已被使用")
                continue
            break


        #招入战士
        player.warriors[warriorName]=hireClass(warriorName)
        #支付灵石
        player.stoneNumber-=hireClass.price
        print(f"雇佣成功，您现在剩余灵石{player.stoneNumber}")

#雇佣弓箭兵，斧头兵
hireWarriors()

#打印出灵石和战士情况
def printinfo():
    print("\n您麾下战士情况如下")
    for name,warrior in player.warriors.items():
        print(f"{name}:{warrior.typeName}生命值{warrior.strength}")
    print(f"您的灵石还剩余{player.stoneNumber}")

printinfo()

for name, warrior in player.warriors.items():
    print(f"{warrior.typeName}:{name}")

print("\n\n***出发啦*********")

#每个森林关卡
for no,forest in enumerate(forestList):
    #如果战士队列为空，游戏还没有通关，就失败了
    if not player.warriors:
        print("您麾下没有战士了，游戏结束")
        exit()

print(f'\n\n###现在到了第{no+1}座森林 ####')

#派出战士，森林作战
while 1:
    while 1:
        warriorName=input("选择派出的战士：")
        if warriorName not in player.warriors:
            print("没有这个战士")
            continue
        break
    warrior=player.warriors[warriorName]

    print(f"当前森林里面是{forest.monster.typeName}")

    warrior.fightWithMonster(forest.monster)

    print(f'经过战斗，你的战士{warriorName},生命值还有{warrior.strength}')

    #如果生命值小于等于0，该战士就死去了，从队列中消失
    if warrior.strength<=0:
        print(f'{warriorName}光荣的牺牲了')
        player.warriors.pop(warriorName)
        #没有战胜怪物，本关没有通关
        continue
    #战士生还，过关
    else:
        break
input("\n\n过关了，按回车键继续。 \n")
#过关后，选择给战士疗伤
while 1:
    printinfo()
    op=input('''\n请输入疗伤战士名字和灵石数量，格式为：姓名+20
    直接回车退出疗伤''')

    if not op:
        break
    if op.count('+')!=1:
        print("输入格式错误")
        continue
    name,stoneCount=op.split('+')
    name=name.strip()

