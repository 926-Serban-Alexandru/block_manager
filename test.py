from functions import *
from copy import deepcopy


def test_add_transaction():
    elem = init_elements()
    add_transaction(["12", "gas", "50"], elem)
    assert elem == {
        "apartaments": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "water": [40, 53, 12, 28, 32, 74, 21, 98, 32, 100, 43, 27, 87, 110, 96],
        "heating": [50, 64, 34, 21, 44, 21, 40, 23, 42, 64, 87, 56, 43, 76, 98],
        "gas": [48, 21, 98, 52, 65, 32, 47, 87, 41, 63, 41, 113, 48, 96, 74],
        "electricity": [41, 23, 89, 65, 41, 23, 55, 19, 41, 54, 79, 21, 63, 150, 41],
        "other": [74, 12, 33, 25, 65, 41, 23, 79, 54, 15, 41, 87, 130, 41, 32]
    }
    add_transaction(["13", "water", "20"], elem)
    assert elem == {
        "apartaments": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "water": [40, 53, 12, 28, 32, 74, 21, 98, 32, 100, 43, 27, 107, 110, 96],
        "heating": [50, 64, 34, 21, 44, 21, 40, 23, 42, 64, 87, 56, 43, 76, 98],
        "gas": [48, 21, 98, 52, 65, 32, 47, 87, 41, 63, 41, 113, 48, 96, 74],
        "electricity": [41, 23, 89, 65, 41, 23, 55, 19, 41, 54, 79, 21, 63, 150, 41],
        "other": [74, 12, 33, 25, 65, 41, 23, 79, 54, 15, 41, 87, 130, 41, 32]
    }
    add_transaction(["4", "electricity", "40"], elem)
    assert elem == {
        "apartaments": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "water": [40, 53, 12, 28, 32, 74, 21, 98, 32, 100, 43, 27, 107, 110, 96],
        "heating": [50, 64, 34, 21, 44, 21, 40, 23, 42, 64, 87, 56, 43, 76, 98],
        "gas": [48, 21, 98, 52, 65, 32, 47, 87, 41, 63, 41, 113, 48, 96, 74],
        "electricity": [41, 23, 89, 105, 41, 23, 55, 19, 41, 54, 79, 21, 63, 150, 41],
        "other": [74, 12, 33, 25, 65, 41, 23, 79, 54, 15, 41, 87, 130, 41, 32]
    }


def test_remove_expenses():
    elem = {"apartaments": [23, 43, 12, 10],
            "water": [40, 53, 12, 5],
            "heating": [50, 64, 34, 6],
            "gas": [48, 21, 98, 100],
            "electricity": [41, 23, 89, 23],
            "other": [74, 12, 33, 90]}

    remove_expenses(["12"], elem)

    assert elem == {"apartaments": [23, 43, 12, 10],
                    "water": [40, 53, 0, 5],
                    "heating": [50, 64, 0, 6],
                    "gas": [48, 21, 0, 100],
                    "electricity": [41, 23, 0, 23],
                    "other": [74, 12, 0, 90]}

    remove_expenses(["electricity"], elem)
    assert elem == {"apartaments": [23, 43, 12, 10],
                    "water": [40, 53, 0, 5],
                    "heating": [50, 64, 0, 6],
                    "gas": [48, 21, 0, 100],
                    "electricity": [0, 0, 0, 0],
                    "other": [74, 12, 0, 90]}


def test_calculate_total_expenses():
    elem = {"apartaments": [23, 43, 12, 10],
            "water": [40, 53, 12, 5],
            "heating": [50, 64, 34, 6],
            "gas": [48, 21, 98, 100],
            "electricity": [41, 23, 89, 23],
            "other": [74, 12, 33, 90]}

    assert calculate_total_expenses_apartament(elem, 23) == 253
    assert calculate_total_expenses_apartament(elem, 43) == 173
    assert calculate_total_expenses_apartament(elem, 12) == 266
    assert calculate_total_expenses_apartament(elem, 10) == 224


def test_split_command_user():
    assert split_command_user('exit') == ('exit', None)
    assert split_command_user('eXiT') == ('exit', None)
    assert split_command_user('add 23 water 34') == ('add', '23 water 34')
    assert split_command_user('  REMOve 5 to   10') == ('remove', '5 to   10')
    assert split_command_user('   ADD    45 Heating 100   ') == ('add', '45 heating 100')
    assert split_command_user('list 14') == ('list', '14')


def test_params_split():
    assert params_split('23 water 3') == ['23', 'water', '3']
    assert params_split('5 to 10') == ['5', 'to', '10']
    assert params_split('45 heating 100') == ['45', 'heating', '100']
    assert params_split('45') == ['45']
    assert params_split('23 to 87') == ['23', 'to', '87']
    assert params_split('> 23') == ['>', '23']


