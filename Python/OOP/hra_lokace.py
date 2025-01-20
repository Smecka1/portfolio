"""
Tento program implementuje jednoduchou textovou adventuru, kde hráč prozkoumává různé lokace
pomocí příkazů pro pohyb (sever, jih, západ, východ). Každá lokace má popis, název a informace
o směrech, kterými se hráč může pohybovat.

Hráč začíná na určité výchozí pozici a může zadávat příkazy k pohybu,
přičemž program kontroluje, zda je pohyb v daném směru možný, a informuje o aktuální lokaci.
Pokud hráč zadá neplatný směr nebo příkaz, dostane zpětnou vazbu. Hra končí zadáním prázdného příkazu (ENTER).
"""

class Lokace:
    def __init__(self, smery, misto, popis):
        self.smery = smery
        self.misto = misto
        self.popis = popis

    def __str__(self):
        return f"{self.misto}\n{self.popis}\nMůžeš jít na {", ".join(self.smery)}\n"

    def kontrola(self, smer):
            return smer in self.smery


class Hra:
    hrad = Lokace(["východ"], "Hrad", "Stojíš před okovanou branou gotického hradu, která je zřejmě jediným vchodem do pevnosti.\nKlíčová dírka je pokryta pavučinami, což vzbuzuje dojem, že je budova opuštěná.")
    les1 = Lokace(["západ", "východ"], "Les", "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce.\nTicho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    les2 = Lokace(["jih", "západ", "východ"], "Lesní rozcestí", "Nacházíš se na lesním rozcestí.")
    les3 = Lokace(["západ", "východ"], "Les", "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce.\nTicho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    rybnik = Lokace(["západ"], "Rybník", "Došel jsi ke břehu malého rybníka. Hladina je v bezvětří jako zrcadlo. Kousek od tebe je dřevěná plošina se stavidlem.")
    les4 = Lokace(["sever", "východ"], "Les", "Jsi na lesní cestě, která se klikatí až za obzor, kde mizí v siluetě zapadajícího slunce.\nTicho podvečerního lesa občas přeruší zpěv posledních ptáků.")
    dum = Lokace(["západ"], "Dům", "Stojíš před svým rodným domem, citíš vůni čerstvě nasekaného dřeva, která se line z hromady vedle vstupních dvěří.")

    rozlozeni = ([hrad, les1, les2, les3, rybnik],
                             [les4, dum])
    y = 1
    x = 1
    pozice = rozlozeni[y][x]

    def pohyb(self, smer):
        if smer == "sever":
            self.y = 0
            self.x = 2
        elif smer == "jih":
            self.y = 1
            self.x = 0
        elif smer == "západ":
            self.x -= 1
        elif smer == "východ":
            self.x += 1
        self.pozice = self.rozlozeni[self.y][self.x]
        return self.pozice

    def interakce(self):
        smer = " "
        while smer != "":
            print(self.pozice)
            smer = input(f"Zadej příkaz ({" | ".join(self.pozice.smery)}) nebo ENTER pro ukončení: ")
            print(150 * '=')
            if smer in self.pozice.smery:
                self.pohyb(smer)
            elif smer == "":
                print("Pohyb ukončen")
            else:
                print("Tímto směrem nelze jít. Zůstáváš na pozici:")




# Zahájení hry
hra = Hra()
hra.interakce()
