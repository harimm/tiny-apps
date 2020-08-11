from mbti_utils import *
from print_utils import print_function_stack_details, print_section_separator

TACTICS_GROUP_1 = (0, 3, 4, 7)
TACTICS_GROUP_2 = (1, 2, 5, 6)
FOCUS_GROUP_1 = {0, 2, 5, 7}
FOCUS_GROUP_2 = {1, 3, 4, 6}
FOCUS_GROUPS = {1: FOCUS_GROUP_1, 2: FOCUS_GROUP_2}


def create_empty_function_stack():
    function_stack = []
    for i in range(0, 8):
        function_stack.append({'focus': None, 'function': None})
    return function_stack


def populate_function_stack(function_1, function_2, position_1, position_2):
    if validate_combination(function_1, function_2, position_1, position_2):
        function_stack = create_empty_function_stack()
        populate_all_functions(function_stack, function_1, position_1, function_2, position_2)
        return function_stack
    else:
        return None


def validate_positions(position_1, position_2):
    if position_1 not in range(0, 8) or position_2 not in range(0, 8):
        return False
    # One position each from both tactics group is necessary for identifying all functions
    if (position_1 in TACTICS_GROUP_1 and position_2 in TACTICS_GROUP_2) or (
            position_1 in TACTICS_GROUP_2 and position_2 in TACTICS_GROUP_1):
        return True
    return False


def validate_combination(function_1, function_2, position_1, position_2):
    if not validate_positions(position_1, position_2):
        return False
    if not validate_function(function_1) and validate_function(function_2):
        return False
    if not validate_function_types(function_1, function_2):
        return False
    if not validate_focus(function_1, function_2, position_1, position_2):
        return False
    return True


def validate_focus(function_1, function_2, position_1, position_2):
    focus_1, focus_2 = function_1[1], function_2[1]
    focus_group_1, focus_group_2 = find_focus_group(position_1), find_focus_group(position_2)
    if focus_1 == focus_2:
        if focus_group_1 == focus_group_2:
            return True
    else:
        if focus_group_1 != focus_group_2:
            return True
    return False


def find_focus_group(position):
    if position in FOCUS_GROUP_1:
        return 1
    if position in FOCUS_GROUP_2:
        return 2
    return None


def find_inverted_focus_group(focus_group_id):
    if focus_group_id == 1:
        return 2
    if focus_group_id == 2:
        return 1
    return None


def populate_all_functions(function_stack, function_1_abbr, position_1, function_2_abbr, position_2):
    focus = function_1_abbr[1]
    focus_group_id = find_focus_group(position_1)
    # Populate all values of intraversion/extraversion focus
    populate_focus(function_stack, focus_group_id, focus)

    function_1_symbol = function_1_abbr[0]
    populate_related_functions(function_stack, function_1_symbol, position_1)
    function_2_symbol = function_2_abbr[0]
    populate_related_functions(function_stack, function_2_symbol, position_2)


def populate_focus(function_stack, focus_group_id, focus):
    inverted_focus = invert_focus(focus)

    focus_group = FOCUS_GROUPS[focus_group_id]
    inverted_focus_group = FOCUS_GROUPS[find_inverted_focus_group(focus_group_id)]

    for focus_position in focus_group:
        function_stack[focus_position]['focus'] = focus
    for focus_position in inverted_focus_group:
        function_stack[focus_position]['focus'] = inverted_focus


def populate_related_functions(function_stack, function_symbol, position):
    # Given function
    function_stack[position]['function'] = function_symbol
    # Ego/Shadow mirror function having inverted focus
    function_stack[find_mirror_position(position)]['function'] = function_symbol
    opposite_function = find_opposite_function(function_symbol)
    opposite_position = find_opposite_position(position)
    # Other function in same tactics group (judging/perceiving)
    function_stack[opposite_position]['function'] = opposite_function
    # Mirror of other function
    function_stack[find_mirror_position(opposite_position)]['function'] = opposite_function


def convert_function_dict(function_stack):
    converted_stack = []
    for function_dict in function_stack:
        converted_stack.append(function_dict['function'] + function_dict['focus'])
    return converted_stack


def print_function_stack(function_1, function_2, position_1, position_2):
    print_section_separator()
    print get_function_order_name(position_1) + ' ' + function_1 + ', ' + get_function_order_name(
        position_2) + ' ' + function_2
    function_stack = populate_function_stack(function_1, function_2, position_1, position_2)
    if function_stack == None:
        print 'Invalid function combination'
    else:
        function_stack = convert_function_dict(function_stack)
        print_function_stack_details((function_stack[0:4], function_stack[4:8]))
    print_section_separator()
