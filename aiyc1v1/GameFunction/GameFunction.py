# 文字对话
# 1、玩家、敌人
# 2、攻击值是随机的
# 3、判断输赢
# 4、玩家可以选择攻击或者防守，防守受到敌人攻击值的 1/10
# 5、显示生命值
# 6、显示玩家 and 敌人名称
# 7、获取输入来进行操作
import random

PLAYER_NAME = "Austin"
ENEMY_NAME = "Jaden"
PLAYER_HP = 100
ENEMY_HP = 80


def attack_value():
    attack_value = random.randint(0, 50)
    return attack_value


def not_dead(hp):
    if hp >= 0:
        return True
    else:
        return False


def being_attack(hp, attack_value):
    hp = hp - attack_value
    return hp


def show_status(name, hp):
    # print(self.hp)
    # print(f"{self.name}' hp is {self.hp}")
    print("{}' hp is {}".format(name, hp))


def win_or_lose(hp):
    if hp > 0:
        print("You Win!")
    else:
        print("You Lose!")


def main():
    global PLAYER_HP, ENEMY_HP
    while not_dead(PLAYER_HP) and not_dead(ENEMY_HP):
        show_status(PLAYER_NAME, PLAYER_HP)
        show_status(ENEMY_NAME, ENEMY_HP)
        user_operation = input("Attack or Defence(A/D):>>>")
        if user_operation.upper() == "A":
            player_attack_value = attack_value()  # 获取攻击值的操作
            enemy_attack_value = attack_value()  # 获取攻击值的操作
            PLAYER_HP = being_attack(PLAYER_HP, enemy_attack_value)
            ENEMY_HP = being_attack(ENEMY_HP, player_attack_value)
        elif user_operation.upper() == "D":
            enemy_attack_value = attack_value() * 0.1  # 获取攻击值的操作
            PLAYER_HP = being_attack(PLAYER_HP, enemy_attack_value)
        else:
            print("请输入 A or D......")
    win_or_lose(PLAYER_HP)


if __name__ == '__main__':
    main()
