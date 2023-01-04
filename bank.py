"""this program is designed for bank and work with it by clients and bank employees  
it can be expanded"""


"""this file designed for managing main program and have main important variable and basic menu
bank_client_list is a dicyionary for keep clients object with their user name and password
bank_employees_list is a dicyionary for keep bank employees object with their user name and password
the banned_list is list for keeping the accounts who entered wrong password for 3 time consecutively
the debtors_list is a set for keeping clients who get loan from bank
"""


import time
import boss
bank_clients_list = {}
bank_employees_list = {}
banned_list = []
debtors_list = set({})

"""this function keep program running while the user want to exit"""


def main_app():

    say_welcome()
    introduction()


"""in this function user specify the type user"""


def welcome():

    time.sleep(1)
    print(200 * '-')
    global input_main
    input_main = input(
        "please select one of user number type : \n1.client \n2.employee \n3.boss\nif you want to exit , press 0\n")

    return input_main


"""this function welcome users"""


def say_welcome():
    time.sleep(1)
    print("welcome to app\n")


"""this function is a gate to enter for users"""


def introduction():

    answer = welcome()
    match answer:
        case '0':
            closing()

        case "1":

            get_client_username()

        case "2":

            get_employee_username()

        case "3":
            get_boss_password()

        case _:
            delay(introduction)


"""this function get clients user name """


def get_client_username():

    basic_repetition = 0

    time.sleep(1)

    print(200 * '-')

    user_name = input("enter user name:\nif you want to back , press 0 \n")
    if user_name == '0':
        introduction()
    elif user_name in banned_list:

        time.sleep(1)

        print(
            "\nyour account is banned\nplease go to employees for activating the account\n")
        introduction()

    elif check_client_username(user_name) != True:
        time.sleep(1)

        print("\nthe user name not found\ntry again\n")
        get_client_username()
    else:

        get_client_password(user_name, basic_repetition)


"""this function get clients password """


def get_client_password(user_name, repetition):

    time.sleep(1)

    password = input(
        "enter password:\nwarning : the password after 3 time incorrect entered continuously lead to banning acount\nif you want to back , press 0 \n")
    if password == '0':
        get_client_username()
    elif check_client_password(user_name, password) != True:

        repetition += 1

        if repetition == 3:
            time.sleep(1)

            print(
                "\nyour account is banned\nplease go to employees for activating the account\n")

            banned_list.append(user_name)
            introduction()
        else:

            time.sleep(1)

            print("\npassword is incorrect\ntry again\n")
            get_client_password(user_name, repetition)

    else:

        list(bank_clients_list[user_name].keys())[0].menu()


"""this function get employees user name """


def get_employee_username():

    time.sleep(1)

    print(200 * '-')

    global user_name
    user_name = input("enter user name:\nif you want to back , press 0 \n")
    if user_name == '0':
        introduction()

    elif check_employee_user_name(user_name) != True:
        time.sleep(1)

        print("\nthe user name not found\ntry again\n")
        get_employee_username()
    else:

        get_employee_password(user_name)


"""this function get employees password """


def get_employee_password(user_name):

    time.sleep(1)
    password = input("enter password:\nif you want to back , press 0 \n")
    if password == '0':
        get_employee_username()
    elif check_employee_password(user_name, password) == False:

        time.sleep(1)

        print("\npassword is incorrect\ntry again\n")

        get_employee_password(user_name)

    else:

        list(bank_employees_list[user_name].keys())[0].menu()


def get_boss_password():

    time.sleep(1)
    password = input("enter boss password:\nif you want to back , press 0 \n")
    if password == '0':
        introduction()

    elif password != "bankboss":

        time.sleep(1)

        print("\npassword is incorrect\ntry again\n")

        get_boss_password()

    else:

        boss.create_employee()


"""this function designed for closing the app with user confirming"""


def closing():

    time.sleep(1)
    print(200 * '-')
    exit_confirm = input(
        "are you sure to close the app? \n1.yes  \n2.no\nif you want to back , press 0\n")
    match exit_confirm:
        case '0':
            introduction()

        case '1':
            time.sleep(1)
            print("\nhave nice day")
        case '2':
            introduction()

        case _:
            delay(closing)


"""this function check that client user name is not incorrect"""


def check_client_username(user_name):

    if user_name in bank_clients_list.keys():

        return True
    else:
        return False


"""this function check that client password is not incorrect"""


def check_client_password(user_name, password):

    if password in bank_clients_list[user_name].values():
        return True
    else:

        return False


"""this function check that employees user name is not incorrect"""


def check_employee_user_name(user_name):

    if user_name in bank_employees_list.keys():

        return True
    else:
        return False


"""this function check that employees password is not incorrect"""


def check_employee_password(user_name, password):

    if password in bank_employees_list[user_name].values():
        return True
    else:

        return False


"""this function designed for times the user insert incorrect data and print error and call again the intended function"""


def delay(function):
    time.sleep(1)
    print(200 * '-')

    print("\ninvalid input\nplease try again\n")
    function()


def delay_with_parameter(function, parameter):
    time.sleep(1)
    print(200 * '-')

    print("\ninvalid input\nplease try again\n")
    function(parameter)
