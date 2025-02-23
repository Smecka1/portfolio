using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Games
    {
    class TowerOfHanoi : AbstractGame
        {
        private int floors; // Number of floors (disks) in the game
        private int minMoves; // Minimum number of moves required to solve the puzzle
        private int moves; // Current number of moves made by the player
        private Stack<int> tower1; // Stack representing the first tower
        private Stack<int> tower2; // Stack representing the second tower
        private Stack<int> tower3; // Stack representing the third tower

        // Method to initialize the game with a specified number of floors
        public void InitiateGame(int floors)
            {
            this.floors = floors;
            minMoves = (int)Math.Pow(2, floors) - 1; // Calculate minimum moves using the formula 2^n - 1
            moves = 0;

            tower1 = new Stack<int>();
            int diskWide = floors * 2 + 1;
            for (int i = floors; i > 0; i--)
                {
                tower1.Push(diskWide); // Add disks to the first tower
                diskWide -= 2;
                }

            tower2 = new Stack<int>();
            tower3 = new Stack<int>();
            }

        // Method to add a disk to a destination tower
        private bool AddDisk(Stack<int> destinationTower, int disk)
            {
            if (destinationTower.Count == 0 || destinationTower.Peek() > disk)
                {
                destinationTower.Push(disk); // Add disk if the destination tower is empty or the top disk is larger
                return true;
                }
            Console.WriteLine("\nCan't put wider one on narrower one");
            return false;
            }

        // Method to remove a disk from a tower
        private int RemoveDisk(Stack<int> fromTower)
            {
            return fromTower.Pop();
            }

        // Method to display the welcome message and game rules
        protected override void WelcomeAndRules()
            {
            Console.WriteLine("                 Welcome in GAME - Tower of Hanoi");
            Console.WriteLine("------------------------------------------------------------------------");
            Console.WriteLine("- The game consists of three rods and multiple disks of different sizes.");
            Console.WriteLine("- The goal is to move all the disks from the first rod to the third rod.");
            Console.WriteLine("- You can only move one disk at a time.");
            Console.WriteLine("- A larger disk cannot be placed on top of a smaller disk.");
            Console.WriteLine("- Use the fewest moves possible to complete the game.");
            Console.WriteLine("\nPress any key to Start...");
            Console.ReadKey();
            }

        // Method to display a row of a tower
        private string ShowTowerRow(Stack<int> tower, int floor)
            {
            int diskWide = 1;
            if (tower.Count > floor)
                {
                diskWide = tower.OrderByDescending(i => i).ToArray()[floor];
                }

            int spaces = 10 + (int)(diskWide / 2);
            return string.Join("", Enumerable.Repeat("█", diskWide)).PadLeft(spaces) + "".PadRight(10 - (spaces - 10));
            }

        // Method to display the current state of the towers
        private void DisplayTowers()
            {
            Console.Clear();
            Console.WriteLine($"Minimum moves: {minMoves}        Moves: {moves}\n");
            for (int i = 6; i >= 0; i--)
                {
                string tower1Row = ShowTowerRow(tower1, i);
                string tower2Row = ShowTowerRow(tower2, i);
                string tower3Row = ShowTowerRow(tower3, i);
                Console.WriteLine($" {tower1Row} {tower2Row} {tower3Row}");
                }
            Console.WriteLine("          1                    2                    3\n");
            }

        // Method to prompt the user to choose the number of floors
        private int ChooseFloorsCount()
            {
            Console.WriteLine("Choose dificulty, enter number of floors (3 or 4 or 5)");
            return ChooseNumber(3, 5);
            }

        // Method to choose a tower based on the number
        private Stack<int> ChooseTower(int number)
            {
            if (number == 1)
                {
                return tower1;
                }
            else if (number == 2)
                {
                return tower2;
                }
            else
                {
                return tower3;
                }
            }

        // Main method to run the game
        public override void RunApp()
            {
            Console.Clear();
            WelcomeAndRules(); // Display welcome message and game rules

            bool run = true;
            while (run)
                {
                Console.Clear();
                int floors = ChooseFloorsCount(); // Prompt user to choose the number of floors
                InitiateGame(floors); // Initialize the game with the chosen number of floors

                bool end = false;
                while (tower3.Count != floors && end == false)
                    {
                    DisplayTowers(); // Display the current state of the towers
                    Console.WriteLine("Remove disk from tower...");
                    Stack<int> fromTower = null;
                    while (fromTower == null || fromTower.Count == 0)
                        {
                        int choose = ChooseNumber(1, 3); // Prompt user to choose a tower to remove a disk from
                        fromTower = ChooseTower(choose);
                        if (fromTower.Count == 0)
                            {
                            Console.WriteLine("Tower without disk, choose again...");
                            }
                        }
                    int disk = RemoveDisk(fromTower); // Remove the top disk from the chosen tower

                    bool success = false;
                    Stack<int> toTower = null;
                    while (!success)
                        {
                        Console.WriteLine("\nTo quit choose '0' or put disk to tower...");
                        int choose = ChooseNumber(0, 3); // Prompt user to choose a tower to place the disk on or quit
                        if (choose == 0)
                            {
                            end = true;
                            toTower = fromTower; // If user chooses to quit, return the disk to the original tower
                            }
                        else
                            {
                            toTower = ChooseTower(choose);
                            }
                        success = AddDisk(toTower, disk); // Attempt to add the disk to the chosen tower
                        }
                    moves++; // Increment the move counter
                    }

                DisplayTowers(); // Display the final state of the towers
                string message = tower3.Count == floors ? "Congratulations, You WIN!" : "Nice try";
                Console.WriteLine($"\n{message}\n");
                Console.WriteLine("\nPlay again?");
                run = YesOrNo(); // Prompt user to play again
                }
            ShowEndScreen(); // Display the end screen
            }
        }
    }
