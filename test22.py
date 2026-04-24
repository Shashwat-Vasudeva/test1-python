# Collect astronaut names and tasks
astronauts = []
tasks = ["Navigation", "Engineering", "Communication"]

for i in range(3):
    name = input("Enter astronaut name: ")

    while True:
        task = input(
            f"Choose a task for {name} (Navigation, Engineering, Communication): "
        )
        if task in tasks:
            break
        else:
            print("Invalid task. Please choose from the given options.")

    astronauts.append((name, task))

print()

# Check oxygen level
oxygen = int(input("Enter spaceship oxygen level (0-100): "))

if 0 <= oxygen <= 100:
    if oxygen >= 50:
        print("Oxygen Status: Stable")
    else:
        print("Oxygen Status: Low")
else:
    print("Invalid oxygen level!")

print()

# Check system statuses
failures = 0
print("Enter system status for 3 critical systems (OK or FAIL):")

for i in range(1, 4):
    status = input(f"System {i}: ")
    if status == "FAIL":
        failures += 1

print(f"Number of system failures: {failures}")
print()

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
if oxygen >= 50 and failures == 0 and food_ok:
    print(" Mission Ready for Launch!")
else:
    print(" Mission Not Ready for Launch.")
