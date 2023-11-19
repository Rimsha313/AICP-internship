def calculate_slab(slab):
    for i in range(3):
        slab[0][i] = slab[0][i] * slab[1][0]  # Multiplies each unit consumed in the slab by the cost per unit

def display_slab_cost(slab, slab_name):
    print(f"Cost for {slab_name} is:")
    for i in range(3):
        print(slab[0][i], end="\t")
    print("\n")

def main():
    slab_one = [[55, 65, 75], [10]]
    slab_two = [[120, 150, 170], [15]]
    slab_three = [[210, 230, 240], [20]]
    condition = True

    while condition:
        print("\n\t\t\tStudent ID is XY12345678")
        print("\n\tEnter your choice:")
        print("\n\tPress 1 to display the cost of slab 1 and slab 2.")
        print("\n\tPress 2 to display the cost of slab 3.")
        print("\n\tPress any other key to exit.")
        user_input = input()

        if user_input == '1':
            calculate_slab(slab_one)
            calculate_slab(slab_two)
            display_slab_cost(slab_one, "Slab 1")
            display_slab_cost(slab_two, "Slab 2")
        elif user_input == '2':
            calculate_slab(slab_three)
            display_slab_cost(slab_three, "Slab 3")
        else:
            condition = False

if __name__ == "__main__":                   
    main()
