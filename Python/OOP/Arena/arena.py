import random
from warior import Warrior
from mage import Mage
from assasin import Assassin


class Arena:
    """
    Represents an arena where fighters compete against each other.
    """

    def __init__(self, fighters):
        self.fighters = fighters  #List of fighter objects (Warrior, Mage, Assassin, etc.)

    def chose_fighters(self):
        """
        Randomly selects two different fighters from the list.
        :return: A list containing two selected fighter objects.
        """
        fighter1 = random.randint(0, len(self.fighters) - 1)  # Select the first fighter randomly.
        fighter2 = random.randint(0, len(self.fighters) - 1)  # Select the second fighter randomly.

        # Ensure the two selected fighters are not the same.
        while fighter1 == fighter2:
            fighter2 = random.randint(0, len(self.fighters) - 1)

        return [self.fighters[fighter1], self.fighters[fighter2]]

    def type_of_fighter(self, fighter):
        """
        Finds out the type of a fighter (Mage, Warrior, or Assassin).
        :return: A string representing the fighter type ("mage", "warrior", or "assassin").
        """
        if isinstance(fighter, Mage):
            return "mage"
        if isinstance(fighter, Warrior):
            return "warrior"
        if isinstance(fighter, Assassin):
            return "assasin"

    def run_arena(self):
        """
        Simulates a fight in the arena until one fighter's health points (hp) reach 0.
        :return: A string declaring the winner.
        """
        oponents = self.chose_fighters()  # Choose two fighters for the battle.

        print("     Today will fight:")
        print("-----------------------------------")
        print(f"     {oponents[0].name} - {self.type_of_fighter(oponents[0])}") # String representation of the first fighter
        print(f"     {oponents[1].name} - {self.type_of_fighter(oponents[1])}\n") # Str. representation of the second fighter

        while oponents[0].hp > 0 and oponents[1].hp > 0:  # Continue the fight until one fighter is defeated.
            print(oponents[0].action(oponents[1]))  # Fighter 1 attacks Fighter 2.
            if oponents[1].hp > 0:  # Check if Fighter 2 is still alive.
                print(oponents[1].action(oponents[0]))  # Fighter 2 attacks Fighter 1.

        # Declare the winner based on which fighter has hp left.
        return f"!!!  {oponents[0].name} WIN  !!!" if oponents[0].hp > 0 else f"!!! {oponents[1].name} WIN !!!"



