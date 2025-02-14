using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace ToDo
    {
    /// <summary>
    /// Represents a simple task database that stores tasks and predefined default tasks.
    /// </summary>
    class Database
        {
        // List of user-defined tasks
        private List<Task> tasks = new List<Task>();
        // List of predefined default tasks
        private List<string> defaultTasks = new List<string>() { "Walk the dog", "Wash the dishes", "Exercise" };
        /// <summary>
        /// Returns an array of predefined default tasks.
        /// </summary>
        public string[] DefaultTasks()
            {
            return defaultTasks.ToArray();
            }


        /// <summary>
        /// Finds the index where a task with the given date should be inserted.
        /// Uses binary search for efficient lookup.
        /// </summary>
        /// <param name="date">The date to search for.</param>
        /// <returns>The index where the task is or should be inserted.</returns>
        public int FindTaskIndex(DateTime date)
            {
            int index = tasks.ConvertAll(t => t.DateAndTime).BinarySearch(date, new TaskDateComparer());
            
            if (index < 0)
                {
                index = ~index;
                }

            return index;
            }

        /// <summary>
        /// Finds all tasks that match a specific date and time.
        /// </summary>
        /// <param name="date">The exact date and time to search for.</param>
        /// <returns>An array of tasks that match the specified date and time.</returns>
        public Task[] FindDayTimeTasks(DateTime date)
            {
            return tasks.Where(x => x.DateAndTime == date).ToArray();
            }

        /// <summary>
        /// Adds a new task at the correct position based on its date and time.
        /// </summary>
        /// <param name="dateTime">The date and time of the task.</param>
        /// <param name="text">The description of the task.</param>
        /// <returns>A confirmation message indicating the task has been added.</returns>
        public string AddTask(DateTime dateTime, string text)
            {
            int index = FindTaskIndex(dateTime);
            Task newTask = new Task(dateTime, text);
            
            tasks.Insert(index, newTask);
            
            return "\n" + newTask.ToString() + " -> added";
            }

        /// <summary>
        /// Removes a specified task from the list.
        /// </summary>
        /// <param name="task">The task to remove.</param>
        /// <returns>A confirmation message indicating the task has been deleted.</returns>
        public string DeleteTask(Task task)
            {
            tasks.Remove(task);
            return task + " -> deleted";
            }

        /// <summary>
        /// Adds a predefined task to the default task list at the specified index.
        /// </summary>
        /// <param name="index">The index at which to insert the task.</param>
        /// <param name="text">The predefined task description.</param>
        public void AddPredefinedTask(int index, string text)
            {
            defaultTasks.Insert(index, text);
            }

        /// <summary>
        /// Deletes a predefined task from the default task list at the specified index.
        /// </summary>
        /// <param name="index">The index of the task to remove.</param>
        public void DeletePredefinedTask(int index)
            {
            defaultTasks.RemoveAt(index);
            }

        /// <summary>
        /// Prints all predefined default tasks to the console.
        /// </summary>
        public void WritePredefinedTasks()
            {
            for (int i = 0; i < defaultTasks.Count; i++)
                {
                Console.WriteLine($"{i + 1}) {defaultTasks[i]}");
                }
            }

        /// <summary>
        /// Retrieves all tasks scheduled for a specific date.
        /// </summary>
        /// <param name="dateTime">The date to retrieve tasks for.</param>
        /// <returns>An array of tasks scheduled for the given date.</returns>
        public Task[] GetTasksForDate(DateTime dateTime)
            {
            List<Task> dayTasks = new List<Task>();

            int index = FindTaskIndex(dateTime.AddDays(-1));

            for (int i = index; i < tasks.Count; i++)
                {
                if (tasks[i].DateAndTime.Date > dateTime.Date)
                    {
                    break; 
                    }

                if (tasks[i].DateAndTime.Date == dateTime.Date)
                    {
                    dayTasks.Add(tasks[i]); 
                    }
                }

            return dayTasks.ToArray();
            }
        }
    }
