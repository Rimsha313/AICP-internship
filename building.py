# Function to check the contents and weight of a single sack
def check_sack(contents, weight):
    # Check contents and weight
    is_valid = True
    rejection_reason = ""

    # Check contents
    if contents not in ['C', 'G', 'S']:
        is_valid = False
        rejection_reason += "Invalid contents. "

    # Check weight based on contents
    if (contents == 'C' and (weight < 24.9 or weight > 25.1)) or ((contents == 'G' or contents == 'S') and (weight < 49.9 or weight > 50.1)):
        is_valid = False
        rejection_reason += "Invalid weight for the contents."

    # Output acceptance or rejection message
    if is_valid:
        return f"Accepted: Contents - {contents}, Weight - {weight}kg"
    else:
        return f"Rejected: {rejection_reason}"


# Function to check a customer's order for delivery
def check_order():
    total_weight = 0
    rejected_sacks = 0

    sacks_cement = int(input("Enter the number of cement sacks required: "))
    sacks_gravel = int(input("Enter the number of gravel sacks required: "))
    sacks_sand = int(input("Enter the number of sand sacks required: "))

    # Check contents and weight for each type of sack
    for _ in range(sacks_cement):
        contents = input("Enter the contents of the cement sack (C for cement): ")
        weight = float(input("Enter the weight of the cement sack in kilograms: "))
        result = check_sack(contents, weight)
        if "Accepted" in result:
            total_weight += weight
        else:
            rejected_sacks += 1
        print(result)

    for _ in range(sacks_gravel):
        contents = input("Enter the contents of the gravel sack (G for gravel): ")
        weight = float(input("Enter the weight of the gravel sack in kilograms: "))
        result = check_sack(contents, weight)
        if "Accepted" in result:
            total_weight += weight
        else:
            rejected_sacks += 1
        print(result)

    for _ in range(sacks_sand):
        contents = input("Enter the contents of the sand sack (S for sand): ")
        weight = float(input("Enter the weight of the sand sack in kilograms: "))
        result = check_sack(contents, weight)
        if "Accepted" in result:
            total_weight += weight
        else:
            rejected_sacks += 1
        print(result)

    print(f"Total weight of the order: {total_weight}kg")
    print(f"Number of sacks rejected from the order: {rejected_sacks}")


# Function to calculate the price for a customer's order
def calculate_price():
    sacks_cement = int(input("Enter the number of cement sacks required: "))
    sacks_gravel = int(input("Enter the number of gravel sacks required: "))
    sacks_sand = int(input("Enter the number of sand sacks required: "))

    regular_price = sacks_cement * 3 + sacks_gravel * 2 + sacks_sand * 2

    # Check for special packs
    special_packs = min(sacks_cement, sacks_gravel // 2, sacks_sand // 2)
    discount_price = special_packs * 10

    if discount_price > 0:
        print(f"Regular price for the order: ${regular_price}")
        print(f"New price for the order after discount: ${regular_price - discount_price}")
        print(f"Amount saved: ${discount_price}")
    else:
        print(f"Regular price for the order: ${regular_price}")


# Switch-like statement to perform tasks based on user choice
def perform_tasks(choice):
    if choice == 1:
        print("\nTASK 1 - Check the contents and weight of a single sack:")
        contents = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ")
        if contents== 'C':
            weight = float(input("Enter the weight of the cement (24.9 < weight <25.1 ): "))
            print(check_sack(contents, weight))
        else:
            weight = float(input("Enter the weight of the stack (49.9 < weight < 50.1 ):  "))
            print(check_sack(contents, weight))    
    elif choice == 2:
        print("\nTASK 2 - Check a customer’s order for delivery:")
        check_order()
    elif choice == 3:
        print("\nTASK 3 - Calculate the price for a customer’s order:")
        calculate_price()
    else:
        print("Invalid choice.")


# Main program
while True:
    print("\nMenu:")
    print("1. Check the contents and weight of a single sack")
    print("2. Check a customer’s order for delivery")
    print("3. Calculate the price for a customer’s order")
    print("4. Exit")

    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 4:
        print("Exiting program.")
        break
    
    perform_tasks(user_choice)
