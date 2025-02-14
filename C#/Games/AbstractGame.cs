using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Games
    {
    abstract class AbstractGame
        {
        // Static Random instance used throughout the game for generating random values
        protected static Random random = new Random();

        // Virtual method to display welcome message and game rules
        protected virtual void WelcomeAndRules()
            {
            Console.WriteLine(" Welcome in GAME - ........");
            Console.WriteLine("---------------------------------------");
            Console.WriteLine("-write rules here........");
            Console.WriteLine("\nPress any key to Start...");
            Console.ReadKey();
            }

        // Virtual method to display the end screen with a thank you message
        protected virtual void ShowEndScreen()
            {
            Console.Clear();
            Console.WriteLine("\n=================================");
            Console.WriteLine("     Thank you for the Game");
            Console.WriteLine("=================================\n");

            Console.WriteLine(" Press any key to Exit...");
            Console.ReadKey();
            }

        // Virtual method that prompts the user with a yes/no question and returns true or false based on input
        protected virtual bool YesOrNo()
            {
            while (true)
                {
                Console.WriteLine($"Write: (yes/no)");
                string input = Console.ReadLine()?.Trim().ToLower();

                if (input == "y" || input == "yes")
                    {
                    return true;
                    }
                else if (input == "n" || input == "no")
                    {
                    return false;
                    }
                else
                    {
                    Console.WriteLine("Invalid choice, try again");
                    }
                }
            }

        // Virtual method that prompts the user to choose a number within a specified range (from/to)
        protected virtual int ChooseNumber(int from, int to)
            {
            int choice = -1;
            while (choice < from || to < choice)
                {
                Console.WriteLine("Choose number:");
                while (!int.TryParse(Console.ReadLine(), out choice))
                    {
                    Console.WriteLine("Choose number:");
                    }
                if (choice < from || to < choice)
                    {
                    Console.WriteLine($"{choice} isn't valid choice, try again");
                    }
                }
            return choice;
            }

        // Abstract method that must be implemented by derived classes to run the game logic
        public abstract void RunApp();
        }
    }
