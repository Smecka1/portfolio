from fighter_parrent import Fighter
import random
import time

class Warrior(Fighter):
    """
    🛡️ Warrior
      - Attributes
          HP = 260
          Power = 40
      - Abilities
          Iron Skin: Reduces damage of the next attack received in 50% and regenerate your health by 40 points. (buff)
          Blade Storm: Attacks with a power of 75 points.(special attack)
    """
    def __init__(self, name, power=40, hp=260):
        super().__init__(name, power, hp)
        self.shield = False

    def defense(self, hurt):
        time.sleep(2)
        shield = ""
        if self.shield:
            shield = " / shield inactive"
            hurt = int(hurt / 2)
            self.shield = False
        if self.hp - hurt <= 0:
            self.hp -= hurt
            return f"{self.name} DIED!\n"
        self.hp -= hurt
        return f"{self.name} HP = {self.hp}{shield}\n"

    def action(self, oponent):
        attack_type = random.randint(0, 2)
        time.sleep(2)
        match attack_type:
            case 0:
                self.shield = True
                self.hp = self.hp + 40 if (self.hp + 40 < self.maxhp) else self.maxhp
                print(f"Iron Skin:\n{self.name}", end=" ")
                time.sleep(1)
                return f"=> HP = {self.hp} / shield activated\n"
            case 1:
                print(f"Blade storm:\n{self.name} attacks: {75}")
                return oponent.defense(75)
            case 2:
                print(f"Basic:\n{self.name} attacks: {self.power}")
                return oponent.defense(self.power)


