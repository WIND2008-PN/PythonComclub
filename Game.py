# PlayerBattleGame.py
import random
import sys

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
        self.ult_ready = False
        self.ult_active = False
        self.last_action = None
        self.dash_success = False

    def attack(self, target, atk_type="normal", extra_atk=0):
        if self.hp <= 0:
            print(f"{self.name} cannot attack. No HP left!")
            return
        if self.mana < 5:
            print(f"{self.name} cannot attack. Not enough mana!")
            return
        if target.hp <= 0:
            print(f"{target.name} has already been defeated!")
            return

        self.mana -= random.randint(10, 100)
        damage = random.randint(40, 100) + extra_atk

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
            target.dash_success = False

        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name} โจมตี {target.name}! {target.name} HP: {target.hp}")

    def heal(self):
        if self.hp <= 0:
            print(f"{self.name} cannot heal. No HP left!")
            return
        heal_amount = random.randint(30, 100)
        self.hp += heal_amount
        print(f"{self.name} heals for {heal_amount} HP! Current HP: {self.hp}")

    def defend(self):
        self.is_defending = True
        print(f"{self.name} is defending this turn!")

    def dash(self):
        self.is_dashing = True
        print(f"{self.name} พยายาม Dash หลบการโจมตี!")

    def rest(self):
        if self.can_rest:
            hp_gain = random.randint(10, 50)
            mana_gain = random.randint(40, 100)
            self.hp += hp_gain
            self.mana += mana_gain
            print(f"{self.name} rests and recovers {hp_gain} HP and {mana_gain} Mana! Current HP: {self.hp}, Mana: {self.mana}")
        else:
            print(f"{self.name} cannot rest. Resting state is not enabled.")

class Player(NPC):
    def __init__(self, name, hp, mana, can_rest, weapon):
        super().__init__(name, hp, mana, can_rest)
        self.weapon = weapon
        self.last_action = None
        self.dash_success = False
        self.ult_ready = False
        self.ult_active = False

    def attack(self, target, atk_type="normal", extra_atk=0):
        if self.hp <= 0:
            print(f"{self.name} cannot attack. No HP left!")
            return
        mana_cost = self.weapon.mana_cost
        if self.ult_active:
            mana_cost += 100
        if self.mana < mana_cost:
            print(f"{self.name} cannot attack. Not enough mana!")
            return
        if target.hp <= 0:
            print(f"{target.name} has already been defeated!")
            return

        self.mana -= mana_cost
        damage = 40 + self.weapon.atk_bonus + extra_atk
        if self.ult_active:
            damage += 500
            print(f"ท่าไม้ตาย! เพิ่มพลังโจมตี +500 และ +1000 HP")
            self.hp += 1000
            self.ult_active = False

        print(f"{self.name} โจมตีด้วย {self.weapon.name}! (ATK+{self.weapon.atk_bonus}, Mana Cost {mana_cost})")

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
        heal_amount = random.randint(30, 100)
        self.hp += heal_amount
        print(f"{self.name} heals for {heal_amount} HP! Current HP: {self.hp}")

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
            hp_gain = random.randint(10, 50)
            mana_gain = random.randint(40, 100)
            self.hp += hp_gain
            self.mana += mana_gain
            print(f"{self.name} rests and recovers {hp_gain} HP and {mana_gain} Mana! Current HP: {self.hp}, Mana: {self.mana}")
        else:
            print(f"{self.name} cannot rest. Resting state is not enabled.")

    def ultimate(self):
        if self.mana < 100:
            print("มานาไม่พอสำหรับท่าไม้ตาย!")
            return False
        self.ult_active = True
        print("ท่าไม้ตายจะถูกใช้ในการโจมตีครั้งถัดไป!")
        return True

