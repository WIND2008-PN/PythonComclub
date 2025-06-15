## Game Goblin vs Enemy
import random

class NPC:
    def __init__(self, name, hp, mana, can_rest):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.can_rest = can_rest  # เปลี่ยนชื่อ attribute

    def attack(self, target):
        if self.hp <= 0:
            print(f"{self.name} cannot attack. No HP left!")
            return
        if self.mana < 5:
            print(f"{self.name} cannot attack. Not enough mana!")
            return
        if target.hp <= 0:
            print(f"{target.name} has already been defeated!")
            return
        
        self.mana -= 5
        target.hp -= 40
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name} attacks {target.name}! {target.name} HP: {target.hp}")

    def heal(self):
        if self.hp <= 0:
            print(f"{self.name} cannot heal. No HP left!")
            return
        self.hp += 10
        print(f"{self.name} heals for 10 HP! Current HP: {self.hp}")

    def defend(self):
        if self.hp <= 0:
            print(f"{self.name} cannot defend. No HP left!")
            return
        if self.mana < 5:
            print(f"{self.name} cannot defend. Not enough mana!")
            return
        self.mana -= 5
        self.hp += 20
        print(f"{self.name} is defending this turn!")

    def rest(self):
        if self.can_rest:
            self.hp += 5
            self.mana += 10
            print(f"{self.name} rests and recovers 5 HP and 10 Mana! Current HP: {self.hp}, Mana: {self.mana}")
        else:
            print(f"{self.name} cannot rest. Resting state is not enabled.")

class PLAYER(NPC):
    def __init__(self, name, hp, mana, can_rest):
        super().__init__(name, hp, mana, can_rest)

    def attack(self, target):
        if self.hp <= 0:
            print(f"{self.name} cannot attack. No HP left!")
            return
        if self.mana < 10:
            print(f"{self.name} cannot attack. Not enough mana!")
            return
        if target.hp <= 0:
            print(f"{target.name} has already been defeated!")
            return
        
        self.mana -= 10
        target.hp -= 40
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name} attacks {target.name}! {target.name} HP: {target.hp}")

    def heal(self):
        if self.hp <= 0:
            print(f"{self.name} cannot heal. No HP left!")
            return
        self.hp += 20
        print(f"{self.name} heals for 20 HP! Current HP: {self.hp}")

    def defend(self):
        if self.hp <= 0:
            print(f"{self.name} cannot defend. No HP left!")
            return
        if self.mana < 5:
            print(f"{self.name} cannot defend. Not enough mana!")
            return
        self.mana -= 5
        self.hp += 20
        print(f"{self.name} is defending this turn!")

    def rest(self):
        if self.can_rest:
            self.hp += 5
            self.mana += 10
            print(f"{self.name} rests and recovers 5 HP and 10 Mana! Current HP: {self.hp}, Mana: {self.mana}")
        else:
            print(f"{self.name} cannot rest. Resting state is not enabled.")

# status
npc1 = NPC("Goblin", 100, 50, True) # atk 40 / heal +10 / mana -5
npc2 = PLAYER("Enemy", 120, 30, True) # atk 40 / heal +20 / mana -10

while npc1.hp > 0 and npc2.hp > 0:
    print(f"\n{npc1.name} (HP: {npc1.hp}, Mana: {npc1.mana})")
    print(f"{npc2.name} (HP: {npc2.hp}, Mana: {npc2.mana})")
    action = input("เลือกการกระทำของ Goblin (1=โจมตี, 2=heal, 3=ป้องกัน , 4=พักผ่อน): ")
    if action == "1":
        npc1.attack(npc2)
    elif action == "2":
        npc1.heal()
    elif action == "3":
        npc1.defend()
    elif action == "4":
        npc1.rest()
    else:
        print("การกระทำไม่ถูกต้อง กรุณาเลือก 1, 2 , 3 หรือ 4")
        continue
    
    if npc2.hp <= 0:
        print(f"{npc2.name} พ่ายแพ้แล้ว!")
        break

    # Enemy เลือกสุ่มการกระทำ
    enemy_action = random.choice(["1", "2", "3", "4"])
    if enemy_action == "1":
        npc2.attack(npc1)
    elif enemy_action == "2":
        npc2.heal()
    elif enemy_action == "3":
        npc2.defend()
    elif enemy_action == "4":
        npc2.rest()

    if npc1.hp <= 0:
        print(f"{npc1.name} พ่ายแพ้แล้ว!")
        break