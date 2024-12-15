# Učím se používat třídy, a provázat je mezi sebou.
"""
Pro jednoduchost a orientaci nechávám vše v jednom souboru.
Cílem naprogramovat 3 třídy Auto které má Motor aby mohlo jet,
Řidič který může řídit Auto.
"""

class Motor:

    def __init__(self, vykon, objem):
        self.vykon = vykon
        self.objem = objem

    def __str__(self):
        return f"-Motor o výkonu {self.vykon} koní a objemu {self.objem} cm2.\n"

class Auto:
    def __init__(self, barva, znacka, max_rychlost):
        self.barva = barva
        self.znacka = znacka
        self.max_rychlost = max_rychlost
        self.motor = '-Bez motoru'
        self.jede = False
        self.rychlost = 0

    def __str__(self):
        return f"-{self.znacka}, barva {self.barva}.\n{self.motor}\n"

    def start(self):
        self.jede = True
        return 'Auto nastartováno jízda zahájena.'

    def vypnout(self):
        if self.rychlost > 0:
            return "Nejprve musíš zabrzdit.\n"
        else:
            self.jede = False
            return 'Jízda ukončena.'


    def zrychli(self):
        if self.jede:
            pridej = int(input("Zadej o kolik km/h chceš přidat: "))
            if self.rychlost + pridej > self.max_rychlost:
                self.rychlost = self.max_rychlost
                return "Dosaženo maximální rychlosti.\n"
            self.rychlost += pridej
            return ""
        return "Nastartuj"

    def brzdi(self):
        if self.jede:
            if self.rychlost > 0:
                uber = int(input("Zadej o kolik km/h chceš zpomalit: "))
                if uber > self.rychlost:
                    self.rychlost = 0
                    print("")
                else:
                    self.rychlost -= uber
                    print("")
            else:
                print("Stojíš")
        else:
            print("Nastartuj")

    def pridat_motor(self, novy_motor):
        self.motor = novy_motor

class Ridic:
    def __init__(self, jmeno, vek, auto = None):
        self.jmeno = jmeno
        self.vek = vek
        self.auto = auto

    def __str__(self):
        return f"-Řidič {self.jmeno} majitel vozu:\n-{self.auto if self.auto else 'Zatím bez auta\n'}"

    def rid(self):
        if self.auto.motor != '-Bez motoru':
            print(self.auto.start())
            while self.auto.jede:
                print(f"Aktuální rychlost: {self.auto.rychlost} km/h")
                ukon = input("Zadej: 1) Pridej, 2) Brzdi, 3) Ukonči jízdu: ")
                match ukon:
                    case "1":
                        print(self.auto.zrychli())
                    case "2":
                        self.auto.brzdi()
                    case "3":
                        print(self.auto.vypnout())
                    case _:
                        print('Neplatná volba\n')
            return ""

        return 'Auto bez motoru není pojízdné.\n'


# Test funkčnosti kodu...vytvoření instancí a zahájení jízdy auta bez motoru, následně přidán motor a opětovné zahájení.

motor = Motor(175, 1200)
print("TEST vytvoření instance, Motor:")
print(motor)
skoda = Auto("červená", "Škoda", 220)
print("TEST vytvoření instance, Auto:")
print(skoda)
ridic = Ridic("Kami", 19)
print("TEST vytvoření instance, Ridic:")
print(ridic)
ridic.auto = skoda
print("TEST vyjimky u metody Ridice rid():")
print(ridic.rid())
skoda.pridat_motor(motor)
print("TEST metody Auta pridat_motor():")
print(skoda)
print("TEST simulace jízdy metody Ridice rid():")
print(ridic.rid())

