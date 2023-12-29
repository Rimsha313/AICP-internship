boat_cost_per_hour = 20
boat_cost_per_half_hour = 12
boats = {i: {'hours_hired': 0, 'return_time': None} for i in range(1, 11)}

def calculate_money_taken(boat_number, start_time, end_time):
    if start_time < 10 or end_time > 17:
        print("Boat can only be hired between 10:00 and 17:00.")
        return

    duration = end_time - start_time
    if duration >= 1:
        cost = duration * boat_cost_per_hour
        boats[boat_number]['hours_hired'] += duration
        boats[boat_number]['return_time'] = end_time
    else:
        cost = boat_cost_per_half_hour
        boats[boat_number]['hours_hired'] += 0.5
        boats[boat_number]['return_time'] = end_time

    print(f"Boat {boat_number}: Money taken - ${cost}, Total hours hired - {boats[boat_number]['hours_hired']}")

def find_next_available():
    current_time = int(input(" Enter current time (in hours): "))
    available_boats = [boat for boat in boats if boats[boat]['return_time'] is None or boats[boat]['return_time'] <= current_time]

    if available_boats:
        print("\n\t\t *** Available Boats*** ")
        print(f"\n {len(available_boats)}boats available for hire right now: {available_boats}")
    else:
        next_return_time = min([boats[boat]['return_time'] for boat in boats if boats[boat]['return_time'] > current_time])
        print(f"\nNo boats available right now. Next available time: {next_return_time}:00")

def calculate_money_all_boats():
    total_money = sum([boats[boat]['hours_hired'] * boat_cost_per_hour if boats[boat]['hours_hired'] >= 1
                       else boat_cost_per_half_hour for boat in boats])
    total_hours = sum([boats[boat]['hours_hired'] for boat in boats])
    boats_not_used = len([boat for boat in boats if boats[boat]['hours_hired'] == 0])
    most_used_boat = max(boats, key=lambda x: boats[x]['hours_hired'])
    print(f"\n\t\t ***Grand total of all boats***")
    print(f"\nTotal money taken for all boats: ${total_money}")
    print(f"\nTotal number of hours boats were hired: {total_hours}")
    print(f"\nBoats not used today: {boats_not_used}")
    print(f"\nBoat used the most today: {most_used_boat}, Hours hired: {boats[most_used_boat]['hours_hired']}")

# Function to handle booking boats
def book_boats():
    while True:
        num_boats = int(input("\n\tHow many boats do you want to hire? (1-10): "))
        if num_boats < 1 or num_boats > 10:
            print("Invalid number of boats. Please choose between 1 and 10.")
            continue

        for _ in range(num_boats):
            boat_num = int(input(f"\nEnter BOAT number to book (1-10): "))
            if boat_num not in boats:
                print("Invalid boat number.")
                continue
            
            start_time = int(input("\nEnter START time for hire (10-17): "))
            end_time = int(input("\nEnter END time for hire (10-17): "))

            calculate_money_taken(boat_num, start_time, end_time)
        
        find_next_available()

        choice = input("\nDo you want to book more boats? (yes/no): ")
        if choice.lower() != 'yes':
            break

    calculate_money_all_boats()

# Main p rogram
book_boats()
