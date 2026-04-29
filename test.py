# Function to assign tasks to astronauts
def assign_tasks():
    """Assign crew members and their tasks"""
    astronauts = []
    tasks = ["Navigation", "Engineering", "Communication"]

    for i in range(3):
        name = input("Enter astronaut name: ")
        while True:
            task = (
                input(
                    f"Choose a task for {name} (Navigation, Engineering, Communication): "
                )
                .capitalize()
                .strip()
            )
            if task in tasks:
                break
            else:
                print("Invalid task. Please choose from the given options.")

        astronauts.append((name, task))
        print()

    return astronauts


def check_oxygen_level():
    """Check and validate spaceship oxygen level"""
    oxygen = int(input("Enter spaceship oxygen level (0-100): "))
    if 0 <= oxygen <= 100:
        if oxygen >= 30:
            print("Oxygen Status: Stable")
        else:
            print("Oxygen Status: Low")
    else:
        print("Invalid oxygen level!")

    print()
    return oxygen


def check_system_status():
    """Check critical system statuses and count failures"""
    failures = 0
    print("Enter system status for 3 critical systems (OK or Fail):")

    for i in range(3):
        status = input(f"System {i + 1}: ")
        if status.lower().strip() == "fail":
            failures += 1

    print("Number of system failures: ", failures)
    print()
    return failures


def check_food_supply():
    """Check food supply availability"""
    food = int(input("Enter total food packs available: "))

    if food >= 15:
        print("Food Supply: Sufficient")
        return True
    else:
        print("Food Supply: Insufficient")
        return False


def display_crew_assignments(astronauts):
    """Display crew member assignments"""
    print("\n--- Crew Assignments ---")
    for name, task in astronauts:
        print(f"{name}: {task}")


def make_mission_decision(oxygen, failures, food_ok):
    """Determine if mission is ready for launch"""
    if oxygen >= 30 and failures == 0 and food_ok:
        print("Mission Ready for Launch!")
    else:
        print("Mission Not Ready for Launch.")


def main():
    """Main program to run space mission simulation"""
    astronauts = assign_tasks()
    oxygen = check_oxygen_level()
    failures = check_system_status()
    food_ok = check_food_supply()

    display_crew_assignments(astronauts)
    make_mission_decision(oxygen, failures, food_ok)


if __name__ == "__main__":
    main()

# ---------------------------------- End of code ----------------------------------
