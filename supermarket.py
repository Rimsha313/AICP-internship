# Initialize variables for charity names and their respective totals
charity_names = ["Charity A", "Charity B", "Charity C"]
charity_totals = [0, 0, 0]

# Task 1 - Set up the donation system
def setup_donation_system():
    print("Enter the names of three charities:")
    for i in range(3):
        charity_names[i] = input(f"Enter name for Charity {i + 1}: ")

    print("\nCharity options:")
    for i, charity in enumerate(charity_names):
        print(f"{i + 1}. {charity}")

# Task 2 - Record and total each donation
def record_donation():
    while True:
        choice = int(input("\nEnter your choice of charity (1, 2, or 3), or -1 to show totals: "))
        if choice == -1:
            show_totals()
            break
        elif choice in [1, 2, 3]:
            bill_amount = float(input("Enter the customer's shopping bill amount: "))
            donation = bill_amount * 0.01
            charity_totals[choice - 1] += donation
            print(f"Donation of ${donation} made to {charity_names[choice - 1]}.")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or -1.")

# Task 3 - Show the totals so far
def show_totals():
    print("\nTotals Donated to Charities:")
    totals = sorted(zip(charity_names, charity_totals), key=lambda x: x[1], reverse=True)
    grand_total = sum(charity_totals)
    
    for charity, total in totals:
        print(f"{charity}: ${total:.2f}")
    
    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")

# Main program
setup_donation_system()
record_donation()
