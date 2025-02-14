using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ToDo
    {
    /// <summary>
    /// Represents a task with a specific date and time.
    /// </summary>
    class Task
        {
        /// <summary>
        /// Gets or sets the date and time of the task.
        /// </summary>
        public DateTime DateAndTime { get; set; }
        /// <summary>
        /// Gets or sets the text description of the task.
        /// </summary>
        public string Text { get; set; }
        
        
        /// <summary>
        /// Initializes a new instance of the <see cref="Task"/> class.
        /// </summary>
        /// <param name="dateTime">The date and time of the task.</param>
        /// <param name="text">The task description.</param>
        public Task(DateTime dateTime, string text)
            {
            DateAndTime = dateTime;
            Text = text;
            }

        /// <summary>
        /// Returns a string representation of the task, showing the time and text.
        /// </summary>
        /// <returns>A string in the format "HH:mm - Task description".</returns>
        public override string ToString()
            {
            return DateAndTime.ToShortTimeString() + " - " + Text;
            }
        }
    }