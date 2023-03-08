#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions.
#
# ==================== GETTER FUNCTIONS =================
def get_apartament_index(elements, apartament_number):
    """
  A function that gets the index of an apartament in the list of apartaments from the dictionary elements.
  Input - a dictionary elements, a positive integer apartament_number
  Output - a >= 0 integer i representing the index of the given apartament
  """
    i = elements["apartaments"].index(apartament_number)
    return i


def get_ap(elements, type, i):
    """
  elements - dictionary
  type - string in "water" / "apartaments" /..
  i - integer - index
  """
    return elements[type][i]


# ==================== SETTER FUCNTIONS ================
def set_ap_expenses(elements, type, i, expense):
    """
  elements - dictionary
  type - string in "water" / "apartaments" /..
  i - integer - index
  expense - integer
  """
    elements[type][i] = expense


# =======================================================
def init_elements():
    """
  A function that initialize the lists of elements(water, gas, heating etc.) with 10 items.
  Return - a dictionary with 10 items for each element. The items of the list from "apartaments" stands for the number
  of the apartament. The items for the rest of the lists stands for the amount of expenses.
  """
    return {
        "apartaments": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "water": [40, 53, 12, 28, 32, 74, 21, 98, 32, 100, 43, 27, 87, 110, 96],
        "heating": [50, 64, 34, 21, 44, 21, 40, 23, 42, 64, 87, 56, 43, 76, 98],
        "gas": [48, 21, 98, 52, 65, 32, 47, 87, 41, 63, 41, 63, 48, 96, 74],
        "electricity": [41, 23, 89, 65, 41, 23, 55, 19, 41, 54, 79, 21, 63, 150, 41],
        "other": [74, 12, 33, 25, 65, 41, 23, 79, 54, 15, 41, 87, 130, 41, 32]
    }


def split_command_user(cmd_line):
    """
  A function that splits the command line into the key-word ('add', 'remove', 'replace' etc.) and its parameters.
  Input - a string that represents the input command
  Output - A tuple of (<command word>, <command params>) in lowercase
  """
    cmd_line = cmd_line.strip()
    tokens = cmd_line.split(maxsplit=1)
    cmd_word = tokens[0].lower() if len(tokens) > 0 else None
    cmd_params = tokens[1].lower() if len(tokens) == 2 else None

    return cmd_word, cmd_params


def params_split(cmd_params):
    """
  A function that splits the command parameters in one-word strings.
  Input: a string containing the parameters of the command: cmd_params
  Output: a list of strings(words) params_list
  """
    if cmd_params == None:
        return []
    else:
        x = cmd_params.split()
        params_list = []
        for item in x:
            params_list.append(item)
        return params_list


def add_new_expenses(expense, amount):
    """
  A function that updates the amount of expenses.
  """
    expense += amount
    return expense


def add_new_apartment(elements, apartament_number):
    """
  A function that adds a new apartament to the dictionary elements a new with all the initial expenses to 0.
  Input - the dictionary of elements and an integer: apartament_number
  """
    elements["apartaments"].append(apartament_number)
    elements["water"].append(0)
    elements["heating"].append(0)
    elements["gas"].append(0)
    elements["electricity"].append(0)
    elements["other"].append(0)


def add_transaction(params_list, elements):
    """
  A function that adds a new transaction to a specific apartament. If the apartament doesn't exist, it's created with
  all the initial expenses to 0.
  add <apartment> <type> <amount>
  Input - a dictionary elements and a string containing the parameters of the command: cmd_params
  """
    if len(params_list) == 3:
        apartament_nr = int(params_list[0])
        amount = int(params_list[2])
        if apartament_nr not in elements["apartaments"]:
            add_new_apartment(elements, apartament_nr)
        i = get_apartament_index(elements, apartament_nr)
        expense = get_ap(elements, params_list[1], i)
        expense = add_new_expenses(expense, amount)
        set_ap_expenses(elements, params_list[1], i, expense)
    else:
        return False


def calculate_total_expenses_apartament(elements, apartament_nr):
    """
  A function that calculates the total expenses of an apartament.
  Input - a dictionary elements, an integer apartament_nr
  Output - an integer s, representing the sum of all the expenses
  """
    i = get_apartament_index(elements, apartament_nr)
    s = 0
    s = get_ap(elements, "water", i) + get_ap(elements, "gas", i) + get_ap(elements, "electricity", i) + get_ap(
        elements, "heating", i) + get_ap(elements, "other", i)
    return s


def remove_expenses_type(elements, type):
    """
  A function that removes the expenses of type type for every apartament in the list.
  Input - a dictionary elements and one string type, representing the type of utilities from which the expenses will be
  removed.
  Output - If the input is correct the function will execute the commands.
  """
    for i in range(len(elements["apartaments"])):
        set_ap_expenses(elements, type, i, 0)


def replace_expenses(params_list, elements):
    """
  replace <apartment> <type> with <amount>
  A function that replaces the expenses of a specific type from an apartament with an specific amount.
  Input - a dictionary elements, and a list of parameters, strings, params_list
  Output - a boolean False value if the input is not correct
  If the input is correct the function will execute the commands
  """
    if len(params_list) == 4:
        if params_list[2] == "with":
            if params_list[1] in elements:
                apartament_nr = int(params_list[0])
                apartament_nr_index = get_apartament_index(elements, apartament_nr)
                amount = int(params_list[3])
                set_ap_expenses(elements, params_list[1], apartament_nr_index, amount)
            else:
                return False
        else:
            return False
    else:
        return False


