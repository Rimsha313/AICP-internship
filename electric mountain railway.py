class TrainJourney:
    def __init__(self, dep_time, arr_time, num_coaches):
        self.departure_time = dep_time
        self.arrival_time = arr_time
        self.total_passengers = 0
        self.total_revenue = 0
        self.available_seats = [80] * num_coaches

class ElectricMountainRailway:
    def __init__(self):
        self.num_trains = 4
        self.num_coaches = 6
        self.up_journeys = [
            TrainJourney("09:00", "10:00", self.num_coaches),
            TrainJourney("11:00", "12:00", self.num_coaches),
            TrainJourney("13:00", "14:00", self.num_coaches),
            TrainJourney("15:00", "16:00", self.num_coaches),
        ]
        self.down_journeys = [
            TrainJourney("10:00", "11:00", self.num_coaches),
            TrainJourney("12:00", "13:00", self.num_coaches),
            TrainJourney("14:00", "15:00", self.num_coaches),
            TrainJourney("16:00", "17:00", self.num_coaches),
        ]
        self.total_passengers = 0
        self.total_revenue = 0

    def purchase_tickets(self, journey_index, num_passengers):
        if 0 <= journey_index < len(self.up_journeys) and self.up_journeys[journey_index].available_seats:
            total_price = num_passengers * 25.0
            self.up_journeys[journey_index].total_passengers += num_passengers
            self.up_journeys[journey_index].total_revenue += total_price
            self.total_passengers += num_passengers
            self.total_revenue += total_price
            if num_passengers >= 10:
                free_tickets = num_passengers // 10
                self.up_journeys[journey_index].total_passengers -= free_tickets
                self.up_journeys[journey_index].total_revenue -= free_tickets * 25.0
                self.total_passengers -= free_tickets
                self.total_revenue -= free_tickets * 25.0
            self.up_journeys[journey_index].available_seats.pop()
            print("Tickets purchased successfully!")
        else:
            print("Sorry, this journey is closed. No more tickets available.")

    def display_end_of_day_summary(self):
        print("{:<15} {:<15} {:<15}".format("Departure Time", "Passengers", "Revenue"))
        for journey in self.up_journeys:
            print("{:<15} {:<15} {:<15}".format(journey.departure_time, journey.total_passengers, journey.total_revenue))

        print("Total Passengers: {}".format(self.total_passengers))
        print("Total Revenue: ${:.2f}".format(self.total_revenue))

        max_passengers_index = max(range(len(self.up_journeys)), key=lambda i: self.up_journeys[i].total_passengers)
        print("Train journey with the most passengers: {}".format(self.up_journeys[max_passengers_index].departure_time))

    def display_screen(self):
        print("{:<15} {:<15}".format("Departure Time", "Available Seats"))
        for journey in self.up_journeys:
            print("{:<15}".format(journey.departure_time), end="")
            if journey.available_seats:
                for seats in journey.available_seats:
                    print("{:<10}".format(seats), end="")
            else:
                print("{:<10}".format("Closed"), end="")
            print()

    def start_of_day_setup(self):
        for journey in self.up_journeys:
            journey.total_passengers = 0
            journey.total_revenue = 0
            journey.available_seats = [80] * self.num_coaches



if __name__ == "__main__":
     # Task 1: Start of the day
    print("\nTask 1: Start of the day setup:")
    railway = ElectricMountainRailway()
    railway.start_of_day_setup()
    railway.display_screen()
    
    print("\nTask 2: Purchasing Tickets")
    railway = ElectricMountainRailway()
    num_of_passenger=int(input("Enter the number of passengers: "))
    index=int(input("Enter the index number: "))
    railway.purchase_tickets(index, num_of_passenger)
    railway.display_end_of_day_summary()
    railway.display_screen()