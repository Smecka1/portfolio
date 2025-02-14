namespace ToDo
{
    /// <summary>
    /// Entry point for the To-Do List application.
    /// Initializes the user interface and starts navigation.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
            {
            // Create instance of User interface
            UserInterface uI = new UserInterface();
            
            // Fill the database with predefined tasks before starting the app
            uI.FillDatabase();
            // Start the navigation menu
            uI.Navigation();

            // Wait for a key press before exiting
            Console.ReadKey();
            }
    }
}