# ระบบเริ่มเกม/ออกเกม
def main_menu():
    print("==== เกมต่อสู้ ====")
    print("1. เริ่มเกม")
    print("2. ออกจากเกม")
    choice = input("เลือกเมนู: ")
    if choice == "1":
        return True
    elif choice == "2":
        print("ออกจากเกม")
        sys.exit()
    else:
        print("กรุณาเลือก 1 หรือ 2")
        return main_menu()

# ระบบสุ่มอาวุธ
def choose_weapon():
    holy_sword_chance = random.random()
    if holy_sword_chance < 0.01:
        print("** คุณได้รับอาวุธพิเศษ Holy sword! **")
        return Weapon("Holy sword", 10000, 0, 999)
    weapons = [
        Weapon("หมัด", 90, 900, 0),
        Weapon("ดาบ", 450, 300, 20),
        Weapon("ธนู", 150, 700, 30)
    ]
    print("เลือกอาวุธ:")
    for i, w in enumerate(weapons, 1):
        print(f"{i}. {w.name} (ATK+{w.atk_bonus}, Mana+{w.mana_bonus}, Mana Cost {w.mana_cost}/attack)")
    choice = input("เลือกอาวุธ (1-3): ")
    return weapons[int(choice)-1]

# ระบบสุ่มศัตรู
def random_enemy():
    enemies = [
        ("Goblin", 12000, 4000, 0.3),
        ("Orc", 20000, 3000, 0.2),
        ("Giant", 40000, 5000, 0.1),
        ("Dragon", 1200000, 40000, 0.05),
        ("God", 9999999, 999999, 0.001)
    ]
    idx = random.randint(0, len(enemies)-1)
    name, hp, mana, escape_chance = enemies[idx]
    print(f"คุณพบกับศัตรู: {name} (HP: {hp}, Mana: {mana})")
    return NPC(name, hp, mana, True), escape_chance

# เริ่มเกม
if main_menu():
    weapon = choose_weapon()
    player = Player("Player", 1100, 150 + weapon.mana_bonus, True, weapon)
    enemy, escape_chance = random_enemy()
    enemy.last_action = None
    enemy.dash_success = False

    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name} (HP: {player.hp}, Mana: {player.mana})")
        print(f"{enemy.name} (HP: {enemy.hp}, Mana: {enemy.mana})")

        # โอกาส 10% สำหรับท่าไม้ตาย
        ult_available = random.random() < 0.1
        if ult_available:
            print("** ท่าไม้ตายพร้อมใช้งาน! (พิมพ์ 6 เพื่อใช้ท่าไม้ตาย) **")

        print("0=หนี, 1=โจมตี, 2=heal, 3=ป้องกัน, 4=พักผ่อน, 5=Dash หลบ", end="")
        if ult_available:
            print(", 6=ท่าไม้ตาย")
        else:
            print()
        action = input("เลือกการกระทำของ Player: ")
        player.last_action = None

        if action == "0":
            if random.random() < escape_chance:
                print("คุณหนีสำเร็จ! จบเกม")
                sys.exit()
            else:
                print("หนีไม่สำเร็จ! ศัตรูโจมตีฟรี!")
                # Enemy โจมตีฟรี
                enemy_action = random.choice(["stab", "slash", "pierce"])
                enemy.attack(player, atk_type=enemy_action)
                if player.hp <= 0:
                    print(f"{player.name} พ่ายแพ้แล้ว!")
                    break
                continue
        elif action == "1":
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
        elif action == "6" and ult_available:
            if player.ultimate():
                player.last_action = "ult"
            else:
                continue
        else:
            print("การกระทำไม่ถูกต้อง กรุณาเลือก 0-6")
            continue

        if enemy.hp <= 0:
            print(f"{enemy.name} พ่ายแพ้แล้ว!")
            break

        # Enemy เลือกสุ่มการกระทำ
        enemy_action = random.choice(["stab", "slash", "pierce"])
        enemy.last_action = None
        enemy.attack(player, atk_type=enemy_action)

        if player.hp <= 0:
            print(f"{player.name} พ่ายแพ้แล้ว!")
            break