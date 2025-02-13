import time,random,re,sys,tabulate
    
class Category:
    def __init__(self,phrase_list):
        self.phrase_list=phrase_list
    def choosePhrase(self,num):
        self.guess_phrase=self.phrase_list[num-1]
        del self.phrase_list[num-1]
        return self.guess_phrase
    def remainPhraseCount(self):
        if len(self.phrase_list)==0:
            print("所有词都猜完了，进入结算...")
            time.sleep(1)
            self.resultCalculation()
        return None
    def resultCalculation(self):
        print("计算公式：总积分=金钱*1+奖品数*250+胜利数*500")
        time.sleep(3)
        self.table_header=["玩家名","金钱","奖品","胜利","总积分"] #表头
        self.table_data=[]
        self.score_dict={}
        for i in range(int(num_human)):
            self.one_player=[]
            self.one_player.append(object_list_human[i].name)
            self.one_player.append(object_list_human[i].money)
            self.one_player.append(object_list_human[i].prize)
            self.one_player.append(object_list_human[i].win)
            score=int(object_list_human[i].money)+250*int(object_list_human[i].prize)+500*int(object_list_human[i].win)
            self.one_player.append(score)
            self.score_dict[object_list_human[i].name]=score #键值对 玩家名：总积分
            self.table_data.append(self.one_player) #将数据加入至表格体中
        for i in range(int(num_computer)):
            self.one_player=[]
            self.one_player.append(object_list_computer[i].name)
            self.one_player.append(object_list_computer[i].money)
            self.one_player.append(object_list_computer[i].prize)
            self.one_player.append(object_list_computer[i].win)
            score=int(object_list_computer[i].money)+250*int(object_list_computer[i].prize)+500*int(object_list_computer[i].win)
            self.one_player.append(score)
            self.score_dict[object_list_computer[i].name]=score  #键值对 玩家名：总积分
            self.table_data.append(self.one_player)
        print(tabulate.tabulate(self.table_data,self.table_header,"simple"))
        time.sleep(5)
        score_result=sorted(self.score_dict.items(),key=lambda item:item[1],reverse=True) #list中嵌套元组
        print(f"本场游戏的胜利者是：{score_result[0][0]}！")
        time.sleep(2)
        print("游戏结束")
        time.sleep(5)
        sys.exit(0)
        #计算方法，输出结果，结束游戏

class Player: #所有玩家都有money，prize，win三个属性
    def __init__(self,money=0,prize=0,win=0):
        self.money=money
        self.prize=prize
        self.win=win

class Human(Player): #所有human玩家都有属性"human",使用"hand"方法答题
    def __init__(self,money=0,prize=0,win=0,player_type="human"):
        super().__init__(money,prize,win)
        self.player_type=player_type
    def HandInput(self):
        return input("你的答案是：")

class Computer(Player): #所有computer玩家都有属性"computer"，使用"random"方法答题
    def __init__(self,money=0,prize=0,win=0,player_type="computer"):
        super().__init__(money,prize,win)
        self.player_type=player_type
    def randomInput(self,guess_phrase):
        time.sleep(3)
        rd=random.randint(1,20)
        list_1=['a','e','i','o','u',' '] #英文字母使用频率来源于网络
        list_2=['s','r','n','t','l']
        list_3=['c','d','g','p','m','h','b']
        list_4=['y','f','v','k','w']
        list_5=['z','x','j','q']
        phrase_list=[guess_phrase[i] for i in range(len(guess_phrase))] #将答案（要猜的内容）分割成列表
        if self.money>=250:
            if rd>10: #10/20
                return random.choice(list_1)
            if rd>7: #3/20
                return random.choice(list_2)
            if rd>5: #2/20
                return random.choice(list_3)
            if rd>3: #2/20
                return random.choice(list_4)
            else: #3/20 必定猜中（不过有可能猜重）
                return random.choice(phrase_list)
        elif self.money==0: #没钱的时候能力爆发
            if rd>10: #10/20 必顶猜中
                return random.choice(phrase_list)
            if rd>4: #4/20
                return random.choice(list_2)
            else: #4/20
                return random.choice(list_3)
        else: #0<money<250
            if rd>14: #6/20
                return random.choice(list_2)
            if rd>9: #5/20
                return random.choice(list_3)
            if rd>5: #4/20
                return random.choice(list_4)
            if rd>3: #2/20
                return random.choice(list_5)
            else: #3/20 必定猜中
                return random.choice(phrase_list)
    def randomAnotherRound(self):
        lst=["yes","no"]
        rd=random.choice(lst)
        return rd

