"""this file is designed for boss of the bank"""

from employee import *
import bank

"""this method currently can just create the employee for bank and give amount for their values with create_employee function"""


def create_employee():

    user = employee()

    user.set_user_name()
    user.set_password()
    user.set_name()
    user.set_family()
    user.set_phone_number()
    user.set_address()
    user.set_national_code()
    user.set_birth_date()
    bank.bank_employees_list[user.user_name] = {user: user.password}
    check_answer()


def check_answer():
    time.sleep(1)
    print(200 * '-')
    input_value = input("\nare you want to continue ? \n1.yes \n2.no\n")
    match input_value:

        case '1':

            create_employee()
        case '2':
            bank.introduction()

        case _:

            time.sleep(1)
            print(200 * '-')
            print("\ninvalid input\nplease try again\n")
            check_answer()
