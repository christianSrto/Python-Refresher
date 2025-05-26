# Match-case (Switch) Statements = An alternative to if-elif-else statements
#                                  Execute some code if a value matches a case

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(day_of_week(1))  
print(day_of_week(9))  



def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":  # Matches either 6 or 7
            return True
        case _:  # Default case
            return False
        
print(is_weekend("Saturday"))  