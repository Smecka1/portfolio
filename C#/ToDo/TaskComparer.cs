using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ToDo
    {
    /// <summary>
    /// A comparer for DateTime objects to enable sorting and searching tasks by date.
    /// Implements IComparer<DateTime> for use in binary search and sorting operations.
    /// </summary>
    class TaskDateComparer : IComparer<DateTime>
        {
        /// <summary>
        /// Compares two DateTime values.
        /// </summary>
        /// <param name="x">The first DateTime value.</param>
        /// <param name="y">The second DateTime value.</param>
        /// <returns>
        /// A negative number if x is earlier than y, zero if they are equal,
        /// or a positive number if x is later than y.
        /// </returns>
        public int Compare(DateTime x, DateTime y)
            {
            return x.CompareTo(y);
            }
        }
    }
