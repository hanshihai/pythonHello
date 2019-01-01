class TaxRating:

    def __init__(self, rangeMin, rangeMax, rating, discard):
        self.rangeMin = rangeMin
        self.rangMax = rangeMax
        self.rating = rating
        self.discard = discard


    def isInRanges(self, number):
        if number >= self.rangeMin and number < self.rangMax:
            return True
        else:
            return False

    def getRating(self):
        return self.rating

    def getDiscard(self):
        return self.discard


BASE_NO_TAX_RATING = 5000
ratings = []


def init():
    global ratings
    rating1 = TaxRating(0, 3000, 0.03, 0)
    rating2 = TaxRating(3000, 12000, 0.1, 210)
    rating3 = TaxRating(12000, 25000, 0.2, 1410)
    rating4 = TaxRating(25000, 35000, 0.25, 2660)
    rating5 = TaxRating(35000, 55000, 0.3, 4410)
    rating6 = TaxRating(55000, 80000, 0.35, 7160)
    rating7 = TaxRating(80000, 9990000, 0.45, 15160)

    ratings.append(rating1)
    ratings.append(rating2)
    ratings.append(rating3)
    ratings.append(rating4)


def calculateTax(salary, special_discard):
    init()
    tax = 0.0
    taxableSalary = salary - special_discard - BASE_NO_TAX_RATING
    for rating in ratings:
        if rating.isInRanges(taxableSalary):
            tax = taxableSalary * rating.getRating() - rating.getDiscard()
            break

    return tax


def main():
    salary_input = input("please input taxable salary and special non-taxable salary with space: ")
    salary = salary_input.split(" ")
    tax = calculateTax((float)(salary[0]), (float)(salary[1]))
    print(tax)


if __name__ == '__main__':
    main()