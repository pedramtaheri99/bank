"""this file contain employee class and its functions"""

import bank
from bank import *
from client import *
from person import person
import time


"""this class make for employees """


class employee (person):


    def __init__(self):

        self
        person.__init__(self)

    """this function written for menu and the options of menu """
    option_2 = None

    def menu(self):

        self.show_iformation()
        time.sleep(1)
        print(200 * '-')
        subject_menu = input(
            "enter subject number:\n1.for employee\n2.for client\nif you want to back , press 0\n")

        match subject_menu:

            case '0':

                self.option_2 = None

                list(bank.bank_employees_list[bank.get_employee_username()].keys())[0].menu()
                
                 

            case '1':

                self.sub_menu_1(subject_menu)

            case'2':

                self.sub_menu_1(subject_menu)

            case _:
                self.delay(self.menu)

    """this function is second menu """

    def sub_menu_1(self, subject_menu):

        if subject_menu == '1':

            time.sleep(1)
            print(200 * '-')

            option_1 = input(
                "enter option number:\n1.edit password \n2.edit phone number \n3.edit address \nif you want to back , press 0\n")

            match option_1:

                case "0":
                    self.menu()

                case "1":
                    self.restore_password()
                    self.sub_menu_1('1')
                case "2":

                    self.set_phone_number()
                    self.sub_menu_1('1')

                case "3":
                    self.set_address()
                    self.sub_menu_1('1')

                case _:
                    self.delay_with_parameter(self.sub_menu_1, '1')
        else:

            time.sleep(1)
            print(200 * '-')

            self.option_2 = input(
                "enter option number : \n1.create client \n2.delete client \n3.services \n4.edit\nif you want to back , press 0\n")

            match self.option_2:
                case "0":
                    self.menu()
                case "1":
                    self.create_client()
                    self.sub_menu_1('2')
                case "2":

                    self.delete_client()
                    self.sub_menu_1('2')

                case "3":
                    self.sub_menu_2()
                case "4":
                    self.sub_menu_3()
                case _:
                    self.delay_with_parameter(self.sub_menu_1, '2')

    """this function is third menu """

    def sub_menu_2(self):

        time.sleep(1)
        print(200 * '-')

        option = input(
            "enter option number:\n1.search client \n2.show debtors list \n3.charge money\n4.get money\n5.move money\n6.show operations\n7.loan request\n8.installment payment\nif you want to back , press 0\n")

        match option:
            case "0":
                self.sub_menu_1('2')

            case "1":
                self.search_client('search')
                self.sub_menu_2()
            case "2":

                self.show_debtors_list()
                self.sub_menu_2()

            case "3":
                self.search_client('charge money')
                self.sub_menu_2()
            case "4":
                self.search_client('get money')
                self.sub_menu_2()
            case "5":
                self.search_client('move money')
                self.sub_menu_2()
            case "6":
                self.search_client('show operations')
                self.sub_menu_2()
            case "7":
                self.search_client('loan request')
                self.sub_menu_2()
            case "8":
                self.search_client('installment payment')
                self.sub_menu_2()
            case _:
                self.delay(self.sub_menu_2)

    """this function is fourth menu """

    def sub_menu_3(self):

        time.sleep(1)
        print(200 * '-')

        option = input(
            "enter option number:\n1.user name \n2.password \n3.name\n4.family\n5.validity\n6.phone number\n7.address\n8.national code\n9.birth date\nif you want to back , press 0\n")

        match option:
            case "0":
                self.sub_menu_1('2')

            case "1":
                self.search_client('edit user name')
                self.sub_menu_3()
            case "2":

                self.search_client('edit password')
                self.sub_menu_3()

            case "3":
                self.search_client('edit name')
                self.sub_menu_3()
            case "4":
                self.search_client('edit family')
                self.sub_menu_3()
            case "5":
                self.search_client('edit validity')
                self.sub_menu_3()
            case "6":
                self.search_client('edit phone number')
                self.sub_menu_3()
            case "7":
                self.search_client('edit address')
                self.sub_menu_3()
            case "8":
                self.search_client('edit national code')
                self.sub_menu_3()
            case "9":
                self.search_client('edit birth date')
                self.sub_menu_3()
            case _:
                self.delay(self.sub_menu_3)

    """this function written for showing the employee general information"""

    def show_iformation(self):

        time.sleep(1)
        print(200 * '-')
        print(f"\nthe information of user {self.user_name} :\n")
        print("total name : " + self.name + " " + self.family)
        print("phone number : " + self.phone_number)
        print("address : " + self.address)
        print("national_code : ", self.national_code)
        print("birth day :", self.birth_year, "/",
              self.birth_month, "/", self.birth_day)

    """this function written for creating clients by employees"""

    def create_client(self):

        user = client()
        user.ob_employee = self
        user.set_user_name()
        user.set_password()
        user.set_name()
        user.set_family()
        user.set_phone_number()
        user.set_address()
        user.set_national_code()
        user.set_birth_date()
        user.set_validity()
        bank.bank_clients_list[user.user_name] = {user: user.password}

    """this function written for deleting clients by employees"""

    def delete_client(self):

        time.sleep(1)
        print(200 * '-')
        user_name = input(
            "enter the user name:\nif you want to back , press 0\n")
        if user_name == '0':
            self.sub_menu_1('2')
        if user_name not in bank.bank_clients_list.keys():
            time.sleep(1)
            print("\nthe user name not found\please try again\n")

            self.delete_client()
        else:
            time.sleep(1)
            answer = input(
                "are you sure for delete user?\n1.yes\n2.no\nif you want to back , press 0\n")

            match answer:
                case '0':
                    self.delete_client()
                case '1':
                    bank.bank_clients_list.pop(user_name)
                case '2':
                    self.sub_menu_1('2')
                case _:
                    self.delay(self.delete_client)

    """this function written for searching and done some operations for clients by employees"""

    def search_client(self, request):
        time.sleep(1)
        print(200 * '-')
        user_name = input(
            "enter the user name:\nif you want to back , press 0\n")
        if user_name == '0':
            if list(request)[0] == 'e':
                self.sub_menu_3()

            else:

                self.sub_menu_2()

        if user_name not in bank.bank_clients_list.keys():

            print("\nthe user name not found\ntry again\n")

            self.search_client(request)
        else:
            list(bank.bank_clients_list[user_name].keys())[
                0].show_iformation()
            match request:
                case 'charge money':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].charge_money()
                case 'get money':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].get_money()
                case 'move money':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].move_money()
                case 'show operations':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].show_operations()
                case 'loan request':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].loan_request()
                case 'installment payment':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].installment_payment()
                case 'edit user name':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].set_user_name()
                case 'edit password':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].restore_password()
                case 'edit name':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].set_name()
                case 'edit family':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].set_family()
                case 'edit validity':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].set_validity()
                case 'edit phone number':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].set_phone_number()
                case 'edit address':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].set_address()
                case 'edit national code':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].set_national_code()
                case 'edit birth date':
                    list(bank.bank_clients_list[user_name].keys())[
                        0].set_birth_date()

                case _:
                    print("\t")

    """this function written for showing the clients who not complete their loan installment payment to employees"""

    def show_debtors_list(self):

        if len(bank.debtors_list) != 0:

            time.sleep(1)
            print(200 * '-')
            print("\nthe debtors :\n")

            for item in bank.debtors_list:
                print(f"\nthe active loans for client {item} : ", list(bank.bank_clients_list[item].keys(
                ))[0].loan_dict.keys(), "\n")
        else:
            print("\nbank has no debtor yet")
