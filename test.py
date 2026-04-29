# Step 1: Store astronaut names and assign tasks
# SET tasks = navigation, engineering, and communication
astronauts = []
tasks = [
    "Navigation",
    "Engineering",
    "Communication",
]

# FOR i from 0 to 2
for i in range(3):
    name = input("Enter astronaut name: ").capitalize().strip()
    # PROMPT user for astronaut name
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


# Check oxygen level
# PROMPT user for oxygen level 0 to 100
oxygen = int(input("Enter spaceship oxygen level (0-100): "))
if 0 <= oxygen <= 100:
    if oxygen >= 30:
        print("Oxygen Status: Stable")
    else:
        print("Oxygen Status: Low")
else:
    print("Invalid oxygen level!")

print()
# Check system statuses

failures = 0
print("Enter system status for 3 critical systems (OK or FAIL):")
# FOR i from 0 to 2
# PROMPT user for system status ok or fail
for i in range(3):
    status = input(f"System {i + 1       }: ")
    if status == "fail":
        failures += 1

print("Number of system failures: ", failures)
print()


# IF status  FAIL
# END IF
# END FOR
# Check food supply
food = int(input("Enter total food packs available: "))

if food >= 15:
    print("Food Supply: Sufficient")
    food_ok = True
else:
    print("Food Supply: Insufficient")
    food_ok = False

print("\n--- Crew Assignments ---")
for name, task in astronauts:
    print(f"{name}: {task}")

# Final mission decision
if oxygen >= 30 and failures == 0 and food_ok == True:
    print("Mission Ready for Launch!")
else:
    print("Mission Not Ready for Launch.")

# ---------------------------------- End of code ----------------------------------
