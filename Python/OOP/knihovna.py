# Trida Kniha predstavuje jednotlive knihy v knihovne
class Kniha:

    def __init__(self, nazev, autor, rok, zanr):
        # Inicializace vlastnosti knihy
        self.nazev = nazev
        self.autor = autor
        self.rok = rok
        self.zanr = zanr
        self.cislo = None  # Prideleno pri pridani knihy do knihovny
        self.dostupnost = True  # True, pokud je kniha dostupna k zapujceni

    def __str__(self):
        # Prevod objektu na textovou reprezentaci
        return (f"{self.autor} - {self.nazev} | č.{self.cislo} | {self.rok} | {self.zanr}\nDostupná: "
                f"{"ANO" if self.dostupnost else "NE"}")


# Trida Ctenar predstavuje ctenare knihovny
class Ctenar:

    def __init__(self, jmeno, prijmeni):
        # Inicializace vlastnosti ctenare
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.cislo = None  # Prideleno pri registraci ctenare do knihovny
        self.zapujceno = []  # Seznam zapujcenych knih

    def __str__(self):
        # Prevod objektu na textovou reprezentaci
        return (f"{self.cislo}) {self.jmeno} {self.prijmeni}\nZapůjčeno: "
                f"{" | ".join(x.nazev for x in self.zapujceno) if self.zapujceno else "NIC"}")


# Trida Knihovna obsluhuje knihy a ctenare
class Knihovna:

    def __init__(self):
        # Inicializace seznamu ctenaru a knih
        self.ctenari = []
        self.knihy = []

    def pridej_knihu(self, kniha):
        # Prida knihu do knihovny a priradi ji cislo
        kniha.cislo = len(self.knihy)
        self.knihy.append(kniha)

    def pridej_ctenare(self, ctenar):
        # Prida ctenare do knihovny a priradi mu cislo
        ctenar.cislo = len(self.ctenari)
        self.ctenari.append(ctenar)

    def najdi_knihu(self, hledany_vyraz):
        # Hleda knihy podle hledaneho vyrazu ve vsech vlastnostech knihy
        nalezeno = []
        for kniha in self.knihy:
            if hledany_vyraz.lower() in kniha.__str__().lower():
                nalezeno.append(str(kniha))
        return "\n".join(nalezeno)

    def pujc_knihu(self, ctenar_cislo, kniha_cislo):
        # Zapujci knihu ctenari, pokud je dostupna
        if self.knihy[kniha_cislo].dostupnost:
            self.ctenari[ctenar_cislo].zapujceno.append(self.knihy[kniha_cislo])
            self.knihy[kniha_cislo].dostupnost = False
            return f"Půjčeno {self.knihy[kniha_cislo].nazev}, čtenáři č.{self.ctenari[ctenar_cislo]}"
        return "Kniha je vypůjčena, operace neproběhla."

    def vrat_knihu(self, ctenar_cislo, kniha_cislo):
        # Vrati knihu od ctenare, pokud ji ma zapujcenou
        if self.knihy[kniha_cislo] in self.ctenari[ctenar_cislo].zapujceno:
            self.ctenari[ctenar_cislo].zapujceno.remove(self.knihy[kniha_cislo])
            self.knihy[kniha_cislo].dostupnost = True
            return f"Vráceno {self.knihy[kniha_cislo].nazev}, čtenářem č.{self.ctenari[ctenar_cislo]}"
        return "Čtenář nemá knihu půjčenou, operace neproběhla."


# Vytvoreni objektu knihovny
knihovna = Knihovna()

# Seznam knih k pridani do knihovny
knihy = [
    Kniha("1984", "George Orwell", 1949, "Sci-fi"),
    Kniha("Hrabě Monte Cristo", "Alexandre Dumas", 1844, "Historický román"),
    Kniha("Na západní frontě klid", "Erich Maria Remarque", 1929, "Válečný román"),
    Kniha("Pýcha a předsudek", "Jane Austenová", 1813, "Román"),
    Kniha("Mistr a Markétka", "Michail Bulgakov", 1940, "Magický realismus"),
    Kniha("Hobit", "J.R.R. Tolkien", 1937, "Fantasy"),
    Kniha("Sto let samoty", "Gabriel García Márquez", 1967, "Magický realismus"),
    Kniha("Alchymista", "Paulo Coelho", 1988, "Filozofický román"),
    Kniha("Malý princ", "Antoine de Saint-Exupéry", 1943, "Povídka"),
    Kniha("Metamorfóza", "Franz Kafka", 1915, "Existenciální román")
]

# Seznam ctenaru k registraci
ctenari = [
    Ctenar("Jan", "Novák"),
    Ctenar("Marie", "Svobodová"),
    Ctenar("Petr", "Novotný"),
    Ctenar("Jana", "Novotná"),
    Ctenar("Tomáš", "Kučera"),
    Ctenar("Eva", "Dvořáková"),
    Ctenar("Martin", "Veselý"),
    Ctenar("Tereza", "Horáková"),
    Ctenar("Michal", "Neumann"),
    Ctenar("Lenka", "Králová")
]

# Pridani knih do knihovny
for kniha in knihy:
    knihovna.pridej_knihu(kniha)

# Pridani ctenaru do knihovny
for ctenar in ctenari:
    knihovna.pridej_ctenare(ctenar)

# Testovani funkci knihovny
print("\nTEST vypsání knihy z knihovny:")
print(knihovna.knihy[9])
print("\nTEST vypsání čtenáře z knihovny:")
print(knihovna.ctenari[3])
print("\nTEST metody najdi_knihu() na výrazu 'ma':")
print(knihovna.najdi_knihu("ma"))
print("\nTEST metody pujc_knihu():")
print(knihovna.pujc_knihu(5, 5))
print("\nTEST metody vrat_knihu():")
print(knihovna.vrat_knihu(5, 6))
print("\nTEST metody vrat_knihu():")
print(knihovna.vrat_knihu(5, 5))













