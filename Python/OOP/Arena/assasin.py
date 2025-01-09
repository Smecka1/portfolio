from fighter_parrent import Fighter
import random
import time

class Assassin(Fighter):
    """
🗡️️ Assassin
    - Attributes
        HP = 235
        Power = 30
    - Abilities
        Assassin's instinct: Increases your power by 40 points for three attacks. (buff)
        Lacerate: Inflicts the equivalent of 2x your power points. (special attack)
    """
    def __init__(self, name, power=30, hp=235):
        super().__init__(name, power, hp)
        self.instinct = 0

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
                self.instinct = 3
                print(f"Assassin's instinct:\n{self.name} instinct",end=" ")
                time.sleep(1)
                return "=> activated\n"
            case 1:
                print("Lacerate:")
                if self.instinct:
                    self.instinct -= 1
                    print(f"{self.name} attacks: {(self.power + 40) * 2}")
                    return oponent.defense((self.power + 40) * 2)
                print(f"{self.name} attacks: {self.power * 2}")
                return oponent.defense(self.power * 2)
            case 2:
                print("Basic:")
                if self.instinct:
                    self.instinct -= 1
                    print(f"{self.name} attacks: {self.power + 40}")
                    return oponent.defense(self.power + 40)
                print(f"{self.name} attacks: {self.power}")
                return oponent.defense(self.power)