class Human_1(Human):  #个体human玩家有不同名字
    def __init__(self,money=0,prize=0,win=0,player_type="human",name="Human 1"):
        super().__init__(money,prize,win,player_type)
        self.name=name
    def __repr__(self):
        return str(self.name)
class Human_2(Human):
    def __init__(self,money=0,prize=0,win=0,player_type="human",name="Human 2"):
        super().__init__(money,prize,win,player_type)
        self.name=name
    def __repr__(self):
        return str(self.name)
class Computer_1(Computer): #个体computer玩家有不同名字
    def __init__(self,money=0,prize=0,win=0,player_type="computer",name="AI 1"):
        super().__init__(money,prize,win,player_type)
        self.name=name
    def __repr__(self):
        return str(self.name)
class Computer_2(Computer):
    def __init__(self,money=0,prize=0,win=0,player_type="computer",name="AI 2"):
        super().__init__(money,prize,win,player_type)
        self.name=name
    def __repr__(self):
        return str(self.name)

def spinWheel(object_list_shuffle,index):
    #human或者computer回合，对不同玩家更改数据
    print(f"{object_list_shuffle[index].name},转动转盘...")
    time.sleep(3)
    options=["猜词","猜词+赠送奖品","跳过回合","破产","跳过回合，但增加金钱250","猜词+增加金钱250"]
    rd=0
    rd=random.randint(1,10)
    print(rd)
    if rd in [1,2,3,4]: #40% cash
        choice=options[0]
    elif rd==5: #10% cash+prize
        choice=options[1]
    elif rd==6: #20% lose turn
        choice=options[2]
    elif rd in [8,9]: #20%
        choice=options[4]
    elif rd==7:
        choice=options[5]
    else: #rd==10 10% bankrupt
        assert rd==10
        choice=options[3]
    print(f"转盘结果：{choice}")
    if choice=="猜词":
        return "guessTurn"
    elif choice=="猜词+赠送奖品":
        print("获得奖品+1")
        object_list_shuffle[index].prize+=1
        print(f"奖品数：{object_list_shuffle[index].prize}")
        return "guessTurn"
    elif choice=="猜词+增加金钱250":
        object_list_shuffle[index].money+=250
        time.sleep(3)
        return "guessTurn"
    elif choice=="破产":
        object_list_shuffle[index].money=0
        print("钱数清零，回合结束")
        time.sleep(3)
        return None
    elif choice=="跳过回合，但增加金钱250":
        object_list_shuffle[index].money+=250
        time.sleep(3)
        return None
    else:
        time.sleep(3)
        return None

def guessTurn(guessed_list,object_list_shuffle,index,guess_phrase,blank_phrase):
    time.sleep(1)
    print(f"{object_list_shuffle[index].name} 开始回合")
    time.sleep(2)
    print(f"钱：{object_list_shuffle[index].money}")
    print(f"题目：{blank_phrase}")
    if object_list_shuffle[index].player_type=="human":
        guess=human.HandInput() #使用human类方法
    elif object_list_shuffle[index].player_type=="computer":
        guess=computer.randomInput(guess_phrase) #使用computer类方法
        print(f"你的答案是：{guess}")
        time.sleep(2)

    while checkIfInputValid(guess,guessed_list,object_list_shuffle,index)=="Invalid":
        #检查输入是否符合规范，只要不符合，就重新输入guess
        if object_list_shuffle[index].player_type=="human":
            guess=human.HandInput()
        elif object_list_shuffle[index].player_type=="computer":
            guess=computer.randomInput(guess_phrase)
            print(f"你的答案是：{guess}")
            time.sleep(2)

    guessed_list.append(guess)  #更新已猜过的list
    guessed_list,blank_phrase,flag=checkIfInputPhrase(guess,guess_phrase,object_list_shuffle,index,guessed_list,blank_phrase)
    if flag=="charcter": #同一函数中返回值数量必须设置为相同，因此用flag来区分不同情况
        pass #输入的是单个字母，继续执行下一步
    elif flag=="win":
        return guessed_list,blank_phrase,"win" #输入的是单词/句子，猜对全部
    else: #flag==0
        assert flag==0
        return guessed_list,blank_phrase,0 #猜错，回合结束
    guessed_list,blank_phrase,flag_1=checkGuess(guess,guess_phrase,object_list_shuffle,index,blank_phrase,guessed_list)
    if flag_1=="win":
        return guessed_list,blank_phrase,"win" #输入的是单个字母，猜对全部
    else: #flag_1==0
        assert flag_1==0
        return guessed_list,blank_phrase,0  #猜错，回合结束

