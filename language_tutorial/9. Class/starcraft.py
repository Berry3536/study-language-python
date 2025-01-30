from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다. ".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}].".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class OffensiveUnit(Unit):  # OffensiveUnit 클래스는 Unit 클래스를 상속받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # 상속
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))

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

# Unit - Marine
class Marine(OffensiveUnit):
    def __init__(self):
        OffensiveUnit.__init__(self, "해병", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# Unit - Tank
class Tank(OffensiveUnit):
    seize_mode_developed = False

    def __init__(self):
        OffensiveUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_mode_developed == False:
            return
        
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False           

# Unit - Wraith
class Wraith(FlyableOffensiveUnit):
    def __init__(self):
        FlyableOffensiveUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 해제 상태

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 활성화합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 게임 시작
game_start()

# 해병 3기 생성
marine1 = Marine()
marine2 = Marine()
marine3 = Marine()

# 탱크 2기 생성
tank1 = Tank()
tank2 = Tank()

# 레이스 2기 생성
wraith1 = Wraith()
wraith2 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(marine1)
attack_units.append(marine2)
attack_units.append(marine3)
attack_units.append(tank1)
attack_units.append(tank2)
attack_units.append(wraith1)
attack_units.append(wraith2)

# 병력 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_mode_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 공격 시작
for unit in attack_units:
    unit.attack("1시")
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()