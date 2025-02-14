using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Games
    {
    // Class that represents the Guess Number game, inheriting from AbstractGame
    class GuessNumber : AbstractGame
        {
        // Override WelcomeAndRules method to display game rules for Guess Number
        protected override void WelcomeAndRules()
            {
            Console.WriteLine("                 Welcome in GAME - Guess Number");
            Console.WriteLine("---------------------------------------------------------------------");
            Console.WriteLine("- the computer will randomly select Number");
            Console.WriteLine("- when prompted, choose number 1-100");
            Console.WriteLine("- the game will compare your choice with the computer's select");
            Console.WriteLine("- return if your choice is lower, higher or same as computer's select");
            Console.WriteLine("- you will get 7 or 9 Lives depend on dificulty, to guess the Number");
            Console.WriteLine("\nPress any key to Start...");
            Console.ReadKey();
            }

        // Method to generate a random number between 1 and 100 (inclusive)
        private int ComputerNumber()
            {
            return random.Next(1, 101);
            }

        // Method to compare the player's guess with the computer's number and return feedback
        private string CompareNumbers(int player, int computer)
            {
            if (player == computer)
                {
                return "WIN"; // If the player's guess is correct
                }
            else if (player < computer)
                {
                return "Too low"; // If the guess is lower than the computer's number
                }
            else
                {
                return "Too high"; // If the guess is higher than the computer's number
                }
            }

        // Method to let the player select the difficulty, which affects the number of lives
        private int SelectDifficulty()
            {
            Console.Clear();
            Console.WriteLine(":: Select Dificulty ::");
            Console.WriteLine(" 1) High: 7 lives");
            Console.WriteLine(" 2) Low:  9 lives\n");
            return ChooseNumber(1, 2); // Prompt the player to select either difficulty
            }

        // Main method to run the game logic
        public override void RunApp()
            {
            Console.Clear();
            WelcomeAndRules(); // Show the welcome message and game rules
            bool run = true; // Variable to track if the game should continue
            while (run)
                {
                int lives = SelectDifficulty() == 1 ? 7 : 9; // Set lives based on difficulty
                bool end = false; // Variable to track if the game has ended
                int guessedNumber = ComputerNumber(); // Generate a random number for the game
                Console.Clear();

                // Game loop where the player has to guess the number
                while (lives > 0 && end == false)
                    {
                    Console.WriteLine($"\nLives: {lives}\n");
                    Console.WriteLine("Guess number from 1 to 100");
                    Console.WriteLine("--------------------------");
                    int playerNumber = ChooseNumber(1, 100); // Prompt the player for a guess
                    Console.WriteLine($"\n{CompareNumbers(playerNumber, guessedNumber)}"); // Provide feedback
                    
                    end = CompareNumbers(playerNumber, guessedNumber) == "WIN" ? true : false; // Check if the player won
                    lives--; // Decrease the number of lives after each guess
                    }

                Console.Clear();
                Console.WriteLine(end ? "YOU WIN!" : "YOU LOOSE!"); // Display whether the player won or lost
                Console.WriteLine($"\nThe number was: {guessedNumber}"); // Show the correct number
                Console.WriteLine("\nPlay Again?\n");
                run = YesOrNo(); // Ask if the player wants to play again
                }
            ShowEndScreen(); // Show the end screen when the game finishes
            }
        }
    }
