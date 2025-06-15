class NPC:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

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
        print(f"{self.name} is defending this turn!")

class PLAYER:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

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
        print(f"{self.name} is defending this turn!")

# status
npc1 = NPC("Goblin", 100, 50) #atk 40 / heal +10 / mana -5
npc2 = PLAYER("Player", 120, 30) #atk 40 / heal +20 / mana -10

while npc1.hp > 0 and npc2.hp > 0:
    print(f"\n{npc1.name} (HP: {npc1.hp}, Mana: {npc1.mana})")
    print(f"{npc2.name} (HP: {npc2.hp}, Mana: {npc2.mana})")
    action = input("เลือกการกระทำของ Goblin (1=โจมตี, 2=heal, 3=ป้องกัน): ")
    if action == "1":
        npc1.attack(npc2)
    elif action == "2":
        npc1.heal()
    elif action == "3":
        npc1.defend()
    else:
        print("กรุณาเลือก 1, 2 หรือ 3")
        continue

    if npc2.hp <= 0:
        print(f"{npc2.name} พ่ายแพ้แล้ว!")
        break

    # Orc เลือกสุ่มการกระทำ
    import random
    orc_action = random.choice(["1", "2", "3"])
    if orc_action == "1":
        npc2.attack(npc1)
    elif orc_action == "2":
        npc2.heal()
    elif orc_action == "3":
        npc2.defend()

    if npc1.hp <= 0:
        print(f"{npc1.name} พ่ายแพ้แล้ว!")
        break