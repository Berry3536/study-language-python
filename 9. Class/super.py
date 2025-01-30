# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}].".format(self.name, location, self.speed))

# 공격 유닛
class OffensiveUnit(Unit):  # OffensiveUnit 클래스는 Unit 클래스를 상속받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # 상속
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
        OffensiveUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0으로 처리
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # method overriding - 공중유닛에게도 fly method 대신 move를 사용
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물 생성 - super
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)   # 다중 상속에서는 super 사용 X
        self.location = location

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

