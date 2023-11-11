class ComputerShop:
    def __init__(self):
        # Define components with dictionaries for better organization
        self.components = {
            "Case": {"A1": {"description": "Compact", "price": 75.00}, "A2": {"description": "Tower", "price": 150.00}},
            "RAM": {"B1": {"description": "8 GB", "price": 79.99}, "B2": {"description": "16 GB", "price": 149.99}, "B3": {"description": "32 GB", "price": 299.99}},
            "Main Hard Disk Drive": {"C1": {"description": "1 TB HDD", "price": 49.99}, "C2": {"description": "2 TB HDD", "price": 89.99}, "C3": {"description": "4 TB HDD", "price": 129.99}},
            "Solid State Drive": {"D1": {"description": "240 GB SSD", "price": 59.99}, "D2": {"description": "480 GB SSD", "price": 119.99}},
            "Second Hard Disk Drive": {"E1": {"description": "1 TB HDD", "price": 49.99}, "E2": {"description": "2 TB HDD", "price": 89.99}, "E3": {"description": "4 TB HDD", "price": 129.99}},
            "Optical Drive": {"F1": {"description": "DVD/Blu-Ray Player", "price": 50.00}, "F2": {"description": "DVD/Blu-Ray Re-writer", "price": 100.00}},
            "Operating System": {"G1": {"description": "Standard Version", "price": 100.00}, "G2": {"description": "Professional Version", "price": 175.00}},
        }

        # Basic set of components
        self.basic_set_price = 200.00

        # Initialize selected components and total price
        self.selected_components = {}
        self.additional_items = []
        self.total_price = 0.00

    def display_menu(self, category):
        print(f"Available {category} options:")
        for item, details in self.components[category].items():
            print(f"{item} - {details['description']}: ${details['price']:.2f}")

    def choose_component(self, category):
        self.display_menu(category)
        while True:
            choice = input(f"Choose {category} (Enter item code, or 'none' to skip): ").upper()
            if choice == 'NONE':
                return None
            elif choice in self.components[category]:
                return choice
            else:
                print("Invalid choice. Please enter a valid item code or 'none' to skip.")

    def update_total_price(self, category, item):
        if item:
            self.total_price += self.components[category][item]["price"]

    def run(self):
        print("Welcome to the Computer Shop!")

        # Choose one case, one RAM, and one Main Hard Disk Drive
        for category in ["Case", "RAM", "Main Hard Disk Drive"]:
            self.selected_components[category] = self.choose_component(category)
            self.update_total_price(category, self.selected_components[category])

        # Ask if the customer wants to purchase additional items
        while True:
            additional_choice = input("Do you want to purchase additional items? (yes/no): ").lower()
            if additional_choice == "yes":
                for category in ["Solid State Drive", "Second Hard Disk Drive", "Optical Drive", "Operating System"]:
                    additional_item = self.choose_component(category)
                    self.update_total_price(category, additional_item)
                    self.additional_items.append(additional_item)
            elif additional_choice == "no":
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

        # Display chosen items and total price
        print("\nChosen Components:")
        for category, item in self.selected_components.items():
            print(f"{category}: {item} - {self.components[category][item]['description']}")
        print("\nAdditional Items:")
        for item in self.additional_items:
            print(item)

        # Display total price and apply discount if applicable
        print(f"\nTotal Price before discount: ${self.total_price:.2f}")

        # Apply discount based on the number of additional items
        discount_percentage = 0.05 if len(self.additional_items) == 1 else 0.10 if len(self.additional_items) >= 2 else 0.00

        # Calculate discount and new price
        discount_amount = self.total_price * discount_percentage
        discounted_price = self.total_price - discount_amount

        # Display discount and new price
        print(f"Discount: ${discount_amount:.2f} ({discount_percentage * 100:.0f}%)")
        print(f"Total Price after discount: ${discounted_price:.2f}")
        print(f"Amount of Money Saved: ${discount_amount:.2f}")


if __name__ == "__main__":
    computer_shop = ComputerShop()
    computer_shop.run()
