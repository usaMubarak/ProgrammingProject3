

# 20 seats on the plane
seats = [False] * 20

FIRST_CLASS_SEATS = [1, 2, 3, 4]
EMERGENCY_SEATS = [9, 10, 11, 12, 13, 14, 15, 16]

base_price = 100.0
first_class_fee = 50.0

total_sales = 0.0
seats_sold = 0

def show_seats():
    print("\nSeat Map (number = open, X = taken):")
    for i in range(20):
        seat_number = i + 1
        if seats[i]:
            print("X", end=" ")
        else:
            print(seat_number, end=" ")
        if seat_number % 4 == 0:
            print()
    print()

while True:
    show_seats()
    print("Enter a seat number from 1 to 20 (0 to quit):")
    user_input = input()

    if not user_input.isdigit():
        print("Please enter a number.\n")
        continue

    seat_choice = int(user_input)

    if seat_choice == 0:
        print("Exiting seat selection.")
        print("Total seats sold:", seats_sold)
        print("Total sales: $", round(total_sales, 2))
        break

    if seat_choice < 1 or seat_choice > 20:
        print("Invalid seat number.\n")
        continue

    index = seat_choice - 1

    if seats[index]:
        print("That seat is already taken.\n")
        continue

    # to check if seat is emergency
    if seat_choice in EMERGENCY_SEATS:
        print("You selected an emergency exit seat.")
        print("You must agree to assist in an emergency.")
        answer = input("Do you accept? (y/n): ")
        if answer.lower() != "y":
            print("You did not accept. Seat not assigned.\n")
            continue

    # price calculate
    seat_price = base_price

    if seat_choice in FIRST_CLASS_SEATS:
        print("First Class seat selected — extra fee applies.")
        seat_price = base_price + first_class_fee

    print("Seat price: $", seat_price)
    pay = input("Type 'y' to buy or anything else to cancel: ")

    if pay.lower() == "y":
        seats[index] = True
        seats_sold += 1
        total_sales += seat_price
        print("Seat", seat_choice, "assigned.\n")
    else:
        print("Purchase cancelled.\n")
