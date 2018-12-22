DOLLAR_RATING = 6.77

def calculate_money(unit, value) :
    if "RMB" == unit :
        return value / DOLLAR_RATING
    elif "USD" == unit :
        return value * DOLLAR_RATING
    else :
        return -1;

while True:
    money_input  = input("please input money with RMB or USD: ")

    if "q" == money_input :
        break

    type_input = money_input[-3:]

    money_input = money_input[:-3]

    money_value = eval(money_input)

    print("the result is : ", calculate_money(type_input , money_value))
