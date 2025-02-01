class Unit:
    def __init__(self, name, hp, damage):   # __init__ -> 생성자: 객체가 생성될 때, 자동으로 호출
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 인스턴스 생성
# marine_1 = Unit("marine1", 40, 5)
# marine_2 = Unit("marine2", 40, 5)
# marine_3 = Unit("marine3", 40, 5)
# tank_1 = Unit("tank1", 150, 35)
# tank_2 = Unit("tank2", 150, 35)
# tank_3 = Unit("tank3", 150, 35)

# 외부에서 멤버 변수 사용, 추가 할당
wraith_1 = Unit("wraith1", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith_1.name, wraith_1.damage))

wraith_2 = Unit("wraith2", 80, 5)
wraith_2.clocking = True

# if wraith_1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다".format(wraith_1.name))

if wraith_2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith_2.name))