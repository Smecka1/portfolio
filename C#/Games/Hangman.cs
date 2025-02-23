using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Games
    {
    // Class representing the Hangman game, inheriting from AbstractGame
    class Hangman : AbstractGame
        {
        // List of possible words for the game
        private string[] words = {"ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra",
                                  "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox",
                                  "frog", "goat", "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose",
                                  "mouse", "mule", "newt", "otter", "owl", "panda", "parrot", "pigeon", "python",
                                  "rabbit", "ram", "rat", "raven", "rhino", "salmon", "seal", "shark", "sheep", "skunk",
                                  "sloth", "snake", "spider", "stork", "swan", "tiger", "toad", "trout", "turkey",
                                  "turtle", "weasel", "whale", "wolf", "wombat", "zebra", "buffalo", "chameleon",
                                  "dolphin", "elephant", "flamingo", "gazelle", "hedgehog", "iguana", "jaguar",
                                  "kangaroo", "lemur", "meerkat", "narwhal", "octopus", "penguin", "quokka", "raccoon",
                                  "scorpion", "tapir", "urchin", "vulture", "walrus", "yak"};

        // Stores the randomly selected word for the game
        private string guessedWord;
        // Stores the current visualization of the word with guessed letters
        private string guessedWordVisualized;
        // Tracks the number of wrong guesses
        private int wrongGuess;
        // Array representing the hangman stages for drawing
        private string[] hangmanStages =
            {
            @"
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========",
            @"
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========",
            @"
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========",
            @"
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========",
            @"
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========",
            @"
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========",
            @"
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            ========="
            };

        // Override the WelcomeAndRules method to display rules for Hangman
        protected override void WelcomeAndRules()
            {
            Console.WriteLine("                        Welcome in GAME - Hangman");
            Console.WriteLine("---------------------------------------------------------------------------------");
            Console.WriteLine("- guess the hidden word by suggesting letters, one at a time");
            Console.WriteLine("- computer choose a word, and You try to guess it");
            Console.WriteLine("- if the guessed letter is in the word, it is revealed in the correct positions");
            Console.WriteLine("- if the guessed letter is not in the word, a part of the \"hangman\" is drawn");
            Console.WriteLine("- game ends when You either guesses all the letters correctly or\n  the \"hangman\" drawing is completed");
            Console.WriteLine("\nPress any key to Start...");
            Console.ReadKey();
            }

        // Initialize the game with a random word and reset the wrong guess count
        private void InicializeGame()
            {
            guessedWord = words[random.Next(words.Length)]; // Randomly choose a word from the list
            guessedWordVisualized = new string('*', guessedWord.Length); // Display the word as hidden
            wrongGuess = 0; // Initialize wrong guesses count
            }

        // Return the current stage of the hangman drawing based on wrong guesses
        private string DrawHangman()
            {
            return hangmanStages[wrongGuess];
            }

        // Return the current visualization of the word with correctly guessed letters
        private string WordVisualized()
            {
            Console.WriteLine($"[DEBUG] Guessed word: {guessedWord}");
            Console.WriteLine("Note: For real game behavior, check Hangman.cs -> method: WordVisualized()\n");
            return $" {guessedWordVisualized}"; // Shows the current state of the guessed word
            }

        // Clear the screen and display the hangman and the word's visualization
        private void NewScreen()
            {
            Console.Clear();
            Console.WriteLine(DrawHangman()); // Draw the hangman stage
            Console.WriteLine();
            Console.WriteLine(WordVisualized()); // Display the current state of the word
            }

        // Prompt the player to input a letter and validate it
        private char GetPlayerGuess()
            {
            char guess = ' ';
            bool guessGot = false;

            while (!guessGot)
                {
                Console.Write("\nEnter a letter: ");
                string input = Console.ReadLine();

                if (!string.IsNullOrEmpty(input) && input.Length == 1 && Char.IsLetter(input[0]))
                    {
                    guess = Char.ToLower(input[0]); // Convert to lowercase
                    guessGot = true;
                    }
                else
                    {
                    Console.WriteLine("Invalid input! Please enter a single letter");
                    }
                }

            return guess;
            }

        // Check if the guessed letter is in the word
        private void IsLetterInWord(char playerGuess)
            {
            if (guessedWord.Contains(playerGuess)) // If the letter is in the word
                {
                char[] guessedArray = guessedWordVisualized.ToCharArray();

                for (int i = 0; i < guessedWord.Length; i++)
                    {
                    if (guessedWord[i] == playerGuess) 
                        {
                        guessedArray[i] = playerGuess; // Reveal the guessed letter in the correct position
                        }
                    }

                guessedWordVisualized = string.Join("", guessedArray); // Update the word's visualization
                }
            else
                {
                wrongGuess++; // Increase wrong guess count to draw one more part of the hangman
                }
            }

        // Check if the game has ended (either the word is guessed or the hangman is fully drawn)
        private bool EndOfGame()
            {
            if (wrongGuess == 6 || !guessedWordVisualized.Contains('*')) // If hangman is complete or all letters are guessed
                {
                return true;
                }
            return false;
            }

        // Main game loop, allowing the player to guess letters and play until the game ends
        public override void RunApp()
            {
            Console.Clear();
            WelcomeAndRules(); // Show game rules and instructions
            bool run = true;

            while (run)
                {
                InicializeGame(); // Start a new game
                bool end = EndOfGame();

                while (!end)
                    {
                    NewScreen(); // Display current game status
                    char letter = GetPlayerGuess(); // Get player's guess
                    IsLetterInWord(letter); // Check if the guess is correct
                    end = EndOfGame(); // Check if the game should end
                    }
                NewScreen();
                string result = wrongGuess == 6 ? $" {guessedWord}\n\n You Loose" : "\n You WIN";
                Console.WriteLine(result); // Display the result: Win or Lose
                Console.WriteLine("\nPlay again?");
                run = YesOrNo(); // Ask if the player wants to play again
                }
            ShowEndScreen(); // Show the end screen when the game finishes
            }
        }
    }