def remove_expenses_apartament(elements, apartament_nr):
    """
  A function that removes all the expenses for one specific apartament in the list.
  Input - a dictionary elements and one integer, representing the number of the apartament.
  Output - If the input is correct the function will execute the commands.
  """
    apartament_index = get_apartament_index(elements, apartament_nr)
    for type in elements:
        if type != "apartaments":
            set_ap_expenses(elements, type, apartament_index, 0)


def remove_expenses_apartament_to_apartament(elements, apartament_nr_start, apartament_nr_stop):
    """
  A function that removes the expenses from the starting apartament to the finish apartament inputed.
  Input - a dictionary elements and 2 integers, representing the starting and the finishing apartament number.
  Output - If the input is correct the function will execute the commands
  """
    apartament_nr_start_index = get_apartament_index(elements, apartament_nr_start)
    apartament_nr_stop_index = get_apartament_index(elements, apartament_nr_stop)
    for i in range(apartament_nr_start, apartament_nr_stop + 1):
        if i in elements["apartaments"]:
            j = get_apartament_index(elements, i)
            for type in elements:
                if type != "apartaments":
                    set_ap_expenses(elements, type, j, 0)


def remove_expenses(params_list, elements):
    """
  A function that removes the either the all the expenses for an apartament, the expenses for apartaments in a given
  range, or the expenses of a type for every apartament.
  remove <apartment> / remove <start apartment> to <end apartment> / remove <type>
  Input - a dictionary elements, and a list of parameters, strings, params_list
  Output - a boolean False value if the input is not correct
  If the input is correct the function will execute the commands
  """
    if len(params_list) == 1 or len(params_list) == 3:
        if len(params_list) == 1:
            if params_list[0] in elements:
                remove_expenses_type(elements, params_list[0])
            else:
                apartament_nr = int(params_list[0])
                remove_expenses_apartament(elements, apartament_nr)
        elif params_list[1] == "to":
            apartament_nr_start = int(params_list[0])
            apartament_nr_stop = int(params_list[2])
            if apartament_nr_start >= apartament_nr_stop:
                return False
            else:
                remove_expenses_apartament_to_apartament(elements, apartament_nr_start, apartament_nr_stop)
        else:
            return False
    else:
        return False


def calculate_total_expenses_type(params_list, elements):
    """
  A function that calculates the total expenses for a certain type (water, gas etc.)
  :param params_list: a list of parameters, strings, params_list
  :param elements: a dictionary elements
  :return: an integer amount, representing the total expenses for the input type
  """
    amount = 0  # The total amount of expenses.
    if len(params_list) == 1:
        if params_list[0] in elements:
            for i in range(len(elements["apartaments"])):
                expense = get_ap(elements, params_list[0], i)
                amount += expense
            return amount
        else:
            return False
    else:
        return False


def list_total_expenses_type(elements):
    """
  A function that creates a list of the total expenses for all types.
  :param elements: a dictionary elements
  :return: a list of integers: total_expenses
  """
    total_expenses = []
    for type in elements:
        if type != "apartaments":
            params_list = [type]
            amount = calculate_total_expenses_type(params_list, elements)
            total_expenses.append(amount)
    return total_expenses


def calculate_total_expenses_for_all_apartaments(elements):
    """
  A function that calculates the total amount of expenses for all apartaments and adds them to a list.
  :param elements: a dictionary elements
  :return: a list of integers: total_expenses
  """
    total_expenses = []
    for apartament_nr in elements["apartaments"]:
        amount = calculate_total_expenses_apartament(elements, apartament_nr)
        total_expenses.append(amount)
    return total_expenses


def filter_by_amount(amount, elements):
    """
  A function that filters the list of the expenses for each type and keeps only the expenses smaller than a given
  amount.
  :param amount: an integer representing the filter criteria
  :param elements: a dictionary, elements
  If the input is correct the function will execute the commands.
  """
    for type in elements:
        if type != "apartaments":
            for i in range(len(elements[type])):
                if get_ap(elements, type, i) >= amount:
                    set_ap_expenses(elements, type, i, 0)


def filter(params_list, elements):
    """
  A function that filters the lists of expenses after a given criteria.
  :param params_list: a list of parameters, strings, params_list
  :param elements: a dictionary, elements
  If the input is correct the function will execute the commands.
  """
    if len(params_list) == 1:
        if params_list[0] in elements:
            filter_by_type(params_list[0], elements)
        else:
            amount = int(params_list[0])
            filter_by_amount(amount, elements)
    else:
        return False


def find_max_expense_water(elements, history_list, apartament_nr):
    """
  A function that finds the maximum amount for the water expense type in the entire history of transactions.
  :param elements: a dictionary, elements
  :param history_list: a list of dictionaries, representing the history of all transactions that were done.
  :param apartament_nr: an integer, representing the number of the given apartament
  :return: an integer, representing the maximum amount for the water expense type in the entire history of transactions
  """
    water_expenses = []
    for elem in history_list:
        i = get_apartament_index(elem, apartament_nr)
        water_expenses.append(get_ap(elem, "water", i))
    maxi = max(water_expenses)
    return maxi


def filter_by_type(type, elements):
    """
   A function that filters the expenses, keeping only the expenses for the given type.
  :param type: a string, representing the given type
  :param elements: a dictionary elements
  If the input is correct the function will execute the commands.
  """
    for elem in elements:
        if elem != "apartaments" and elem != type:
            for i in range(len(elements[type])):
                set_ap_expenses(elements, elem, i, 0)
