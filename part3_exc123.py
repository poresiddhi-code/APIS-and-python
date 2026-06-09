import requests

# -------------------------------
# EXERCISE 1: WEATHER BY CITY
# -------------------------------
def get_weather():
    print("\n=== Weather Checker ===")

    city = input("Enter city (pune, delhi, mumbai): ").lower().strip()

    city_coords = {
        "pune": (18.5204, 73.8567),
        "delhi": (28.6139, 77.2090),
        "mumbai": (19.0760, 72.8777)
    }

    if city not in city_coords:
        print("City not supported!")
        return

    lat, lon = city_coords[city]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["current_weather"]

        print(f"\n--- Weather in {city.title()} ---")
        print("Temperature:", weather["temperature"], "°C")
        print("Wind Speed:", weather["windspeed"], "km/h")
    else:
        print("Weather data not found!")


# -------------------------------
# EXERCISE 2: TODOS SEARCH
# -------------------------------
def search_todos():
    print("\n=== Todo Search ===")

    status = input("Show completed tasks? (yes/no): ").lower().strip()

    completed = True if status == "yes" else False

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": completed}

    response = requests.get(url, params=params)

    todos = response.json()

    print(f"\n--- Todos (completed={completed}) ---")
    for i, todo in enumerate(todos[:10], 1):
        print(f"{i}. {todo['title']}")


# -------------------------------
# EXERCISE 3: USER INFO + VALIDATION
# -------------------------------
def get_user_info():
    print("\n=== User Info Lookup ===")

    user_id = input("Enter user ID (1-10): ")

    # validation
    if not user_id.isdigit():
        print("Invalid input! Please enter a number.")
        return

    user_id = int(user_id)

    if user_id < 1 or user_id > 10:
        print("User ID must be between 1 and 10.")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print(f"\n--- User #{user_id} ---")
        print("Name:", data["name"])
        print("Email:", data["email"])
        print("Phone:", data["phone"])
    else:
        print("User not found!")


# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    while True:
        print("\n========================")
        print("  API MINI PROJECT MENU")
        print("========================")
        print("1. Weather Checker")
        print("2. Todo Search")
        print("3. User Info")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            get_weather()
        elif choice == "2":
            search_todos()
        elif choice == "3":
            get_user_info()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


# run program
if __name__ == "__main__":
    main()