def test_get_apartament_index():
    elements = init_elements()
    assert get_apartament_index(elements, 1) == 0
    assert get_apartament_index(elements, 2) == 1
    assert get_apartament_index(elements, 3) == 2
    assert get_apartament_index(elements, 4) == 3
    assert get_apartament_index(elements, 5) == 4
    assert get_apartament_index(elements, 6) == 5
    assert get_apartament_index(elements, 7) == 6


def test_calculate_total_expenses_type():
    elem = {
        "apartaments": [23, 43, 12, 10],
        "water": [40, 53, 12, 5],
        "heating": [50, 64, 34, 6],
        "gas": [48, 21, 98, 100],
        "electricity": [41, 23, 89, 23],
        "other": [74, 12, 33, 90]
    }
    assert calculate_total_expenses_type("dfosam", elem) is False
    assert calculate_total_expenses_type("water", elem) == 110
    assert calculate_total_expenses_type("heating", elem) == 154
    assert calculate_total_expenses_type("gas", elem) == 267
    assert calculate_total_expenses_type("electricity", elem) == 176
    assert calculate_total_expenses_type("other", elem) == 209


def test_calculate_total_expenses_for_all_apartaments():
    elem = {
        "apartaments": [23, 43, 12, 10],
        "water": [40, 53, 12, 5],
        "heating": [50, 64, 34, 6],
        "gas": [48, 21, 98, 100],
        "electricity": [41, 23, 89, 23],
        "other": [74, 12, 33, 90]
    }
    assert calculate_total_expenses_for_all_apartaments(elem) == [253, 173, 266, 224]


def test_filter():
    elem = {
        "apartaments": [1, 2, 3, 4],
        "water": [40, 53, 12, 5],
        "heating": [50, 64, 34, 6],
        "gas": [48, 21, 98, 100],
        "electricity": [41, 23, 89, 23],
        "other": [74, 12, 33, 90]
    }
    filter(["water"], elem)
    assert elem == {
        "apartaments": [1, 2, 3, 4],
        "water": [40, 53, 12, 5],
        "heating": [0, 0, 0, 0],
        "gas": [0, 0, 0, 0],
        "electricity": [0, 0, 0, 0],
        "other": [0, 0, 0, 0]
    }
    elem = {
        "apartaments": [1, 2, 3, 4],
        "water": [40, 53, 12, 5],
        "heating": [50, 64, 34, 6],
        "gas": [48, 21, 98, 100],
        "electricity": [41, 23, 89, 23],
        "other": [74, 12, 33, 90]
    }
    filter(["50"], elem)
    assert elem == {
        "apartaments": [1, 2, 3, 4],
        "water": [40, 0, 12, 5],
        "heating": [0, 0, 34, 6],
        "gas": [48, 21, 0, 0],
        "electricity": [41, 23, 0, 23],
        "other": [0, 12, 33, 0]
    }


def test_max_expense_for_water():
    elem = {
        "apartaments": [1, 2, 3, 4],
        "water": [40, 53, 12, 5],
        "heating": [50, 64, 34, 6],
        "gas": [48, 21, 98, 100],
        "electricity": [41, 23, 89, 23],
        "other": [74, 12, 33, 90]
    }
    hist = [deepcopy(elem)]
    elem = {
        "apartaments": [1, 2, 3, 4],
        "water": [40, 73, 12, 5],
        "heating": [50, 64, 34, 6],
        "gas": [48, 21, 98, 100],
        "electricity": [41, 23, 89, 23],
        "other": [74, 12, 33, 90]
    }
    hist.append(deepcopy(elem))
    elem = {
        "apartaments": [1, 2, 3, 4],
        "water": [40, 93, 12, 5],
        "heating": [50, 64, 34, 6],
        "gas": [48, 21, 98, 100],
        "electricity": [41, 23, 89, 23],
        "other": [74, 12, 33, 90]
    }
    hist.append(deepcopy(elem))
    elem = {
        "apartaments": [1, 2, 3, 4],
        "water": [40, 43, 12, 5],
        "heating": [50, 64, 34, 6],
        "gas": [48, 21, 98, 100],
        "electricity": [41, 23, 89, 23],
        "other": [74, 12, 33, 90]
    }
    hist.append(deepcopy(elem))
    water = find_max_expense_water(elem, hist, 2)
    assert water == 93


def test_all():
    test_get_apartament_index()
    test_split_command_user()
    test_params_split()
    test_calculate_total_expenses()
    test_add_transaction()
    test_remove_expenses()
    test_calculate_total_expenses()
    test_calculate_total_expenses_for_all_apartaments()
    test_filter()
    test_max_expense_for_water()



