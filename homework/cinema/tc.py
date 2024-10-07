def get_ticket_prices( day, time_period):
    if day.lower() =="tuesday":
        return {
            "adult":5.40,
            'child':5.40,
            
            'student':5.40,
            'senior':5.40,
            'family':5.40,
        }
    else: 
        if time_period == "before" :
            return{
                'adult': 7.40,
                'child':5.40,
                'student': 5.90,
                'senior':5.90,
                'family':22.60
            
            }
        elif time_period =="after":
            return{
                'adult': 8.90,
                'child':6.40,
                'student': 6.90,
                'senior':6.90,
                'family':27.60

            }
        else:
            raise ValueError("invalid time period")
        

def calc_total_cost(ticket_prices, num_tickets):
    total = (
        ticket_prices['adult']* num_tickets.get('adult',0)+
        ticket_prices['child']* num_tickets.get('child',0)+
        ticket_prices['student']* num_tickets.get('student',0)+
        ticket_prices['senior']* num_tickets.get('senior',0)+
        ticket_prices['family']* num_tickets.get('family',0)
    )
    return total

def get_vaild_input(prompt, valid_values=None, value_type=int):
    while True:
        user_input = input(prompt).strip().lower()
        if valid_values and user_input not in valid_values:
            print('invalid input')
        else:
            try:
                if value_type == int:
                    return int(user_input)
                else:
                    return user_input
            except ValueError:
                print('please enter valid type')


def main():
    day = get_vaild_input("what day is it?", valid_values=['monday','tuesday','wednesday',"thursday","friday","saturday","sunday"], value_type=str
)
    if day.lower()!="tuesday":
        time_period = get_vaild_input("Is it befroe 5pm or after 5pm?", valid_values=['before',"after"], value_type=str)

    else:
        time_period= None


    num_tickets = {
        "adult": get_vaild_input("how many adult ticktes?:", value_type=int),
        "child": get_vaild_input("how many child ticktes?:", value_type=int),
        "student":get_vaild_input("how many students ticktes?:", value_type=int),
        "senior":get_vaild_input("how many seniors ticktes?:", value_type=int),
        'family':get_vaild_input("how many family ticktes?:", value_type=int),

    }

    ticket_prices = get_ticket_prices(day, time_period if time_period else "before")

    total_cost = calc_total_cost(ticket_prices, num_tickets)

    print(f"the total cost of ticket is:£{total_cost:.2f}")

if __name__ == "__main__":
    main() 
