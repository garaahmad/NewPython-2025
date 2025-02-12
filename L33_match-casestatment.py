#by IF Statment
def day_of_week(day):
    if day == 1:
        return'It is Sunday'
    elif day == 2:
        return 'It is Monday'
    elif day == 3:
        return 'It is Tuesday'
    elif day == 4:
        return 'It is wednesday'
    elif day == 5:
        return 'It is Tuesday'
    elif day == 6:
        return 'It is Friday'
    elif day == 7:
        return 'It is Saturday'
    else:
        return 'NOT a valid day'
    
    

print(day_of_week(5))


#by Match-case Statment
def day_of_week_1(day):
    match day:
        case 1 | 5:
            return'It is Sunday OR Tuesday'
        case 2 | 7:
            return 'It is Monday OR Saturday'
        case 3 | 6:
            return 'It is Tuesday OR Friday'
        case 4 :
            return 'It is wednesday'
        case 5 | 1:
            return 'It is Tuesday OR Sunday'
        case 6 | 3:
            return 'It is Friday OR Tuesday'
        case 7 | 2:
            return 'It is Saturday OR Monday'
        case _:
            return 'NOT a valid day'
        
print(day_of_week_1(4))