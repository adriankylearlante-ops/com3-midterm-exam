# Storage
assigned_chores = []
assigned_roommates = []
assigned_status = []

# Status options
done_inputs = {"done", "d", "yes", "y"}
not_done_inputs = {"not done", "notdone", "not_done", "n", "no", "incomplete"}

# Room Monitor Input
while True:
    monitor = input("Room monitor name: ").strip()

    if not monitor:
        print("Cannot be empty.")
        continue
    if " " in monitor:
        print("No spaces allowed in name.")
        continue

    has_number = False
    for ch in monitor:
        if ch >= "0" and ch <= "9":
            has_number = True

    if has_number:
        print("Name cannot contain numbers.")
        continue

    break

# Room Number Input
while True:
    room = input("Room number: ").strip()
    if not room:
        print("Room number cannot be empty. Please enter a room number.")
        continue
    if room == "0":
        print("Room number cannot be 0. Please enter a valid room number.")
        continue
    room = room.upper()
    break

# Display chores
chore_list = ["Sweeping / Mopping", "Dishwashing", "Taking Out Trash",
              "Cleaning Bathroom", "Buying Groceries"]
chore_regularity = ["Daily", "After meals", "Every other day", "Weekly", "Weekly"]

print("\n" + "=" * 50)
print("DORM ROOM -- CHORE LIST")
print("=" * 50)
for i in range(len(chore_list)):
    print(f"{i + 1}. {chore_list[i]:<25} [{chore_regularity[i]}]")
print("=" * 50)

# Assign chores
for i in range(4):
    print(f"\n--- CHORE {i + 1} ---")

    while True:
        choice = input("Chore number (0 to skip): ").strip()

        if choice == "":
            print("Input cannot be empty. Enter 0 to skip or a single digit.")
            continue

        all_digits = True
        for ch in choice:
            if ch < "0" or ch > "9":
                all_digits = False

        if not all_digits:
            print("Invalid input. Please enter a number.")
            continue

        if len(choice) != 1:
            print("Chore number must be a single digit only.")
            continue

        num = int(choice)
        if num == 0:
            break
        if 1 <= num <= len(chore_list):
            break

        print("Invalid chore number.")

    if num == 0:
        continue

    # Roommate name
    while True:
        name = input("Roommate name: ").strip()

        if name == "":
            print("Roommate name cannot be empty. Please enter a name.")
            continue
        if " " in name:
            print("Roommate name cannot contain spaces.")
            continue

        has_number = False
        for ch in name:
            if ch >= "0" and ch <= "9":
                has_number = True

        if has_number:
            print("Roommate name cannot contain numbers.")
            continue

        break

    # Status
    while True:
        stat_input = input("Status (done/not done): ").strip()
        if stat_input == "":
            print("Status cannot be empty. Please enter 'done' or 'not done'.")
            continue

        sval = stat_input.lower().replace("_", " ").strip()
        if sval in done_inputs:
            status = "done"
            break
        elif sval in not_done_inputs:
            status = "not done"
            break
        else:
            print("Unrecognized status. Please type 'done' or 'not done'.")

    assigned_chores.append(num)
    assigned_roommates.append(name)
    assigned_status.append(status)

# Compute
total = len(assigned_chores)
done_count = 0
for s in assigned_status:
    if s == "done":
        done_count += 1

if total > 0:
    rate = int((done_count / total) * 100)
else:
    rate = 0

# Status label
if rate == 100:
    condition = "ROOM IS SPOTLESS!"
elif rate >= 50:
    condition = "ALMOST THERE!"
else:
    condition = "NEEDS CATCHING UP!"

# Output
print("\n" + "=" * 50)
print(f"ROOM {room} -- WEEKLY CHORE REPORT")
print("=" * 50)

print(f"Room Monitor : {monitor}")
print("-" * 50)

for i in range(total):
    c_num = assigned_chores[i]
    print(f"[{i+1}] {chore_list[c_num-1]:<24} [{chore_regularity[c_num-1]}]")
    print(f"    Roommate : {assigned_roommates[i]}")
    print(f"    Status   : {assigned_status[i]}\n")

print("-" * 50)
print(f"Completed       : {done_count} out of {total} assigned")
print(f"Completion Rate : {rate}%")
print(f"Room Status     : {condition}")
print("=" * 50)
