from matplotlib import pyplot as plt


# Kalkulačka složeného úročení
class InvestmentCalculator:
    """
      Třída pro výpočty spojené s investicemi a složeným úročením.
      Poskytuje funkce pro:
      - Výpočet budoucí hodnoty investice s pravidelnými příspěvky a složeným úročením
      - Výpočet potřebné úrokové míry pro dosažení cílové částky
      - Srovnání růstu investice se složeným úročením a bez něj
      """

    def calculate_compound_interest(self, start, monthly, rate, year):
        """
            Vypočítá budoucí hodnotu investice s pravidelnými měsíčními příspěvky a složeným úročením.
            Vykreslí graf vývoje investice s a bez úročení.

            Args:
                start: Počáteční investice
                monthly: Měsíční příspěvek
                rate: Roční úroková míra v procentech
                year: Počet let investování
            """
        actual_balance = start
        without_interest_balance = start
        growth_factor = (rate + 100) / 100

        years = []
        balance_over_time = []
        balance_no_interest = []

        for i in range(1, year + 1):
            actual_balance = (actual_balance + 12 * monthly) * growth_factor
            without_interest_balance = without_interest_balance + 12 * monthly
            years.append(i)
            balance_over_time.append(round(actual_balance/1000000, 1))
            balance_no_interest.append(round(without_interest_balance/1000000, 1))

        print(130 * "=")
        print(f"Pokud by sis peníze pouze spořil, po {year} letech by jsi měl o "
              f"{f"{int(actual_balance - without_interest_balance):,}".replace(",", " ")} Kč míň, "
              f"tedy jen {f"{without_interest_balance:,}".replace(",", " ")}.")

        plt.scatter(years, balance_over_time, label="Složené úročení")
        plt.scatter(years, balance_no_interest, label="Bez úročení")
        plt.legend()
        plt.title("Složené úročení   X   Spoření do kasičky")
        plt.xlabel("Roky")
        plt.ylabel("mil.Kč")
        plt.show()

########################################################################################################################
    def interest_rate_for_suma(self, years, final_sum, yearly, starting_sum):
        """
            Vypočítá potřebnou roční úrokovou míru pro dosažení cílové částky při pravidelných ročních příspěvcích.
            Používá iterativní metodu pro nalezení řešení.

            Args:
                years: Počet let investování
                final_sum: Cílová částka
                yearly: Roční příspěvek
                starting_sum: Počáteční investice

            Returns:
                Řetězec obsahující vypočítanou úrokovou míru.
            """
        rate = 0
        result = 0
        while result < final_sum:
            rate += 0.01
            result = starting_sum * (1 + rate) ** years + yearly * (((1 + rate) ** years - 1) / rate)
            if result > final_sum:
                rate -= 0.01
                while result < final_sum:
                    rate += 0.001
                    result = starting_sum * (1 + rate) ** years + yearly * (((1 + rate) ** years - 1) / rate)
        return f"potřebuješ dosáhnout úroku: {rate * 100:.1f}% ročně."

########################################################################################################################
    def annual_interest_rate(self, years, multiply):
        """
           Vypočítá potřebnou roční úrokovou míru pro zvětšení počáteční investice na konkrétní násobek za počet let.
           Srovnává výpočet pro průběžné roční vklady a jednorázový počáteční vklad.

           Args:
               years: Počet let investování
               multiply: Násobek, kterého chceme dosáhnout

           Returns:
               Řetězec obsahující vypočítané úrokové míry.
           """
        final = years * multiply
        rate = 0
        result = 0
        while result < final:
            rate += 0.01
            num = (((1 + rate) ** years - 1) / rate) * (1 + rate)
            if num > final:
                rate -= 0.01
                while result < final:
                    rate += 0.001
                    result = (((1 + rate) ** years - 1) / rate) * (1 + rate)
        rate_only_one = (multiply ** (1 / years)) - 1
        return (f"Abys dosáhl {multiply}X za {years} let, budeš potřebovat úrokovou míru:\n"
                f"- pro průběžný roční vklad:            {rate * 100:.1f}% ročně\n"
                f"- pro jednorázový počáteční vklad:     {rate_only_one * 100:.1f}% ročně")

########################################################################################################################
    @staticmethod
    def introduce():
        """
        Stručný popis účelu třídy a jednotlivých funkcí.
        """
        print(130 * "=")
        print("Vítej v kalkulačce, díky které pochopíš sílu složeného úročení!")
        print("Vyber si z následujících možností:")
        print(130 * "-")
        print("1) Výpočet složeného úročení: Zjisti, kolik naspoříš během let s úrokem a bez úroku.")
        print("   - Parametry: počáteční investice / měsíční příspěvky / roční úroková míra / počet let")
        print("2) Výpočet ročního úroku: Pokud vím sumu které chci dosáhnout a kolik můžu ročně investovat.")
        print("   - Parametry: cílová částka / počáteční investice / roční příspěvek / počet let")
        print("3) Výpočet ročního úroku: Znáš pouze kilikrát chceš zhodnotit své investice.")
        print("   - Parametry: počet let / násobek kterého chceš dosáhnout")
        print(130 * "=")

########################################################################################################################
    @classmethod
    def user_interface(cls):
        """
        Interaktivní část programu, která umožňuje uživateli zadávat vstupní hodnoty a vybírat požadovanou funkci.
        """
        cls.introduce()
        run = ""
        while run == "":
            print("1) Složené úročení / 2) Úrok k dosažení cíle / 3) Jak velký násobek chceš dosáhnout")
            choice = input("Vyber: 1 / 2 / 3\n")
            investment_calculator = cls()
            match choice:
                case "1":
                    start = float(input("Počáteční investice v Kč: "))
                    monthly = float(input("Měsíční příspěvek v Kč: "))
                    rate = float(input("Předpokládaná roční úroková míra(%): "))
                    year = int(input("Počet let úročení:     "))
                    investment_calculator.calculate_compound_interest(start, monthly, rate, year)
                case "2":
                    starting_sum = float(input("Počáteční investice v Kč: "))
                    yearly = float(input("Roční příspěvek v Kč: "))
                    final_sum = float(input("Požadovaná částka v Kč: "))
                    years = int(input("Počet let úročení: "))
                    print(130 * "=")
                    print(investment_calculator.interest_rate_for_suma(years, final_sum, yearly, starting_sum))
                case "3":
                    years = int(input("Zadej počet let: "))
                    multiply = float(input("Zadej požadovaný násobek: "))
                    print(130 * "=")
                    print(investment_calculator.annual_interest_rate(years, multiply))
                case _:
                    print("Neplatná volba.")
            print(130 * ".")
            run = input("Pokračování = Enter  /  Ukončeníení = libovolná klávesa + Enter:\n")


# Zpuštění interakce
cl = InvestmentCalculator()
InvestmentCalculator.user_interface()
