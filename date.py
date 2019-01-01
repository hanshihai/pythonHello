import datetime

month_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def isSpecialYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0 :
        return True
    else:
        return False


def main(year):
    print("the year {} is special year : {}".format(year, isSpecialYear(year)))


if __name__ == '__main__':
    while True:
        year_input = input("please input year: ")
        if year_input == 'q':
            break
        else:
            try:
                year = (int)(year_input)
                main(year)
            except:
                print('exception is out')
