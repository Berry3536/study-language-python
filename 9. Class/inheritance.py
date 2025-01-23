# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class OffensiveUnit(Unit):  # OffensiveUnit 클래스는 Unit 클래스를 상속받음
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   # 상속
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 비행 능력
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

# 비행 공격 유닛 - 다중 상속
class FlyableOffensiveUnit(OffensiveUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        OffensiveUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie = FlyableOffensiveUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")