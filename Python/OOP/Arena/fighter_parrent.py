import random
import time

class Fighter:

    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.maxhp = hp
        self.hp = hp

    def defense(self, hurt):
        time.sleep(2)
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
                pass
            case 1:
                pass
            case 2:
                print(f"Basic:\n{self.name} attacks: {self.power}")
                return oponent.defense(self.power)
        



