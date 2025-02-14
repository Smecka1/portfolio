using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Games
    {
    // Class that represents the Rock, Paper, Scissors game, inheriting from AbstractGame
    class RockPaperScissors : AbstractGame
        {
        // Override WelcomeAndRules method to display game rules for Rock, Paper, Scissors
        protected override void WelcomeAndRules()
            {
            Console.WriteLine("        Welcome in GAME - Rock, Paper, Scissors");
            Console.WriteLine("-------------------------------------------------------------");
            Console.WriteLine("- when prompted, choise: rock, paper, or scissors");
            Console.WriteLine("- the computer also select one of this three options");
            Console.WriteLine("- the game will compare your choice with the computer's choice\n  and display the result.");
            Console.WriteLine("\nPress any key to Start...");
            Console.ReadKey();
            Console.Clear();
            }

        // Method to display the current score of the player and the computer
        private void ScoreTable(int playerScore, int computerScore)
            {
            Console.WriteLine("  ::::::: Score :::::::");
            Console.WriteLine("  ::  You  ::   PC   ::");
            Console.WriteLine($"  ::{playerScore.ToString().PadLeft(4)}   ::   {computerScore.ToString().PadRight(5)}::");
            Console.WriteLine("  :::::::::::::::::::::");
            }


        // Method to convert the numerical choice to a string representation (Rock, Paper, Scissors)
        private string ChoiceToWord(int choice)
            {
            switch (choice)
                {
                case 1:
                    return "Rock";
                case 2:
                    return "Paper";
                case 3:
                    return "Scissors";
                case 4:
                    return "END";
                default:
                    return "Mistake";
                }
            }

        // Method to simulate the computer's choice, randomly selecting one of the three options
        private string ComputerChoice()
            {
            int choice = random.Next(1, 4);

            return ChoiceToWord(choice);
            }

        // Method to determine the result of the game (Win, Draw, or Loss) based on player and computer choices
        private string WhoWin(string player, string computer)
            {
            string text;
            // Determine if it's a draw
            if (player == computer)
                text = "DRAW";
            // Check if the player wins
            else if ((player == "Rock" && computer == "Scissors") 
                || (player == "Paper" && computer == "Rock") 
                || (player == "Scissors" && computer == "Paper"))
                text = "YOU WIN";
            // Otherwise, the computer wins
            else
                text = "COMPUTER WIN";

            return text;
            }

        // Main method to run the game logic
        public override void RunApp()
            {
            Console.Clear();
            WelcomeAndRules(); // Show the welcome message and game rules
            bool end = false; // Variable to track when to end the game
            int playerScore = 0; // Player's score
            int computerScore = 0; // Computer's score
            while (end == false)
                {
                Console.WriteLine("\n1) Rock, 2) Paper, 3) Scissors, 4) END");
                Console.WriteLine("---------------------------------------");
                int playerNumber = ChooseNumber(1, 4); // Prompt player for a choice
                string playerChoice = ChoiceToWord(playerNumber); // Convert player's number to word
                string computerChoice = ComputerChoice(); // Get computer's choice
                if (playerChoice == "END")
                    {
                    end = true; // Set end to true to stop the game loop
                    }                
                else
                    {
                    Console.Clear();
                    // Display the result of the round
                    Console.WriteLine($"\n{WhoWin(playerChoice, computerChoice)} => You: {playerChoice} / Computer: {computerChoice}\n");
                    if (WhoWin(playerChoice, computerChoice) == "YOU WIN")
                        playerScore++; // Increment player's score if they win
                    if (WhoWin(playerChoice, computerChoice) == "COMPUTER WIN")
                        computerScore++; // Increment computer's score if they win
                    ScoreTable(playerScore, computerScore); // Display the updated score
                    }
                }
            ShowEndScreen(); // Show the end screen after the game ends
            }
        }
    }
