"""this file contain person class and its functions"""

import time
import datetime
import bank

"""this class make for users consist of clients and employees and their classes inherit from this class"""


class person:

    def __init__(self):

        self
    """this function written for get and set the user name"""

    def set_user_name(self):

        time.sleep(1)
        print(200 * '-')
        user_name_2 = input(
            "enter user name:\nthe user name should be have at least one captal word and one number\nif you want to back , press 0\n")
        if user_name_2 == '0':

            if str(type(self)) == "<class 'employee.employee'>":
                
                    bank.get_boss_password()
               


            else:
                if self.ob_employee.option_2 == "4":

                    self.ob_employee.sub_menu_3()
                else:

                    self.ob_employee.sub_menu_1('2')

        if self.check_user_name(user_name_2) == True:

            self.user_name = user_name_2

        else:

            self.delay(self.set_user_name)

    """this function written for get and set the password"""

    def set_password(self):
        time.sleep(1)
        print(200 * '-')

        password_2 = input(
            "enter password:\nthe password should be have 6 characters\nif you want to back , press 0\n")
        if password_2 == '0':
            if str(type(self)) == "<class 'employee.employee'>":
                bank.get_boss_password()

            else:
                if self.ob_employee.option_2 == "4":

                    self.ob_employee.sub_menu_3()
                else:

                    self.ob_employee.sub_menu_1('2')

        if self.check_password(password_2) == True:
            self.password = password_2

        else:
            self.delay(self.set_password)

    """this function written for get and set the name"""

    def set_name(self):
        time.sleep(1)
        print(200 * '-')
        name_2 = input("enter name:\nif you want to back , press 0\n")
        if name_2 == '0':
            if str(type(self)) == "<class 'employee.employee'>":
                bank.get_boss_password()

            else:
                if self.ob_employee.option_2 == "4":

                    self.ob_employee.sub_menu_3()
                else:

                    self.ob_employee.sub_menu_1('2')
        if self.check_name_and_family(name_2) == False:
            self.delay(self.set_name)
        else:
            self.name = self.check_name_and_family(name_2)

    """this function written for get and set the family"""

    def set_family(self):
        time.sleep(1)
        print(200 * '-')

        family_2 = input("enter family:\nif you want to back , press 0\n")
        if family_2 == '0':
            if str(type(self)) == "<class 'employee.employee'>":
                bank.get_boss_password()

            else:
                if self.ob_employee.option_2 == "4":

                    self.ob_employee.sub_menu_3()
                else:

                    self.ob_employee.sub_menu_1('2')
        if self.check_name_and_family(family_2) == False:
            self.delay(self.set_family)
        else:
            self.family = self.check_name_and_family(family_2)

    """this function written for get and set the phone number and chek and prevent to its incorrect amounts"""

    def set_phone_number(self):

        time.sleep(1)
        print(200 * '-')

        phone_number_2 = input(
            "enter phone number:\nif you want to back , press 0\n")
        if phone_number_2 == '0':

            if str(type(self)) == """<class 'employee.employee'>""":
                if bank.input_main == '3':

                    bank.get_boss_password()
                else:
                    self.sub_menu_1('1')


            else:

                if self.ob_employee.option_2 == None:
                    self.sub_menu('1')

                elif self.ob_employee.option_2 == '4':
                    self.ob_employee.sub_menu_3()
                else:
                    self.ob_employee.sub_menu_1('2')
            
                

        if phone_number_2.isnumeric() == False or len(phone_number_2) != 11:
            self.delay(self.set_phone_number)
        else:
            self.phone_number = phone_number_2

    """this function written for get and set the users city """

    def set_address(self):
        time.sleep(1)
        print(200 * '-')

        city_2 = input("enter city name : \nif you want to back , press 0\n")
        if city_2 == '0':
            if str(type(self)) == """<class 'employee.employee'>""":

                if bank.input_main == '3':

                    bank.get_boss_password()
                else:
                    self.sub_menu_1('1')

            else:

                if self.ob_employee.option_2 == None:
                    self.sub_menu('1')

                elif self.ob_employee.option_2 == '4':
                    self.ob_employee.sub_menu_3()
                else:
                    self.ob_employee.sub_menu_1('2')

        if self.check_city(city_2) == False:
            self.delay(self.set_address)
        else:
            self.city = self.check_city(city_2)
            self.set_main_address(self.city)

    """this function written for get and set the address"""

    def set_main_address(self, city):
        time.sleep(1)
        print(200 * '-')

        address_2 = input(
            "enter address : \nsplit details with / \nif you want to back , press 0\n")
        if address_2 == '0':
            if str(type(self)) == """<class 'employee.employee'>""":

                if bank.input_main == '3':

                    bank.get_boss_password()
                else:
                    self.sub_menu_1('1')

            else:

                if self.ob_employee.option_2 == None:
                    self.sub_menu('1')

                elif self.ob_employee.option_2 == '4':
                    self.ob_employee.sub_menu_3()
                else:
                    self.ob_employee.sub_menu_1('2')

        if self.check_address(address_2) == False:
            self.delay_with_parameter(self.set_main_address, self.city)
        else:
            self.address = city+"/"+self.check_address(address_2)

    """this function written for get and set the national code and chek and prevent to its incorrect amounts"""

    def set_national_code(self):
        time.sleep(1)
        print(200 * '-')

        national_code_2 = input(
            "enter national code:\nif you want to back , press 0\n")
        if national_code_2 == '0':
            if str(type(self)) == "<class 'employee.employee'>":
                bank.get_boss_password()

            else:
                if self.ob_employee.option_2 == "4":

                    self.ob_employee.sub_menu_3()
                else:

                    self.ob_employee.sub_menu_1('2')

        if national_code_2.isnumeric() == False or len(national_code_2) != 10:
            self.delay(self.set_national_code)
        else:
            self.national_code = int(national_code_2)

    """this function written for get and set the birth date of users"""

    def set_birth_date(self):

        time.sleep(1)
        print(200 * '-')

        birth_year_2 = input(
            "enter year of birth:\nif you want to back , press 0\n")
        if birth_year_2 == '0':
            if str(type(self)) == "<class 'employee.employee'>":
                bank.get_boss_password()

            else:
                if self.ob_employee.option_2 == "4":

                    self.ob_employee.sub_menu_3()
                else:

                    self.ob_employee.sub_menu_1('2')
        else:
            time.sleep(1)
            birth_month_2 = input(
                "enter month of birth: \nif you want to back , press 0\n")
            if birth_month_2 == '0':
                self.set_birth_date()
            else:
                time.sleep(1)
                birth_day_2 = input(
                    "enter day of birth: \nif you want to back , press 0\n")
                if birth_day_2 == '0':
                    self.set_birth_date()
                else:

                    if self.check_birth_day(birth_year_2, birth_month_2, birth_day_2) == False:
                        self.delay(self.set_birth_date)

                    else:
                        self.birth_year = int(birth_year_2)
                        self.birth_month = int(birth_month_2)
                        self.birth_day = int(birth_day_2)

    """this function written for changing the password"""

    def restore_password(self):

        time.sleep(1)
        print(200 * '-')
        pass_check = input(
            "enter previous password:\nif you want to back , press 0\n")

        if pass_check == '0':

            if str(type(self)) == "<class 'client.client'>":
                if self.ob_employee.option_2 == None:
                    self.sub_menu('1')
                else:
                    self.ob_employee.sub_menu_3()

            else:
                self.sub_menu_1('1')

        if self.password == pass_check:

            time.sleep(1)

            new_pass = input(
                "enter new password: \nthe password should be have 6 characters\nif you want to back , press 0\n")
            if new_pass == '0':

                self.restore_password()

            time.sleep(1)

            new_pass2 = input(
                "enter new password again: \nif you want to back , press 0\n")

            if new_pass2 == '0':
                self.restore_password()
            if new_pass == new_pass2 and self.check_password(new_pass2) == True:

                self.password = new_pass2
                if str(type(self)) == "<class 'client.client'>":
                    bank.bank_clients_list[self.user_name].update(
                        {self: new_pass2})
                else:

                    bank.bank_employees_list[self.user_name].update(
                        {self: new_pass2})

            else:

                time.sleep(1)

                print("\nerror\nthe two new password must be same\n")

                self.restore_password()

        else:
            self.delay(self.restore_password)

    """this function written to check user name and prevent to its incorrect amounts"""

    def check_user_name(self, user_name):
        number_flag = False
        word_flag = False
        for item in user_name:
            if ord(item) >= 65 and ord(item) <= 90:

                word_flag = True
            if ord(item) >= 48 and ord(item) <= 57:
                number_flag = True
        if number_flag == True and word_flag == True:
            return True
        else:
            return False

    """this function written to check password and prevent to its incorrect amounts"""

    def check_password(self, password):

        if len(password) >= 6:
            return True
        return False

    """this function written to check name and family and prevent to its incorrect amounts"""

    def check_name_and_family(self, value):

        flag = True

        word = ""

        for item in value:
            if (ord(item) <= 90 and ord(item) >= 65) or (ord(item) <= 122 and ord(item) >= 97):

                word += item
            else:

                return False
        for letter in value:
            if letter == " ":
                flag = False
        if flag == False:
            return False
        if len(word) < 3:
            return False
        return word
    """this function written to check city and prevent to its incorrect amounts"""

    def check_city(self, city):

        flag = True

        city1 = ""

        for item in city:
            if (ord(item) == 32) or (ord(item) <= 65 and ord(item) >= 90) or (ord(item) <= 122 and ord(item) >= 97) or (ord(item) >= 47 and ord(item) <= 57) or (ord(item) == 32):

                city1 += item

            else:

                return False
        for word in city1:
            if word == " ":
                flag = False
        if flag == False:
            return False
        if len(city1) < 2:
            return False
        return city1

    """this function written to check address and prevent to its incorrect amounts"""

    def check_address(self, address):

        flag = True

        address1 = ""

        for item in address:
            if (ord(item) == 32) or (ord(item) <= 65 and ord(item) >= 90) or (ord(item) <= 122 and ord(item) >= 97) or (ord(item) >= 47 and ord(item) <= 57) or (ord(item) == 32):

                address1 += item

            else:

                return False
        for word in address1:
            if word == " ":
                flag = False
        if flag == False:
            return False
        if len(address1) < 8:
            return False
        return address1

    """this function written to check birth date and prevent to its incorrect amounts"""

    def check_birth_day(self, year, month, day):

        if  year.isnumeric() == False or int(year) > int(datetime.datetime.now().year) or int(year) < 1900 :
            return False
        elif  year.isnumeric() == False or int(month) > 12 or int(month) < 1 :

            return False
        if year.isnumeric() == False or int(day) > 30 or int(day) < 1 :

            return False

    """this function designed for times the user insert incorrect data and print error and call again the intended function"""

    def delay(self, function):

        time.sleep(1)
        print(200 * '-')

        print("\ninvalid input\nplease try again\n")
        function()

    def delay_with_parameter(self, function, parameter):
        time.sleep(1)
        print(200 * '-')

        print("\ninvalid input\nplease try again\n")
        function(parameter)
