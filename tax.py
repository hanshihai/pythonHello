'''
This is the calculator for personal tax of Shanghai 2018

version : v0.1

'''

COMPANY_AGE = 0.20
COMPANY_MEDICAL = 0.095
COMPANY_JOB = 0.005
COMPANY_HOUSE = 0.07
COMPANY_ADDITIONAL_HOUSE = 0.03
COMPANY_INSURANCE_HURTING = 0.002
COMPANY_INSURANCE_BABY = 0.01

PERSONAL_AGE = 0.08
PERSONAL_MEDICAL = 0.02
PERSONAL_JOB = 0.005
PERSONAL_HOUSE = 0.07
PERSONAL_ADDITIONAL_HOUSE = 0.03

def main():

    total_input = input("Please input the base month income, and the rating money with space split, such as 12000 12000 : ")
    input_list = total_input.split(' ')
    total_income = input_list[0]
    rating_money = input_list[1]

    company_age_output = float(rating_money) * COMPANY_AGE
    company_medical_output = float(rating_money) * COMPANY_MEDICAL
    company_job_output = float(rating_money) * COMPANY_JOB
    company_house_output = float(rating_money) * COMPANY_HOUSE
    company_additional_house_output = float(rating_money) * COMPANY_ADDITIONAL_HOUSE
    company_insurance_hurting = float(rating_money) * COMPANY_INSURANCE_HURTING
    company_insurance_baby = float(rating_money) * COMPANY_INSURANCE_BABY

    company_total_output = company_age_output + company_medical_output + company_job_output + company_house_output + company_additional_house_output + company_insurance_hurting + company_insurance_baby

    personal_age_output = float(rating_money) * PERSONAL_AGE
    personal_medical_output = float(rating_money) * PERSONAL_MEDICAL
    personal_job_output = float(rating_money) * PERSONAL_JOB
    personal_house_output = float(rating_money) * PERSONAL_HOUSE
    personal_additional_house_output = float(rating_money) * PERSONAL_ADDITIONAL_HOUSE

    personal_total_output = personal_age_output + personal_medical_output + personal_job_output + personal_house_output + personal_additional_house_output

    company_format_output = "The money that company provided:  age {},     medical {},    job {},     house {},   additional_house {},    insurance_hurting {},   insurance_baby {},  and total {}"
    personal_format_output = "The money that personal provided: age {},     medical {},     job {},     house {},   additional_house {},    and total {}"

    print(company_format_output.format(company_age_output, company_medical_output, company_job_output, company_house_output, company_additional_house_output, company_insurance_hurting, company_insurance_baby, company_total_output))
    print('')
    print(personal_format_output.format(personal_age_output, personal_medical_output, personal_job_output, personal_house_output, personal_additional_house_output, personal_total_output))


if __name__ == '__main__':
    main()