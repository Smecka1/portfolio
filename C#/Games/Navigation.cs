using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace Games
    {
    // Class that represents the game selection menu, inheriting from AbstractGame
    class Navigation: AbstractGame
        {
        // Displays the game selection menu
        private void Menu()
            {
            Console.Clear();
            Console.WriteLine(":::::::::::: Choose The Game :::::::::::::");
            Console.WriteLine("::                                      ::");
            Console.WriteLine("::  1) Hangman                          ::");
            Console.WriteLine("::                                      ::");
            Console.WriteLine("::  2) Guess number                     ::");
            Console.WriteLine("::                                      ::");
            Console.WriteLine("::  3) Rock, Paper, Scissors            ::");
            Console.WriteLine("::                                      ::");
            Console.WriteLine("::  4) Quit                             ::");
            Console.WriteLine("::                                      ::");
            Console.WriteLine("::::::::::::::::::::::::::::::::::::::::::\n");
            }

        // Handles quitting the application
        private bool QuitApp()
            {
            return true;
            }

        // Starts the selected game based on user input
        private bool StartGame(int chosenGame)
            {
            Hangman hangman = new Hangman();
            GuessNumber guessNumber = new GuessNumber();
            RockPaperScissors rockPaperScissors = new RockPaperScissors();

            switch (chosenGame)
                {
                case 1:
                    hangman.RunApp(); // Starts Hangman game
                    return false;
                case 2:
                    guessNumber.RunApp(); // Starts Guess Number game
                    return false;
                case 3:
                    rockPaperScissors.RunApp(); // Starts Rock, Paper, Scissors game
                    return false;
                case 4:
                    return QuitApp(); // Exits the application
                default:
                    Console.WriteLine("Invalid input! Please enter a number between 1 and 4.");
                    return false;
                }
            }

        // Runs the main application loop, allowing the user to select and play games
        public override void RunApp()
            {
            bool end = false;
            while (!end)
                {
                Menu(); // Displays the menu
                int whatToDo = ChooseNumber(1, 4); // Gets user input for game selection
                end = StartGame(whatToDo); // Starts the selected game or Quit app
                }
            ShowEndScreen(); // Displays the final screen before exiting
            }
        }
    }