def checkIfInputValid(guess,guessed_list,object_list_shuffle,index):
    for i in range(len(guessed_list)):
        if guess==guessed_list[i]:
            print("你的答案已经猜过了!") #如果computer随机猜测，猜重复，不会显示
            time.sleep(1)
            return "Invalid" #检查是否输入重复，无重复则执行下面的代码
    if guess in ["a","e","i","o","u"," "] and object_list_shuffle[index].money<250:
        print(f"猜元音和空格需要花费250，你只有{object_list_shuffle[index].money}")
        time.sleep(1)
        return "Invalid"
    elif guess in ["a","e","i","o","u"," "]and object_list_shuffle[index].money>=250:
        object_list_shuffle[index].money-=250 #若猜元音和空格，扣除250
        print(f"金钱-250，剩余金钱:{object_list_shuffle[index].money}")
    return None

def checkIfInputPhrase(guess,guess_phrase,object_list_shuffle,index,guessed_list,blank_phrase):
    if len(guess)>1: #若输入的是单词/句子
        if checkIfWin(guess,guess_phrase,object_list_shuffle,index,blank_phrase,flag="sentence")=="win": #win
            return guessed_list,blank_phrase,"win"
        else:
            print("回答错误，扣除所有金钱，回合结束")
            object_list_shuffle[index].money=0
            return endPlayerTurn(guessed_list,blank_phrase,0)
    else: #输入的是单个字符
        return guessed_list,blank_phrase,"charcter"

def checkIfWin(guess,guess_phrase,object_list_shuffle,index,blank_phrase,flag):
    if flag=="sentence": #猜单词/句子猜对
        if guess==guess_phrase:
            print(f"回答正确，{object_list_shuffle[index].name}胜利+1")
            object_list_shuffle[index].win+=1
            return "win"
        else:
            return None
    elif flag=="character": #猜字母猜对
        if blank_phrase==guess_phrase:
            print("回答正确，胜利+1")
            object_list_shuffle[index].win+=1
            return "win"
        else:
            return None

def checkGuess(guess,guess_phrase,object_list_shuffle,index,blank_phrase,guessed_list):
    count=0 #记录匹配字符的次数
    correct_dest=[] #记录匹配的所有str下标
    for i in range(len(guess_phrase)):
        if guess==guess_phrase[i]:
            count+=1
            correct_dest.append(i)
    if guess==" ": guess="|" #猜空格的时候，换成|以明确显示
    blank_phrase_new=""
    for i in range(len(guess_phrase)): #对blank_phrase进行替换
        if i in correct_dest:
            blank_phrase_new+=guess
        else:
            blank_phrase_new+=blank_phrase[i]
    if guess=="|": guess=" "
    blank_phrase=blank_phrase_new
    if count>0:
        if checkIfWin(guess,guess_phrase,object_list_shuffle,index,blank_phrase,flag="character")=="win":
            return guessed_list,blank_phrase,"win"
        else:
            object_list_shuffle[index].money+=250*count
            print(f"回答正确，{guess}在题目中出现{count}次，金钱+{count*250}")
            print(f"金钱：{object_list_shuffle[index].money}")
            if object_list_shuffle[index].player_type=="human":
                flag=input("是否再转一次转盘？输入yes为“是”，输入其它为“否”：") #猜对但没猜完的情况
            elif object_list_shuffle[index].player_type=="computer":
                print("是否再转一次转盘？")
                flag=computer.randomAnotherRound() #如果是AI，随机选择是否继续一回合
                time.sleep(2)
                print(flag)
                time.sleep(2)
            if flag=="yes":
                if spinWheel(object_list_shuffle,index)=="guessTurn":
                    time.sleep(3)
                    guessed_list,blank_phrase,flag=guessTurn(guessed_list,object_list_shuffle,index,guess_phrase,blank_phrase)
                    if flag==0:  #同玩家多次猜词后猜错，结束回合
                        return endPlayerTurn(guessed_list,blank_phrase,0)
                    if flag=="win":  #同玩家多次猜词到全猜中，win
                        return guessed_list,blank_phrase,"win"
                else:
                    return endPlayerTurn(guessed_list,blank_phrase,0)
            else:
                print("回合结束")
                return endPlayerTurn(guessed_list,blank_phrase,0)
    else:
        print("回答错误，回合结束")
        return endPlayerTurn(guessed_list,blank_phrase,0)

def endPlayerTurn(guessed_list,blank_phrase,flag=0):
    time.sleep(1)
    return guessed_list,blank_phrase,flag #下一个玩家继续猜

