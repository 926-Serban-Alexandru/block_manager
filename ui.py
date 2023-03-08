#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
from functions import *
from copy import deepcopy


def display_all(elements):
    for i in range(len(elements["apartaments"])):
        print("Apartament number: " + str(get_ap(elements, "apartaments", i)))
        print("Water expenses: " + str(get_ap(elements, "water", i)) + " RON")
        print("Heating expenses: " + str(get_ap(elements, "heating", i)) + " RON")
        print("Gas expenses: " + str(get_ap(elements, "gas", i)) + " RON")
        print("Electricity expenses: " + str(get_ap(elements, "electricity", i)) + " RON")
        print("Other expenses: " + str(get_ap(elements, "other", i)) + " RON")
        print(" ")


def display_apartament(elements, apartament_number):
    i = get_apartament_index(elements, apartament_number)
    print("Apartament number: " + str(get_ap(elements, "apartaments", i)))
    print("Water expenses: " + str(get_ap(elements, "water", i)) + " RON")
    print("Heating expenses: " + str(get_ap(elements, "heating", i)) + " RON")
    print("Gas expenses: " + str(get_ap(elements, "gas", i)) + " RON")
    print("Electricity expenses: " + str(get_ap(elements, "electricity", i)) + " RON")
    print("Other expenses: " + str(get_ap(elements, "other", i)) + " RON")
    print(" ")


def display_expenses_higher_than(elements, sum):
    p = 0
    for i in range(len(elements["apartaments"])):
        apartament_nr = get_ap(elements, "apartaments", i)
        if calculate_total_expenses_apartament(elements, apartament_nr) > sum:
            print(apartament_nr)
            p += 1
    if p == 0:
        print(f"There are no apartaments with the total expenses higher than {sum}.")


def display_expenses_lower_than(elements, sum):
    p = 0
    for i in range(len(elements["apartaments"])):
        apartament_nr = get_ap(elements, "apartaments", i)
        if calculate_total_expenses_apartament(elements, apartament_nr) < sum:
            print(apartament_nr)
            p += 1
    if p == 0:
        print(f"There are no apartaments with the total expenses lower than {sum}.")


def display_expenses_equal_to(elements, sum):
    p = 0
    for i in range(len(elements["apartaments"])):
        apartament_nr = get_ap(elements, "apartaments", i)
        if calculate_total_expenses_apartament(elements, apartament_nr) == sum:
            print(apartament_nr)
            p += 1
    if p == 0:
        print(f"There are no apartaments with the total expenses equal to {sum}.")


def display_expenses(params_list, elements):
    if len(params_list) == 0:
        display_all(elements)
    elif len(params_list) == 1:
        apartament_number = int(params_list[0])
        if apartament_number not in elements["apartaments"]:
            print(f"Sorry, but the apartament {params_list[0]} is not registered.")
        else:
            display_apartament(elements, apartament_number)
    elif len(params_list) == 2:
        if params_list[0] == '>':
            print(f"The apartaments with the total expenses higher than {params_list[1]} are: ")
            display_expenses_higher_than(elements, int(params_list[1]))
            print(" ")
        elif params_list[0] == '<':
            print(f"The apartaments with the total expenses lower than {params_list[1]} are: ")
            display_expenses_lower_than(elements, int(params_list[1]))
            print(" ")
        elif params_list[0] == '=':
            print(f"The apartaments with the total expenses equal to {params_list[1]} are: ")
            display_expenses_equal_to(elements, int(params_list[1]))
            print(" ")
        else:
            return False
    else:
        return False


def display_total_expenses_type(params_list, elements):
    # A function that displays the total amount of expenses for a certain type.
    amount = calculate_total_expenses_type(params_list, elements)
    print(f"The total amount of expenses for {params_list[0]} is: " + str(amount))
    print(" ")


def wrong_undo():
    print("There aren't any actions to undo.")


def wrong_input():
    print("Sorry, you've entered an incorrect command. Please try again.\n")


def print_command_menu():
    print("\n\tAdd transaction. (add)")
    print("\tRemove")
    print("\tReplace")
    print("\tDisplay expenses. (list)")
    print("\tFilter. (filter)")
    print("\tExit the program. (exit)\n")


def run_menu_ui():
    elements = init_elements()
    history_list = []
    history_list.append(deepcopy(elements))

    while True:
        print_command_menu()
        cmd_line = input("Input the command and the arguments: ")
        cmd_word, cmd_params = split_command_user(cmd_line)
        params_list = params_split(cmd_params)
        try:
            if cmd_word == "add":
                if add_transaction(params_list, elements) is False:
                    wrong_input()
                else:
                    history_list.append(deepcopy(elements))
            elif cmd_word == "remove":
                if remove_expenses(params_list, elements) is False:
                    wrong_input()
                else:
                    history_list.append(deepcopy(elements))
            elif cmd_word == "replace":
                if replace_expenses(params_list, elements) is False:
                    wrong_input()
                else:
                    history_list.append(deepcopy(elements))
            elif cmd_word == "list":
                if display_expenses(params_list, elements) is False:
                    wrong_input()
            elif cmd_word == "sum":
                if calculate_total_expenses_type(params_list, elements) is False:
                    wrong_input()
                else:
                    display_total_expenses_type(params_list, elements)
            elif cmd_word == "filter" and len(params_list) == 1:
                if filter(params_list, elements) is False:
                    wrong_input()
                else:
                    history_list.append(deepcopy(elements))
            elif cmd_word == "undo" and params_list == []:
                if len(history_list) == 1:
                    wrong_undo()
                else:
                    history_list.pop()
                    elements = deepcopy(history_list[-1])
            elif cmd_word == "exit":
                return
            else:
                wrong_input()
        except KeyError:
            wrong_input()
        except ValueError:
            wrong_input()
