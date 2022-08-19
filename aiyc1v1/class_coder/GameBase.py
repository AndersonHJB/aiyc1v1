import random
from faker import Faker


# 游戏的完成
# 随机生成敌人名称
# 自定义玩家名称
# 扩展：要求特殊神通：一键回血，副作用：敌人攻击值加倍
class Creature():
    def __init__(self, hp, name=Faker().name()):
        self.hp = hp
        self.name = name
        # self.faker = Faker()
        self.beishu = 1

    def attack(self):
        """
        function: 生成随机攻击值
        :return:
        """
        attack_value = random.randint(0, 50)
        return attack_value

    def not_dead(self):
        if self.hp > 0:
            return True
        else:
            return False

    def being_attack(self, attack_value):
        self.hp = self.hp - attack_value * self.beishu

    def show_status(self):
        # print(self.hp)
        print(f"{self.name}' hp is {self.hp}.")

    def hp_update(self):
        self.hp = 100
        self.beishu = 2


def main():
    player = Creature(100, "Austin")
    enemy = Creature(80)
    while player.not_dead() and enemy.not_dead():
        player.show_status()
        enemy.show_status()
        user_operation = input("Attack or Defence(A or D):>>>").upper()
        if user_operation == "A":
            player_attack_value = player.attack()
            enemy_attack_value = enemy.attack()
            player.being_attack(enemy_attack_value)
            enemy.being_attack(player_attack_value)
        elif user_operation == "D":
            enemy_attack_value = enemy.attack() * 0.1
            player.being_attack(enemy_attack_value)
        elif user_operation == "666":
            s = "请确认您的操作，这将把你的血量恢复至 100\n敌人攻击值将提升两倍。\n取消请输入 No，确认直接 enter or yes:"
            u = input(s)
            if u == "" or u.lower() == "yes":
                player.hp_update()
            else:
                print("您已经取消恢复血量......\n祝您好运！")
                # pass

    if player.not_dead():
        print("You Win.")
    else:
        print("You lose.")


if __name__ == '__main__':
    main()