def gameStart():
    while 1: #直到category里所有词都被猜完，结束游戏
        res=category.remainPhraseCount() #判断是否还有剩余题目
        guess_phrase=category.choosePhrase(num=1) #baseball
        blank_phrase=re.sub(".","_",guess_phrase) #______
        print(f"题目：{blank_phrase}")
        print("正在随机生成猜词顺序...")
        time.sleep(3)
        object_list_shuffle=object_list_human+object_list_computer
        random.shuffle(object_list_shuffle)
        print("本场猜词顺序：",end='')
        for i in range(int(num_human)+int(num_computer)): #输出猜词顺序
            print(object_list_shuffle[i],end=' ')
        print("\n",end='')
        time.sleep(2)
        guessed_list=[""]
        while 1: #直到一个phrase被全部猜中，才会结束循环，循环的过程中变量保留
            flag_out=""
            for i in range(int(num_human)+int(num_computer)):
                index=i
                if spinWheel(object_list_shuffle,index)=="guessTurn": #拥有猜词机会
                    guessed_list,blank_phrase,flag=guessTurn(guessed_list,object_list_shuffle,index,guess_phrase,blank_phrase)
                    if flag=="win": #被全部猜中
                        print(f"正确答案是：{guess_phrase}")
                        time.sleep(3)
                        flag_out=flag
                        break #跳出for
            if flag_out=="win":
                break #跳出while

def gameInit():
    print(f"本游戏最多支持{max_num_human}人和{max_num_computer}台AI")
    name_list_human,num_human,flag=namePlayers("human")
    while flag==0: #输入错误
        name_list_human,num_human,flag=namePlayers("human")
    name_list_computer,num_computer,flag=namePlayers("computer")
    while flag==0:
        name_list_computer,num_computer,flag=namePlayers("computer")
    return name_list_human,name_list_computer,num_human,num_computer

def namePlayers(player_type):
    if player_type=="human":
        max_num=max_num_human
    elif player_type=="computer":
        max_num=max_num_computer
    num=input(f"输入{player_type}玩家数：")
    try:
        int(num)
    except:
        print("输入的不是数字，重新输入")
        return [],num,0
    if int(num)==0 and player_type=="human":
        print("玩家人数必须至少为1，重新输入")
        return [],num,0
    if int(num)>max_num:
        print(f"人数最多为{max_num}，重新输入")
        return [],num,0
    elif int(num)<0:
        print("人数不能为负，重新输入")
        return [],num,0
    elif int(num)==0:
        return [],num,None
    elif int(num)==1:
        name_list=[]
        name_list.append(input(f"请输入{player_type}玩家名："))
        return name_list,num,None
    else:
        name=input(f"请按顺序输入{player_type}玩家名，单个空格隔开：")
        if len(re.findall(" ",name))!=int(num)-1:
            print("输入名字个数错误，重新输入")
            return [],num,0
        name_list=name.split(" ",int(num)-1)
        return name_list,num,None

max_num_human=2  #预先赋值的全局变量，要用此值决定实例化几个human个体类
max_num_computer=2

##在这里修改题目：注意无大写，无标点
phrase_list=["si affettano le patate e il prosciutto sul tagliere","si accende il fuoco e si mettono due cucchiai di pasta sulla padella"]

random.shuffle(phrase_list) #打乱题目顺序
category=Category(phrase_list)

#人类玩家名单和人数，AI玩家名单和人数，这些都是全局变量
name_list_human,name_list_computer,num_human,num_computer=gameInit()
#设置：每个玩家个体类对象名，和类中的name属性名相同
#需要由类对象名，得知其player_type（使用键盘输入还是随机输入方法），改变money等属性数据
#需要由类属性name，获取其名字的str形式，输出结果
#因此增加object_list，用以与name_list区分，之后不再使用name_list，而是通过object.name访问name
object_list_human=name_list_human.copy()
object_list_computer=name_list_computer.copy()

#实例化：由于有很多全局变量，故不使用函数
player=Player()
human=Human()
computer=Computer()
if int(num_human)>0: #设置多少玩家，就实例化多少玩家个体类
    object_list_human[0]=Human_1()
    object_list_human[0].name=name_list_human[0]
    if int(num_human)==2:
        object_list_human[1]=Human_2()
        object_list_human[1].name=name_list_human[1]
if int(num_computer)>0:
    object_list_computer[0]=Computer_1()
    object_list_computer[0].name=name_list_computer[0]
    if int(num_computer)==2:
        object_list_computer[1]=Computer_2()
        object_list_computer[1].name=name_list_computer[1]

gameStart()