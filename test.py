# Step 1: Store astronaut names and assign tasks
# CREATE dictionary astronauts
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

# SET tasks = navigation, engineering, and communication

# FOR i from 1 to 3
# PROMPT user for astronaut name
# STORE name in astronauts with  task
# END FOR

# Get oxygen level
# PROMPT user for oxygen level 0 to 100
# STORE as oxygenLevel

##FOR i from 1 to 3
# PROMPT user for system status ok or fail
# IF status == FAIL
# END IF
# END FOR

# Step 4: Get food supply
# PROMPT user for number of food packs
# STORE as foodSupply

# Step 5: Check mission readiness
# IF oxygenLevel < 30 OR failCount > 1 OR foodSupply < 15
# PRINT " Mission Not Ready!"
# ELSE
# PRINT "Astronaut Assignments:"

# FOR each astronaut in dictionary
#  PRINT astronaut name  assigned task
# END FOR

# PRINT " Mission Ready for Launch!"
# ND IF
