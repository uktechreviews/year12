adultsbefore = 7.40
adultsafter = 8.90

childrenbefore = 5.40
childrenafter = 6.40

studentsbefore = 5.90
studentsafter = 6.90

seniorsbefore = 5.90
seniorsafter = 6.90

familybefore = 22.60
familyafter = 27.60

tuesdayprice = 5.40

day = input("what day is it today? ").lower()
time = input("is it before or after 5pm? (before/after)").lower()

if time == "before":
    adults = adultsbefore
    children = childrenbefore
    students = studentsbefore
    senior = seniorsbefore
    family = familybefore

if time == "after":
    adults = adultsafter
    children = childrenafter
    students = studentsafter
    senior = seniorsafter
    family = familyafter

if day == "tuesday":
    adults = tuesdayprice
    children = tuesdayprice
    students = tuesdayprice
    senior = tuesdayprice
    family = tuesdayprice

adulttickets = int(input("how many adult tickets? ")) * adults
childrenticket = int(input("how many children tickets? ")) * children
studentsticket = int(input("how many student tickets? ")) * students
seniorsticket = int(input("how many seniors tickets? ")) * senior
familyticket = int(input("how many family tickets? ")) * family

total = adulttickets + childrenticket + studentsticket + seniorsticket + familyticket

print(f"your total will be £{total}") 
