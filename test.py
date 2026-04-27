# Step 1: Store astronaut names and assign tasks
# CREATE dictionary astronauts
# SET tasks = navigation, engineering, and communication
astronauts = []
tasks = ["Navigation", "Engineering", "Communication"]

# FOR i from 1 to 3
for i in range(3):
    name = input("Enter astronaut name: ")
    # PROMPT user for astronaut name
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
# PROMPT user for oxygen level 0 to 100
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
# FOR i from 1 to 3
# PROMPT user for system status ok or fail
for i in range(1, 4):
    status = input(f"System {i}: ")
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
if oxygen >= 50 and failures == 0 and food_ok:
    print(" Mission Ready for Launch!")
else:
    print(" Mission Not Ready for Launch.")

# Step 4: Get food supply
# PROMPT user for number of food packs
# STORE as foodSupply

# Step 5: Check mission readiness

# PRINT " Mission Not Ready!"
# ELSE
# PRINT "Astronaut Assignments:"
