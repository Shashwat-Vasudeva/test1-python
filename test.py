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

for i in range(1, 4):
    status = input(f"System {i}: ")
    if status == "fail":
        failures += 1

print("Number of system failures: ", failures)
print()
##FOR i from 1 to 3
# PROMPT user for system status ok or fail


# IF status  FAIL
# END IF
# END FOR

# Step 4: Get food supply
# PROMPT user for number of food packs
# STORE as foodSupply

# Step 5: Check mission readiness

# PRINT " Mission Not Ready!"
# ELSE
# PRINT "Astronaut Assignments:"
