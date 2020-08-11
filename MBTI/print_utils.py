from mbti_utils import *


def print_function_stack_details(function_stack):
    if type(function_stack) != tuple or len(function_stack) != 2:
        print 'Function stack invalid!'
        return
    ego_functions = function_stack[0]
    if type(ego_functions) != list or len(ego_functions) != 4:
        print 'Ego function stack invalid!'
        return
    shadow_functions = function_stack[1]
    if type(shadow_functions) != list or len(shadow_functions) != 4:
        print 'Shadow function stack invalid!'
        return
    print_line_separator()
    print 'EGO FUNCTIONS'
    print_line_separator()
    for i in range(0, 4):
        print EGO_FUNCTION_ORDER_NAMES[i] + ': ' + get_function_detail(ego_functions[i])
    print_line_separator()
    print 'SHADOW FUNCTIONS'
    print_line_separator()
    for i in range(0, 4):
        print SHADOW_FUNCTION_ORDER_NAMES[i] + ': ' + get_function_detail(shadow_functions[i])


def get_function_detail(function_abbr):
    if type(function_abbr) != str or len(function_abbr) != 2:
        print function_abbr + ' is not a valid function!'
        return None
    function_name = FUNCTION_NAME_DICT[function_abbr[0]]
    focus = FOCUS_NAME_DICT[function_abbr[1]]
    if function_name is None or focus is None:
        print function_abbr + ' is not a valid function!'
        return None
    return focus + ' ' + function_name


def print_section_separator():
    print '============================================================'


def print_line_separator():
    print '------------------------------------------------------------'
