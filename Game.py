## Game Player vs Enemy
import random

class Weapon:
    def __init__(self, name, atk_bonus, mana_bonus, mana_cost):
        self.name = name
        self.atk_bonus = atk_bonus
        self.mana_bonus = mana_bonus
        self.mana_cost = mana_cost

class NPC:
    def __init__(self, name, hp, mana, can_rest):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.can_rest = can_rest
        self.is_defending = False
        self.is_dashing = False

    def attack(self, target, atk_type="normal"):
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
        damage = 40

        # Enemy attack type
        if atk_type == "stab":
            print(f"{self.name} ใช้ท่า 'แทง'!")
        elif atk_type == "slash":
            print(f"{self.name} ใช้ท่า 'ฟัน'!")
        elif atk_type == "pierce":
            print(f"{self.name} ใช้ท่า 'ทะลุ'!")

        # Player defend/dash logic
        if hasattr(target, "last_action"):
            if atk_type == "stab":
                if target.last_action == "dash":
                    if target.dash_success:
                        print(f"{target.name} หลบการแทงได้!")
                        return
                print(f"{target.name} ไม่สามารถป้องกันการแทงได้!")
            elif atk_type == "slash":
                if target.last_action == "defend":
                    damage = int(damage * 0.4)
                    print(f"{target.name} ป้องกันการฟัน! ความเสียหายลดลงเหลือ {damage}")
                elif target.last_action == "dash":
                    print(f"{target.name} ไม่สามารถหลบการฟันได้!")
            elif atk_type == "pierce":
                if target.last_action == "dash" and target.dash_success:
                    print(f"{target.name} หลบการทะลุได้!")
                    return
                print(f"{target.name} ไม่สามารถป้องกันการทะลุได้!")
            # reset dash success
            target.dash_success = False

        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name} โจมตี {target.name}! {target.name} HP: {target.hp}")

    def heal(self):
        if self.hp <= 0:
            print(f"{self.name} cannot heal. No HP left!")
            return
        self.hp += 10
        print(f"{self.name} heals for 10 HP! Current HP: {self.hp}")

    def defend(self):
        self.is_defending = True
        print(f"{self.name} is defending this turn!")

    def dash(self):
        self.is_dashing = True
        print(f"{self.name} พยายาม Dash หลบการโจมตี!")

    def rest(self):
        if self.can_rest:
            self.hp += 5
            self.mana += 10
            print(f"{self.name} rests and recovers 5 HP and 10 Mana! Current HP: {self.hp}, Mana: {self.mana}")
        else:
            print(f"{self.name} cannot rest. Resting state is not enabled.")

class Player(NPC):
    def __init__(self, name, hp, mana, can_rest, weapon):
        super().__init__(name, hp, mana, can_rest)
        self.weapon = weapon
        self.last_action = None
        self.dash_success = False

    def attack(self, target, atk_type="normal"):
        if self.hp <= 0:
            print(f"{self.name} cannot attack. No HP left!")
            return
        if self.mana < self.weapon.mana_cost:
            print(f"{self.name} cannot attack. Not enough mana!")
            return
        if target.hp <= 0:
            print(f"{target.name} has already been defeated!")
            return

        self.mana -= self.weapon.mana_cost
        damage = 40 + self.weapon.atk_bonus
        print(f"{self.name} โจมตีด้วย {self.weapon.name}! (ATK+{self.weapon.atk_bonus}, Mana Cost {self.weapon.mana_cost})")

        # Enemy defend/dash logic
        if hasattr(target, "last_action"):
            if target.last_action == "defend":
                damage = int(damage * 0.4)
                print(f"{target.name} ป้องกัน! ความเสียหายลดลงเหลือ {damage}")
            elif target.last_action == "dash" and target.dash_success:
                print(f"{target.name} หลบการโจมตีได้!")
                target.dash_success = False
                return

        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name} โจมตี {target.name}! {target.name} HP: {target.hp}")

    def heal(self):
        if self.hp <= 0:
            print(f"{self.name} cannot heal. No HP left!")
            return
        self.hp += 20
        print(f"{self.name} heals for 20 HP! Current HP: {self.hp}")

    def defend(self):
        self.last_action = "defend"
        print(f"{self.name} is defending this turn!")

    def dash(self):
        self.last_action = "dash"
        self.dash_success = random.random() < 0.4
        if self.dash_success:
            print(f"{self.name} Dash สำเร็จ! มีโอกาสหลบการโจมตี 100% ในรอบนี้")
        else:
            print(f"{self.name} Dash ไม่สำเร็จ!")

    def rest(self):
        if self.can_rest:
            self.hp += 5
            self.mana += 10
            print(f"{self.name} rests and recovers 5 HP and 10 Mana! Current HP: {self.hp}, Mana: {self.mana}")
        else:
            print(f"{self.name} cannot rest. Resting state is not enabled.")

# เลือกอาวุธ
weapons = [
    Weapon("หมัด", 90, 900, 0),
    Weapon("ดาบ", 450, 300, 20),
    Weapon("ธนู", 150, 700, 30)
]
print("เลือกอาวุธ:")
for i, w in enumerate(weapons, 1):
    print(f"{i}. {w.name} (ATK+{w.atk_bonus}, Mana+{w.mana_bonus}, Mana Cost {w.mana_cost}/attack)")
choice = input("เลือกอาวุธ (1-3): ")
weapon = weapons[int(choice)-1]

# status
player = Player("Player", 1100, 150 + weapon.mana_bonus, True, weapon)
enemy = NPC("Enemy", 12000, 300, True)
enemy.last_action = None
enemy.dash_success = False

while player.hp > 0 and enemy.hp > 0:
    print(f"\n{player.name} (HP: {player.hp}, Mana: {player.mana})")
    print(f"{enemy.name} (HP: {enemy.hp}, Mana: {enemy.mana})")
    print("1=โจมตี, 2=heal, 3=ป้องกัน, 4=พักผ่อน, 5=Dash หลบ")
    action = input("เลือกการกระทำของ Player: ")
    player.last_action = None
    if action == "1":
        player.attack(enemy)
        player.last_action = "attack"
    elif action == "2":
        player.heal()
        player.last_action = "heal"
    elif action == "3":
        player.defend()
    elif action == "4":
        player.rest()
        player.last_action = "rest"
    elif action == "5":
        player.dash()
    else:
        print("การกระทำไม่ถูกต้อง กรุณาเลือก 1-5")
        continue

    if enemy.hp <= 0:
        print(f"{enemy.name} พ่ายแพ้แล้ว!")
        break

    # Enemy เลือกสุ่มการกระทำ
    enemy_action = random.choice(["stab", "slash", "pierce"])
    enemy.last_action = None
    if enemy_action == "stab":
        enemy.attack(player, atk_type="stab")
        enemy.last_action = "attack"
    elif enemy_action == "slash":
        enemy.attack(player, atk_type="slash")
        enemy.last_action = "attack"
    elif enemy_action == "pierce":
        enemy.attack(player, atk_type="pierce")
        enemy.last_action = "attack"

    if player.hp <= 0:
        print(f"{player.name} พ่ายแพ้แล้ว!")
        break