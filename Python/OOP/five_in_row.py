class FiveInRow:

    def __init__(self, rows = 16, columns = 18):
        # Initialize the game board with the given number of rows and columns
        self.rows = rows
        self.columns = columns
        self.activ_player_sign = " X"   # Set the starting player
        self.field = [[f"{i:>2}" for i in range(columns + 1)]]  # Create the column headers
        for i in range(1 , rows + 1):
            # Create the game board with row numbers and empty cells represented by ". "
            next_row = [f"{i:>2}"] + [". " for _ in range(columns)]
            self.field.append(next_row)

    def welcome_screen(self):
        # Giving informatins about game rules
        print(f"\n               VÍTEJ VE HŘE PIŠKVORKY")
        print("-hrači O a X se střídají v zadávaní svých znaků do tabulky")
        print("-první kdo dosáhne nepřerušené řady 5 svých znaků vyhrál")
        input("-------------Zmáčkni Enter pro zahájení hry--------------")

    def print_field(self):
        # Print the current state of the game board
        for row in self.field:
            print(" ".join(row))

    def player_switch(self):
        # Switch the active player between "X" and "O"
        if self.activ_player_sign == " O":
            self.activ_player_sign = " X"
        else:
            self.activ_player_sign = " O"

    def player_choice(self):
        # Handle the player's move
        y, x = False, False
        self.player_switch()
        while not (x and y):
            # Loop until valid input is received
            try:
                print(f"NA TAHU JE HRÁČ:{self.activ_player_sign}")
                y = int(input("Zadej č.řádku: "))
                x = int(input("Zadej sloupec: "))
            except ValueError:
                print("CHYBNÉ ZADÁNÍ! (Zadej číslo)")
                continue
            if not (0 < y < self.rows + 1) or not(0 < x < self.columns + 1):
                # Ensure the input is within the board's range
                print("CHYBNÉ ZADÁNÍ! (Zadej souřadnice uvnitř hracího pole)")
                y, x = False, False
            elif self.field[y][x] != ". ":
                # Check if the selected cell is already occupied
                print("CHYBNÉ ZADÁNÍ! (Zadal jsi obsazené pole)")
                y, x = False, False
            else:
                # Mark the cell with the active player's symbol
                self.field[y][x] = self.activ_player_sign

        self.print_field()  # Display the updated game board
        return y, x

    def row_checker(self, row, column):
        # Check for a winning sequence in the row
        sign_chain = 0
        for i in range(column - 4, column + 5):
            if i > self.columns:
                continue
            if self.field[row][i] == self.activ_player_sign:
                sign_chain += 1
                if sign_chain == 5:
                    return True
            else:
                sign_chain = 0
        return False

    def column_checker(self, row, column):
        # Check for a winning sequence in the column
        sign_chain = 0
        for i in range(row - 4, row + 5):
            if i > self.rows:
                continue
            if self.field[i][column] == self.activ_player_sign:
                sign_chain += 1
                if sign_chain == 5:
                    return True
            else:
                sign_chain = 0
        return False

    def diagonal_checker_left_to_right(self, row, column):
        # Check for a winning sequence in the diagonal (top-left to bottom-right)
        sign_chain = 0
        for i in range(-4, 5):
            if row + i > self.rows or column + i > self.columns:
                continue
            if self.field[row + i][column + i] == self.activ_player_sign:
                sign_chain += 1
                if sign_chain == 5:
                    return True
            else:
                sign_chain = 0
        return False

    def diagonal_checker_right_to_left(self, row, column):
        # Check for a winning sequence in the diagonal (top-right to bottom-left)
        sign_chain = 0
        column = column + 5
        for i in range(-4, 5):
            column -= 1
            if column > self.columns or row + i > self.rows:
                continue
            if self.field[row + i][column] == self.activ_player_sign:
                sign_chain += 1
                if sign_chain == 5:
                    return True
            else:
                sign_chain = 0
        return False

    def win_verification(self, row, column):
        # Verify if the current player has won the game
        return self.row_checker(row, column) or self.column_checker(row, column) or \
           self.diagonal_checker_left_to_right(row, column) or self.diagonal_checker_right_to_left(row, column)

    def run(self):
        # Main game loop
        self.welcome_screen()  # Display instructions
        self.print_field()  # Display the initial empty game board
        winner = False
        while not winner:
            # Continue playing until there is a winner
            row, column = self.player_choice()
            winner = self.win_verification(row, column)
        print(f"\n!!! Vítězem je:{self.activ_player_sign} !!!")


f = FiveInRow(15, 18)
f.run()