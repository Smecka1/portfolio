# Trida reprezentuje jidlo s cenou a nazvem
class Jidlo:
    def __init__(self, cena, nazev):
        self.cena = cena
        self.nazev = nazev

# Trida reprezentuje piti s cenou a nazvem
class Piti:
    def __init__(self, cena, nazev):
        self.cena = cena
        self.nazev = nazev

# Trida reprezentuje cisnika, ktery muze prijimat objednavky
class Cisnik:
    def __init__(self, jmeno):
        self.jmeno = jmeno  # Jmeno cisnika
        self.objednavka = []  # Aktualni objednavka

    # Metoda pro prijem objednavky od zakaznika
    def prijmi_obednavku(self):
        print(f"Dobrý den jsem váš číšník {self.jmeno} a dnes vás budu obspuhovat. Co si dáte?\n")
        self.objednavka = []
        while True:
            # Pozadavek na polozku z menu
            end = input("Objednej si polozku z Menu, nebo zmackni ENTER pro ukonceni objednavky: ")
            if end == "":
                break  # Ukonceni objednavky

            # Hledani polozky v menu
            polozka = menu.najdi_polozku(end)
            if polozka == 0:
                print("Polozka neni v nabidce.")
            else:
                self.objednavka.append(polozka)  # Pridani polozky do objednavky

        # Vypis objednanych polozek a celkove ceny
        pochutiny = []
        celkem = 0
        for pochutina in self.objednavka:
            pochutiny.append(pochutina.nazev)
            celkem += pochutina.cena
        print(f"Vase objednavka je: {', '.join(pochutiny)} a cena bude {celkem}Kc.")

# Trida reprezentuje menu restaurace
class Menu:
    def __init__(self):
        self.jidla = []  # Seznam jidel
        self.napoje = []  # Seznam napoju

    # Pridani jidla do menu
    def pridej_jidlo(self, jidlo):
        self.jidla.append(jidlo)

    # Pridani napoje do menu
    def pridej_napoj(self, napoj):
        self.napoje.append(napoj)

    # Vytvoreni citelneho seznamu jidel a napoju
    def seznam_citelne(self):
        seznam_radku = []
        for jidlo in self.jidla:
            radek = f"{jidlo.nazev:<25}{jidlo.cena}Kc"
            seznam_radku.append(radek)
        for piti in self.napoje:
            radek = f"{piti.nazev:<25}{piti.cena}Kc"
            seznam_radku.append(radek)
        return "\n".join(seznam_radku) + "\n" + (80 * "-")

    # Vyhledani polozky podle nazvu
    def najdi_polozku(self, nazev):
        for jidlo in self.jidla:
            if jidlo.nazev == nazev:
                return jidlo
        for napoj in self.napoje:
            if napoj.nazev == nazev:
                return napoj
        return 0  # Položka nebyla nalezena

    # Reprezentace menu jako textu
    def __str__(self):
        return f"Menu:\n{self.seznam_citelne()}"

# Vytvoreni instance menu
menu = Menu()

# Vytvoreni instance cisnika
cisnik = Cisnik("Karel")

# Pridani polozek do menu
hrachovka = Jidlo(60, "Hrachova kase")
menu.pridej_jidlo(hrachovka)

gulasovka = Jidlo(70, "Gulasova polevka")
menu.pridej_jidlo(gulasovka)

cola = Piti(35, "Coca-Colla")
menu.pridej_napoj(cola)

voda = Piti(20, "Voda")
menu.pridej_napoj(voda)

# Zobrazeni menu a prijem objednavky
print(menu)
cisnik.prijmi_obednavku()

