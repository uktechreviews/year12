total_price = 0
tue_offer = False
tue_price = 5.40
prices = [7.40,5.40,5.90,5.90,22.60]
prices2 = [8.90,6.40,6.90,6.90,27.60]
ticket_type =input("What type of tickets do you require? Adult? Children? Students? Seniors? Family? ")
if ticket_type == "Adults" and "Children ":
    adult = int(input("How many adult tickets?"))
    child = int(input("How many child tickets?"))
    tickets = adult + child
elif ticket_type == "Seniors":
    adult = int(input("How many adult tickets?"))
    child = int(input("How many child tickets?"))
    senior = int(input("How many senior tickets?"))
    tickets = adult + child + senior
elif ticket_type == "Students":
    students = int(input("How many student tickets"))
    tickets = students
elif ticket_type == "Family":
    family = int(input("How many Family tickets?"))
    tickets = family
else:
    print("Invalid Ticket")


date = "Saturday"
if date == "Tuesday":
    tue_offer = True
time = input("We have a film in booking, before and after 5 pm. Can you write after or before to choose your time")
if time == "before": 
    print("These are prices for bookings under 5 pm")
    print (" Adult: £",prices2[1],"Students: £",prices2[2],"Seniors: £",prices2[3],"Family: £",prices2[4])
    if ticket_type == "Adults" and "Children ":
        total_price = prices[0]*tickets+prices[1]*tickets
    elif ticket_type == "Seniors":
        total_price = prices[0]*tickets+prices[1]*tickets+prices[2]*tickets
    elif ticket_type == "Students":
        total_price = prices[3]*tickets
    elif ticket_type == "Family":
        total_price == prices[4]*tickets
    else:
        print("Invalid ticket")


        
elif time == "after":
    print("Prices for after 5 pm are shown below")
    print (" Adult: £",prices[0],"Children: £",prices[1],"Students: £",prices[2],"Seniors: £",prices[3],"Family: £",prices[4])
    if ticket_type == "Adults" and "Children ":
        total_price = prices2[0]*tickets+prices2[1]*tickets
    elif ticket_type == "Seniors":
        total_price = prices2[0]*tickets+prices2[1]*tickets+prices2[2]*tickets
    elif ticket_type == "Students":
        total_price = prices2[3]*tickets
    elif ticket_type == "Family":
        total_price == prices2[4]*tickets
    else:
        print("Invalid ticket")
else:
    print("Invalid word or integer entered. Please reset the application to try again")

if tue_offer == True:
    print("The cost is £",tue_price*tickets,"because it is discount Tuesday") 
