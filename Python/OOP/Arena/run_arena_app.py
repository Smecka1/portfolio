from warior import Warrior
from mage import Mage
from assasin import Assassin
from arena import Arena

# Instantiate fighters.
warior = Warrior('Leonidas')  # Create a Warrior named Leonidas.
mage = Mage('Gandalf')        # Create a Mage named Gandalf.
assassin = Assassin('Kutna')  # Create an Assassin named Kutna.

# Create an arena with the fighters.
arena = Arena([warior, mage, assassin])

# Run the arena fight and print the result.
print(arena.run_arena())