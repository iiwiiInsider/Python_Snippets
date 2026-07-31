import csv
from datetime import datetime

def calculate_calories(minutes, calories_per_min):
    return minutes * calories_per_min

def save_to_csv(data, filename="workout_log.csv"):
    header = ["Date", "Activity", "Minutes", "Calories per Min", "Calories Burned"]

    try:
        with open(filename, "r"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(data)

def main():
    print("=== Universal Workout Tracker ===")

    activity = input("Enter activity name (e.g., running, cycling, yoga): ").strip()

    minutes = float(input("Enter duration in minutes: "))

    calories_per_min = float(input(
        "Enter calories burned per minute for this activity "
        "(e.g., running ~12, cycling ~8, yoga ~4): "
    ))

    calories_burned = calculate_calories(minutes, calories_per_min)

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_to_csv([date, activity, minutes, calories_per_min, calories_burned])

    print("\nWorkout logged successfully!")
    print(f"Activity: {activity}")
    print(f"Duration: {minutes} min")
    print(f"Calories burned: {calories_burned:.1f}")
    print("Saved to workout_log.csv")

if __name__ == "__main__":
    main()
