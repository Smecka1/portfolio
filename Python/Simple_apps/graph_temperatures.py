import random
import matplotlib.pyplot as plt
import statistics

# List of month names in Czech
months = ["Leden", "Únor", "Březen", "Duben", "Květen", "Červen",
          "Červenec", "Srpen", "Září", "Říjen", "Listopad", "Prosinec"
]

# Dictionary with random temperatures for each month
month_temperatures = {
    "Leden": [random.randint(-8, 2) for _ in range(31)],
    "Únor": [random.randint(-6, 5) for _ in range(28)],
    "Březen": [random.randint(0, 10) for _ in range(31)],
    "Duben": [random.randint(2, 15) for _ in range(30)],
    "Květen": [random.randint(8, 20) for _ in range(31)],
    "Červen": [random.randint(14, 25) for _ in range(30)],
    "Červenec": [random.randint(20, 35) for _ in range(31)],
    "Srpen": [random.randint(18, 32) for _ in range(31)],
    "Září": [random.randint(8, 25) for _ in range(30)],
    "Říjen": [random.randint(5, 22) for _ in range(31)],
    "Listopad": [random.randint(0, 15) for _ in range(30)],
    "Prosinec": [random.randint(-6, 5) for _ in range(31)],
}

# Combine all month temperatures into a single list for yearly graph
all_months_temperatures = []
for temperatures in month_temperatures.values():
    all_months_temperatures += temperatures

# Calculate the average temperature for each month
month_average_temp = {}
for month, temperatures in month_temperatures.items():
    month_average_temp[month] = round(statistics.mean(temperatures),1)

# Font settings for graph titles and labels
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# Function to plot yearly temperature trend
def year_graph():
    plt.figure("Roční vývoj teploty")
    plt.plot(all_months_temperatures)
    plt.grid(axis="y", linestyle='--', linewidth=0.5)
    plt.title("Roční vývoj teploty", fontdict=font1)
    plt.xlabel("dny", fontdict=font2)
    plt.ylabel("teplota °C", fontdict=font2)
    plt.show(block=False)

# Function to plot individual monthly temperature trends in separate subplots
def year_graph_separate():
    plt.figure("Vývoj průměrné denní teploty")
    for position, month in enumerate(months):
        plt.subplot(3, 4, position + 1)  # Create a subplot for each month
        plt.plot(month_temperatures[month])
        plt.grid(axis="y", linestyle='--', linewidth=0.5)
        plt.suptitle("Vývoj průměrné denní teploty", fontsize=16)  # Main title for all subplots
        plt.title(month, {'family': 'serif', 'color': 'darkred', 'size': 12})  # Month title
        plt.tight_layout()  # Adjust the layout to prevent overlap
    return plt.show()

# Function to plot average monthly temperatures
def graph_average_temp():
    plt.figure(figsize=(12, 6))
    plt.bar(month_average_temp.keys(), month_average_temp.values(), color='skyblue')
    for month, temp in month_average_temp.items():
        plt.text(month, temp, f"{temp:.1f} °C", ha='center', fontsize=10)  # Display values on top of bars
    plt.title("Průměrné teploty v průběhu roku", fontdict=font1)
    plt.xlabel("měsíc", fontdict=font2)
    plt.ylabel("teplota °C", fontdict=font2)
    plt.grid(axis="y", linestyle='--', linewidth=0.5)
    return plt.show()

# Function to plot the temperature for a specific month
def month_graph(month_number):
    month = months[month_number - 1]  # Get the month name
    plt.figure(figsize=(12, 6))
    plt.plot(month_temperatures[month])
    plt.title(f"{month} - průměrná denní teplota", fontdict=font1)
    plt.xlabel("dny", fontdict=font2)
    plt.ylabel("teplota °C", fontdict=font2)
    plt.grid(axis="y", linestyle='--', linewidth=0.5)
    return plt.show()

# Function to validate the month number input
def month_range_validation(choice):
    if choice in range(1, 13):  # Check if the choice is within the valid range
        month_graph(choice)
    else:
        print("Číslo mimo rozsah! Zadej číslo od 1 do 12.")  # Error message for invalid input

# Main user interface for selecting options
def user_interface():
    print(f"{10 * ' '}Zobrazení grafů průměrných teplot pro loňský rok\n{72 * '-'}")
    while True:
        # Ask the user to select an option
        action = input("Vyber: 1) Přehled, 2) Průměrné měsíční teploty, 3) Zvol konkrétní měsíc, 4) Konec:\n")
        match action:
            case "1":
                year_graph()  # Plot yearly temperature trend
                year_graph_separate()  # Plot individual months' temperature trends
            case "2":
                graph_average_temp()  # Plot average monthly temperatures
            case "3":
                try:
                    # Ask user for a month number and validate input
                    month_choice = int(input("Zadej 1-12 podle měsíce který chceš zobrazit:\n"))
                    month_range_validation(month_choice)
                except ValueError:
                    print("Musíš zadat číslo!")  # Error if input is not a number
            case "4":
                break  # Exit the program
            case _:
                print("Neplatná volba!")  # Error message for invalid option


# Call the user interface function to start the program
user_interface()

