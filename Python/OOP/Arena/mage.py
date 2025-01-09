from fighter_parrent import Fighter
import random
import time

class Mage(Fighter):
    """
🧙 Mage
    - Attributes
      HP = 200
      Power = 50
    - Abilities
      Arcane Shield: Absorb the next damage received. (buff)
      Fireball: Attacks with a power of 90 points.(special attack)
    """
    def __init__(self, name, power=50, hp=200):
        super().__init__(name, power, hp)
        self.shield = False

    def defense(self, hurt):
        time.sleep(2)
        if self.shield:
            self.shield = False
            return f"{self.name} HP = {self.hp}  / shield inactive\n"
        if self.hp - hurt <= 0:
            self.hp -= hurt
            return f"{self.name} DIED!\n"
        self.hp -= hurt
        return f"{self.name} HP = {self.hp}\n"

    def action(self, oponent):
        attack_type = random.randint(0, 2)
        time.sleep(2)
        match attack_type:
            case 0:
                self.shield = True
                print(f"Arcane Shield:\n{self.name} shield", end=" ")
                time.sleep(1)
                return "=> activated\n"
            case 1:
                print(f"Fireball:\n{self.name} attacks: {90}")
                return oponent.defense(90)
            case 2:
                print(f"Basic:\n{self.name} attacks: {self.power}")
                return oponent.defense(self.power)

