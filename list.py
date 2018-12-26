import math


MONEY_DETLA = 10


def main(total_week):
    money_list = []
    week_index = 0
    week_save_money = 0
    total_summary = 0

    while week_index < total_week:
        week_index += 1
        week_save_money += MONEY_DETLA
        money_list.append(week_save_money)
        total_summary = math.fsum(money_list)
        print("the {} week, save money {}   and total money {}.".format(week_index, week_save_money, total_summary))


    print(money_list)


if __name__ ==  '__main__':
    main(52)
