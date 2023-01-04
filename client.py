"""this file contain client class and its functions"""


import time
import datetime
import math
import bank
from bank import *
from person import person


"""this class make for clients """


class client (person):

    def __init__(self):

        self. ob_employee = None
        self.time_list = []
        self.transaction_list = []
        self.code_list = []
        self.amount_list = []
        self.loan_dict = {}
        self.flag_dict = {}
        self.counter_dict = {}

        person.__init__(self)

    """this function written for menu and the options of menu """
    switch = False

    def menu(self):

        self.show_iformation()
        time.sleep(1)
        print(200 * '-')
        subject_menu = input(
            "enter subject number:\n1.edit\n2.service\nif you want to back , press 0\n")
        match subject_menu:
            case '0':
                list(bank.bank_clients_list[bank.get_client_username()].keys())[
                    0].menu()
            case '1':
                self.sub_menu(subject_menu)
            case '2':
                self.sub_menu(subject_menu)
            case _:
                self.delay(self.menu)

    """this function is second menu """

    def sub_menu(self, subject_menu):

        if subject_menu == '1':

            time.sleep(1)
            print(200 * '-')

            option = input(
                "enter option number:\n1.edit password \n2.edit phone number \n3.edit address \nif you want to back , press 0\n")

            match option:
                case "0":
                    self.menu()

                case "1":
                    self.restore_password()
                    self.sub_menu('1')
                case "2":

                    self.set_phone_number()
                    self.sub_menu('1')

                case "3":
                    self.set_address()
                    self.sub_menu('1')
                case _:
                    self.delay_with_parameter(self.sub_menu, '1')

        else:

            time.sleep(1)
            print(200 * '-')

            option = input(
                "enter option number : \n1.charge money \n2.get money \n3.move money \n4.show operations \n5.loan request \n6.installment_payment \nif you want to back , press 0\n")

            match option:

                case "0":
                    self.menu()
                case "1":
                    self.charge_money()
                    self.sub_menu('2')
                case "2":

                    self.get_money()
                    self.sub_menu('2')

                case "3":
                    self.move_money()
                    self.sub_menu('2')
                case "4":
                    self.show_operations()
                    self.sub_menu('2')
                case "5":
                    self.loan_request()
                    self.sub_menu('2')
                case "6":
                    self.installment_payment()
                    self.sub_menu('2')

                case _:
                    self.delay_with_parameter(self.sub_menu, '2')

    """this function written for get and set the validity and it check it to prevent its incorrect values"""

    def set_validity(self):
        time.sleep(1)
        print(200 * '-')

        validity_2 = input(
            "enter validity:\nthe number must great than 1000 Rials\nif you want to back , press 0\n")
        if validity_2 == '0':
            if self.ob_employee.option_2 == "4":
                self.ob_employee.sub_menu_3()
            else:

                self.ob_employee.sub_menu_1('2')
        if validity_2.isnumeric() == False or int(validity_2) < 1000:
            self.delay(self.set_validity)
        else:
            self.validity = int(validity_2)

    """this function written for charging the account and it check it to prevent its incorrect values and send the information of this operation"""

    def charge_money(self):

        time.sleep(1)
        print(200 * '-')

        amount_money = input(
            "enter amount of money that you want charge:\nthe number must great than 1000 Rials\nif you want to back , press 0\n")
        if amount_money == '0':
            if self.ob_employee.option_2 == "3":
                list(bank.bank_employees_list[bank.user_name].keys())[
                    0].sub_menu_2()

            else:
                self.sub_menu('2')

        if amount_money.isnumeric() == False or int(amount_money) < 1000:
            self.delay(self.charge_money)
        else:

            self.validity += int(amount_money)
            self.operations(datetime.datetime.now(), "charge money",
                            str(datetime.datetime.now().year) + str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+str(datetime.datetime.now().hour)+str(datetime.datetime.now().minute)+str(datetime.datetime.now().second), amount_money)

    """this function written for getting the money and it check it to prevent its incorrect values and send the information of this operation"""

    def get_money(self):

        time.sleep(1)
        print(200 * '-')

        amount_money = input(
            "enter amount of money that you want get:\nthe number must great than 1000 Rials\nif you want to back , press 0\n")
        if amount_money == '0':
            if self.ob_employee.option_2 == "3":
                list(bank.bank_employees_list[bank.user_name].keys())[
                    0].sub_menu_2()

            else:
                self.sub_menu('2')

        if amount_money.isnumeric() == False or int(amount_money) < 1000:
            self.delay(self.get_money)
        if self.validity < 1000:
            if self.ob_employee.option_2 != '3':
                time.sleep(1)
                print("\nyour validity is not enough please charge it\n")
                self.sub_menu('2')
            else:
                time.sleep(1)
                print("\nyour validity is not enough please charge it\n")
                list(bank.bank_employees_list[bank.user_name].keys())[
                    0].sub_menu_2()
        if int(amount_money) > (self.validity - 1000):
            if self.ob_employee.option_2 != '3':
                time.sleep(1)
                print("\nyour amount money is out of amount \nplease try again\n")
                self.sub_menu('2')
            else:
                time.sleep(1)
                print("\nyour amount money is out of amount \nplease try again\n")
                list(bank.bank_employees_list[bank.user_name].keys())[
                    0].sub_menu_2()

        else:

            self.validity -= int(amount_money)
            self.operations(datetime.datetime.now(), "get money",
                            str(datetime.datetime.now().year) + str(datetime.datetime.now().month)+str(datetime.datetime.now().day) +
                            str(datetime.datetime.now(
                            ).hour)+str(datetime.datetime.now().minute)+str(datetime.datetime.now().second),
                            amount_money)

    """this function written for when the another user give money to this user account and send the information of this operation"""

    def receive_money(self, amount):

        self.validity += int(amount)
        self.operations(datetime.datetime.now(), "receive money",
                        str(datetime.datetime.now().year) + str(datetime.datetime.now().month)+str(datetime.datetime.now().day) +
                        str(datetime.datetime.now().hour)+str(datetime.datetime.now().minute) +
                        str(datetime.datetime.now().second),
                        amount)

    """this function written for showing the client general information"""

    def show_iformation(self):

        time.sleep(1)
        print(200 * '-')
        print(f"\nthe information of user {self.user_name} :\n")
        print("total name : " + self.name + " " + self.family)
        print("validity : ", self.validity)
        print("phone number : " + self.phone_number)
        print("address : " + self.address)
        print("national_code : ", self.national_code)
        print("birth day :", self.birth_year, "/",
              self.birth_month, "/", self.birth_day)
        if self.switch == True:
            self.show_loans()

    """this function written for moving money from this account to another account and it check it to prevent to its incorrect values and prevent to moving validity out of maximum amount and send the information of this operation"""

    def move_money(self):

        time.sleep(1)
        print(200 * '-')

        money_amount = input(
            "how much do you want to move:\nif you want to back , press 0\n")
        if money_amount == '0':
            if self.ob_employee.option_2 == "3":
                list(bank.bank_employees_list[bank.user_name].keys())[
                    0].sub_menu_2()

            else:
                self.sub_menu('2')

        if int(money_amount) > 100000000 and bank.input_main != '2':
            time.sleep(1)

            print(
                "\nthe amount of money is out of range\nplease go to the employees for moving\n")
            self.menu()
        else:
            time.sleep(1)

            des = input(
                "enter destination account user name:\nif you want to back press 0\n")
            if des == '0':
                self.move_money()
            if des not in bank.bank_clients_list.keys():
                self.delay(self.move_money)
            else:
                if self.validity < 1000:
                    if self.ob_employee.option_2 != '3':
                        time.sleep(1)
                        print("\nyour validity is not enough please charge it\n")
                        self.sub_menu('2')

                    else:
                        time.sleep(1)
                        print("\nyour validity is not enough please charge it\n")
                        list(bank.bank_employees_list[bank.user_name].keys())[
                            0].sub_menu_2()
                if int(money_amount) > (self.validity - 1000):
                    if self.ob_employee.option_2 != '3':
                        time.sleep(1)
                        print(
                            "\nyour amount money is out of amount \nplease try again\n")
                        self.sub_menu('2')
                    else:
                        time.sleep(1)
                        print(
                            "\nyour amount money is out of amount \nplease try again\n")
                        list(bank.bank_employees_list[bank.user_name].keys())[
                            0].sub_menu_2()

                else:
                    self.validity -= int(money_amount)
                    self.operations(datetime.datetime.now(), "move money",
                                    str(datetime.datetime.now().year) + str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+str(
                        datetime.datetime.now().hour)+str(datetime.datetime.now().minute)+str(datetime.datetime.now().second),
                        money_amount)
                    list(bank.bank_clients_list[des].keys())[
                        0].receive_money(money_amount)

    """this function written for keep the information of operation 
    the time_list is a list for containing times of operation
    the transaction_list is a list for containing type of operation
    the code_list is a list for containing code of operation 
    the amount_list is a list for containing operations amounts
    """

    def operations(self, time, pay_or_settle, code, amount):

        self.time_list.append(time)
        self.transaction_list.append(pay_or_settle)

        code = int(int(code) * math.pow(10, 14 - len(code)))
        self.code_list.append(code)
        self.amount_list.append(amount)

    """this function written for showing the operations and get from user number of last operations and show them"""

    def show_operations(self):
        time.sleep(1)
        print(200 * '-')

        number = input(
            "enter number of last operations:\nif you want to back press 0\n")
        if number == '0':
            if self.ob_employee.option_2 == "3":

                list(bank.bank_employees_list[bank.user_name].keys())[
                    0].sub_menu_2()

            else:
                self.sub_menu('2')

        if int(number) < 1 or int(number) > len(self.time_list) or number.isnumeric() == False:

            self.delay(self.show_operations)

        else:

            time.sleep(1)

            for item in range(int(number)):

                print("\ntime : ", self.time_list[(len(self.time_list) - item)-1],
                      "transaction type : ", self.transaction_list[(len(
                          self.transaction_list) - item) - 1],
                      "code : ", self.code_list[(len(
                          self.code_list) - item) - 1],
                      "amount : ", self.amount_list[(len(self.amount_list) - item) - 1], '\n')

    """this function written for requesting for loan and have loan_dict for containing general information of loans and have 
    flag_dict for loan penalty situation specify and have counter_dict for count the loan installment payment times
    and this function check if the user requests number is out of maximum number , it prevent to apply loan to client"""

    def loan_request(self):

  

        if len(self.loan_dict) > 2:
            time.sleep(1)
            print(200 * '-')
            print("\nyour loans number is achieve to maximum\n")
            if self.ob_employee.option_2 == "3":
                list(bank.bank_employees_list[bank.user_name].keys())[0].sub_menu_2()

            else:
                self.menu()

        else:
            time.sleep(1)
            print(200 * '-')

            loan_type = input("""enter No type of the loan that you want :\n1.long time loan with 60 month deadline and %5 profit and its amount : 500000000 Rials for accounts that have 100000000 Rials or more\n2.short time loan with 12 month deadline and %1 profit and its amount : 50000000 Rials for accounts that have 10000000 Rials or more\nif you want to back , press 0\n""")
            if loan_type == '0':
                if self.ob_employee.option_2 == "3":
                    list(bank.bank_employees_list[bank.user_name].keys())[
                        0].sub_menu_2()

                else:
                    self.sub_menu('2')

            if loan_type == '1':

                if self.validity < 100000000:
                    time.sleep(1)
                    print("\nsorry\nyour vilidity is not enough for loan\n")
                    if self.ob_employee.option_2 == "3":
                        list(bank.bank_employees_list[bank.user_name].keys())[
                            0].sub_menu_2()

                    else:
                        self.menu()
                else:
                    self.validity += 500000000

                    code = str(datetime.datetime.now(
                    ).year) + str(datetime.datetime.now().month)+str(datetime.datetime.now().day) + str (datetime.datetime.now().second)
                    code = int(int(code) * math.pow(10, 10 - len(code)))
                    self.loan_dict[code] = {
                        500000000: datetime.datetime.today()}
                    self.flag_dict[code] = True
                    self.counter_dict[code] = 0
                    bank.debtors_list.add(self.user_name)
                    self.switch = True
                    time.sleep(1)
                    self.operations(datetime.datetime.now(), "pay loan", str(datetime.datetime.now().year) + str(datetime.datetime.now().month)+str(
                        datetime.datetime.now().day)+str(datetime.datetime.now().hour)+str(datetime.datetime.now().minute)+str(datetime.datetime.now().second), '500000000')
                    print(f"""\ncongratulations\nthe long time loan apply for you\nyour loan code is : {code} 
                        \nplease pay the payment before your monthly timing for your loan is out because otherwise your month payment include %5 penalty\n""")
            elif loan_type == '2':

                if self.validity < 10000000:
                    time.sleep(1)
                    print("\nsorry\nyour vilidity is not enough for loan\n")
                    if self.ob_employee.option_2 == "3":
                        list(bank.bank_employees_list[bank.user_name].keys())[
                            0].sub_menu_2()

                    else:
                        self.menu()
                else:
                    self.validity += 50000000

                    code = str(datetime.datetime.now(
                    ).year) + str(datetime.datetime.now().month)+str(datetime.datetime.now().day) + str (datetime.datetime.now().second)
                    code = int(int(code) * math.pow(10, 10 - len(code)))
                    self.loan_dict[code] = {
                        50000000: datetime.datetime.today()}
                    self.flag_dict[code] = True
                    self.counter_dict[code] = 0
                    bank.debtors_list.add(self.user_name)
                    self.switch = True

                    time.sleep(1)
                    self.operations(datetime.datetime.now(), "pay loan", str(datetime.datetime.now().year) + str(datetime.datetime.now().month)+str(
                        datetime.datetime.now().day)+str(datetime.datetime.now().hour)+str(datetime.datetime.now().minute)+str(datetime.datetime.now().second), '50000000')

                    print(f"""\ncongratulations\nthe short time loan apply for you\nyour loan code is : {code} 
                        \nplease pay the payment before your monthly timing for your loan is out because otherwise your month payment include %5 penalty\n""")
            else:
                self.delay(self.loan_request)

    """this function written for showing active loans in show information section"""

    def show_loans(self):

        lists = self.loan_dict

        time.sleep(1)
        print(200 * '-')

        for counter in range(len(lists)):

            print("\nyou have installment_payment for loan by code : ", list(lists)[counter], "in day number : ",
                  list(lists[list(lists)[counter]].values())[0].day,  "in months\n")

    """this function written for installment payment loans"""

    def installment_payment(self):

        time.sleep(1)
        print(200 * '-')

        loan_code = input(
            "enter the loan code:\nif you want to back , press 0\n")
        if loan_code == '0':
            if self.ob_employee.option_2 == "3":
                list(bank.bank_employees_list[bank.user_name].keys())[
                    0].sub_menu_2()

            else:
                self.sub_menu('2')

        if int(loan_code) not in self.loan_dict.keys():
            self.delay(self.installment_payment)
        else:

            monthly_payment = (list(self.loan_dict[int(loan_code)].keys())[
                               0] * 13) / (2400 * 100)
            if self.flag_dict[int(loan_code)] == True:

                monthly_payment += (monthly_payment/20)

            if self.validity < monthly_payment:
                time.sleep(1)

                print("\nyour validity is not enough\nplease charge it\n")
                self.menu()
            else:

                self.validity -= monthly_payment
                self.operations(datetime.datetime.now(), "installment payment",
                                str(datetime.datetime.now().year) + str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+str(
                    datetime.datetime.now().hour)+str(datetime.datetime.now().minute)+str(datetime.datetime.now().second),
                    monthly_payment)
                self.flag_dict[int(loan_code)] == False

                self.counter_dict[int(loan_code)] += 1
                if list(self.loan_dict[int(loan_code)].keys())[0] == 500000000:
                    if self.counter_dict[int(loan_code)] == 60:
                        self.loan_dict.pop(int(loan_code))
                        bank.debtors_list.remove(self.user_name)
                        self.switch = False

                else:
                    if self.counter_dict[int(loan_code)] == 12:
                        self.loan_dict.pop(int(loan_code))
                        bank.debtors_list.remove(self.user_name)
                        self.switch = False

        difference = (((datetime.datetime.now().year - list(self.loan_dict[int(loan_code)].values())[0].year) * 360) + ((datetime.datetime.now().month - list(self.loan_dict[int(loan_code)].values())[0].month) * 30) + (datetime.datetime.now().day - list(self.loan_dict[int(loan_code)].values())[0].day))

        if difference // 30 > self.counter_dict[int(loan_code)]:

            self.flag_dict[int(loan_code)] == True
