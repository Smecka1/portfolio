using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace ToDo
    {
    /// <summary>
    /// Handles user interaction, input validation, and task management.
    /// </summary>
    class UserInterface
        {
        private Database database = new Database();

        /// <summary>
        /// Reads a valid integer from the console, prompting the user until a valid number is entered.
        /// </summary>
        /// <param name="errorMessage">Message displayed when input is invalid.</param>
        /// <returns>The validated integer input.</returns>
        public int GetValidNumber(string errorMessage)
            {
            int number;
            while (!int.TryParse(Console.ReadLine(), out number))
                {
                Console.WriteLine(errorMessage);
                }
            
            return number;
            }

        /// <summary>
        /// Reads a valid integer within a specified range.
        /// </summary>
        /// <param name="from">Lower bound of the range (inclusive).</param>
        /// <param name="to">Upper bound of the range (inclusive).</param>
        /// <returns>A valid integer within the specified range.</returns>
        public int GetNumberInRange(int from, int to)
            {
            int number;
            do
                {
                number = GetValidNumber("Input must be a number:");
                if (number < from || number > to)
                    {
                    Console.WriteLine($"Input must be from {from} to {to}...");
                    }
                } while (number < from || number > to);

            return number;
            }

        /// <summary>
        /// Reads a valid date from the console, prompting the user until a correct format is entered.
        /// </summary>
        /// <param name="promptText">Prompt message for the user.</param>
        /// <param name="errorMessage">Error message displayed on incorrect input.</param>
        /// <returns>A valid DateTime object.</returns>
        private DateTime GetDate(string promptText, string errorMessage)
            {
            Console.WriteLine(promptText);
            
            DateTime dateTime;
            while (!DateTime.TryParse(Console.ReadLine(), out dateTime))
                Console.WriteLine(errorMessage);

            return dateTime;
            }

        /// <summary>
        /// Reads a non-empty string from the console, trimming extra spaces.
        /// </summary>
        /// <returns>The validated input string.</returns>
        public string GetText()
            {
            string text = Console.ReadLine();

            while (string.IsNullOrWhiteSpace(text))
                {
                Console.WriteLine("Invalid input, try again:");
                text = Console.ReadLine();
                }

            return text.Trim();
            }

        /// <summary>
        /// Allows the user to select a predefined task or enter a custom task description.
        /// </summary>
        /// <returns>The task text.</returns>
        public string GetTaskText()
            {
            Console.WriteLine("Choose number of a predefined task:");
            database.WritePredefinedTasks();
            Console.WriteLine("\nor write your own text...");

            string text = GetText();

            string[] predefinedTasks = database.DefaultTasks();
            if (int.TryParse(text, out int choice))
                {
                if (choice > 0 && choice <= predefinedTasks.Length)
                    {
                    return predefinedTasks[choice - 1];
                    }
                else
                    {
                    return text;
                    }
                }
            else
                {
                return text;
                }
            }

        /// <summary>
        /// Creates a new task by collecting user input and storing it in the database.
        /// </summary>
        public void CreateNote()
            {
            Console.WriteLine("                     Create new task");
            Console.WriteLine("-----------------------------------------------------------------\n");
            string text = GetTaskText();
            DateTime date = GetDate("Enter date in format (30.1.2025) or with time (30.1.2025 15:30):", "Invalid, input must be like (30.1.2025) or (30.1.2025 15:30):");
            Console.WriteLine(database.AddTask(date, text));
        }

        /// <summary>
        /// Deletes a task specified by the user.
        /// </summary>
        public void DeleteNote()
            {
            Console.WriteLine("     Task on the specified day and time will be deleted");
            Console.WriteLine("-----------------------------------------------------------------\n");
            DateTime date = GetDate("Enter date and time in format (30.1.2025 15:30):", "Invalid, input must be like (30.1.2025 15:30):");
            
            Task[] tasksToDelete = database.FindDayTimeTasks(date);
            Console.WriteLine();
            
            foreach (Task task in tasksToDelete)
                {
                if (task.DateAndTime == date)
                    {
                    Console.WriteLine(database.DeleteTask(task));
                    }
                }
            }

        /// <summary>
        /// Allows the user to modify the list of predefined tasks.
        /// The user can either add a new task or remove an existing one.
        /// </summary>
        public void ChangePredefinedTasks()
            {
            Console.WriteLine("                  Change predefined tasks");
            Console.WriteLine("-----------------------------------------------------------------");
            database.WritePredefinedTasks();
            Console.WriteLine("\nChoose:\n1) Add new / 2) Remove existing");
            
            int addOrRemove = GetNumberInRange(1, 2);

            switch (addOrRemove)
                {
                case 1:
                    Console.WriteLine("\nAdd new\n-----------------------------");
                    Console.WriteLine("Write text of new task:");
                    string newText = GetText();
                    
                    Console.WriteLine("Write numeric position of new task:");
                    int index = GetNumberInRange(1, database.DefaultTasks().Length + 1);
                    
                    database.AddPredefinedTask(index - 1, newText);
                    break;
                
                case 2:
                    Console.WriteLine("\nRemove existing\n-----------------------------");
                    Console.WriteLine("Write number of task to remove:");
                    int removeText = GetNumberInRange(1, database.DefaultTasks().Length);
                    
                    database.DeletePredefinedTask(removeText - 1);
                    break;
                
                default:
                    Console.WriteLine("Invalid option");
                    break;
                }
            Console.WriteLine("\nAfter changes\n-----------------------------");
            database.WritePredefinedTasks();
            }

        /// <summary>
        /// Displays tasks for a specific day.
        /// </summary>
        /// <param name="date">The date for which tasks should be displayed.</param>
        public void ShowDay(DateTime date)
            {
            Task[] tasks = database.GetTasksForDate(date);
            
            Console.WriteLine("|                   " + date.DayOfWeek + " " + date.ToShortDateString());
            Console.WriteLine("|----------------------------------------------------------------");
            
            foreach (Task task in tasks)
                {
                Console.WriteLine("| " + task);
                }
            Console.WriteLine();
            }

        /// <summary>
        /// Displays tasks for multiple consecutive days.
        /// </summary>
        public void ShowTasksForDays()
            {
            Console.WriteLine("          Choose day(s) which you want to see");
            Console.WriteLine("-----------------------------------------------------------------\n");
            DateTime dayDate = GetDate("Enter date in format (30.1.2025):", "Invalid, input must be like (30.1.2025):");
            
            Console.WriteLine("And how many days after this date...");                  
            int days = GetValidNumber("Input must be a number:");

            Console.Clear();
            HeadVisualize();

            for (int i = 0; i <= days; i++)
                {
                ShowDay(dayDate);
                dayDate = dayDate.AddDays(1);
                }
            }

        /// <summary>
        /// Displays a decorative header for the To-Do list interface.
        /// </summary>
        public void HeadVisualize()
            {
            Console.WriteLine($"|{string.Join("", Enumerable.Repeat("|", 63))}|");
            Console.WriteLine($"||{string.Join("", Enumerable.Repeat(" To-Do", 10))} ||");
            Console.WriteLine($"|{string.Join("", Enumerable.Repeat("|", 63))}|");
            Console.WriteLine();
            }

        /// <summary>
        /// Waits for the user to press Enter before proceeding.
        /// </summary>
        public void WaitForEnter()
            {
            Console.WriteLine("\nPress Enter to continue...");
            Console.ReadLine();
            }

        /// <summary>
        /// Handles the main navigation menu for the To-Do list application.
        /// Allows the user to view, add, delete tasks, modify predefined tasks, or exit.
        /// </summary>
        public void Navigation()
            {
            bool end = false;
            while (!end)
                {
                Console.Clear();
                HeadVisualize();
                Console.WriteLine("|----------------------------------------------------------------");
                ShowDay(DateTime.Today);
                Console.WriteLine("1) View tasks");
                Console.WriteLine("2) Add new task");
                Console.WriteLine("3) Delete task");
                Console.WriteLine("4) Change predefined tasks");
                Console.WriteLine("5) Exit To-Do List");

                Console.WriteLine("\nChoose number:");
                int choice = GetNumberInRange(1, 5);

                switch (choice)
                    {
                    case 1:
                        Console.Clear();
                        HeadVisualize();
                        ShowTasksForDays();
                        WaitForEnter();
                        break;
                    
                    case 2:
                        Console.Clear();
                        HeadVisualize();
                        CreateNote();
                        WaitForEnter();
                        break;
                    
                    case 3:
                        Console.Clear();
                        HeadVisualize();
                        DeleteNote();
                        WaitForEnter();
                        break;
                    
                    case 4:
                        Console.Clear();
                        HeadVisualize();
                        ChangePredefinedTasks();
                        WaitForEnter();
                        break;
                    
                    case 5:
                        Console.Clear();
                        end = true;
                        break;
                    
                    default:
                        Console.WriteLine("Invalid option");
                        break;
                    }
                }
            Console.Clear();
            Console.WriteLine("\n Have a nice day...");
            }


        /// <summary>
        /// fills the database with data for testing the app.
        /// </summary>
        public void FillDatabase()
            {
            Random random = new Random();
            DateTime dateTime = DateTime.Today;
            string[] imaginaryTasks = {
                    "Walk the dog",
                    "Wash the dishes",
                    "Grocery shopping",
                    "Clean the house",
                    "Do the laundry",
                    "Cook dinner",
                    "Take out the trash",
                    "Water the plants",
                    "Go to the doctor",
                    "Pick up mail",
                    "Vacuum the floor",
                    "Pay the bills",
                    "Call a family member",
                    "Exercise",
                    "Read a book",
                    "Plan weekly meals",
                    "Organize the closet",
                    "Charge electronic devices",
                    "Check car maintenance",
                    "Sort and recycle waste" };

            for (int i = 0; i < 30; i++)
                {
                database.AddTask(dateTime, imaginaryTasks[random.Next(imaginaryTasks.Length)]);
                dateTime = dateTime.AddHours(11);
                database.AddTask(dateTime, imaginaryTasks[random.Next(imaginaryTasks.Length)]);
                dateTime = dateTime.AddHours(4);
                database.AddTask(dateTime, imaginaryTasks[random.Next(imaginaryTasks.Length)]);
                dateTime = dateTime.AddHours(9);
                }
            }
        }
    }
