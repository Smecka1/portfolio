namespace Games
{
    // Main entry point of the application
    class Program
    {
        // Main method that initializes and runs the game navigation
        static void Main(string[] args)
        {
            Navigation navigation = new Navigation(); // Creates an instance of the Navigation class
            navigation.RunApp(); // Starts the game selection menu


            Console.ReadKey(); // Waits for user input before closing the console
        }
    }
}
