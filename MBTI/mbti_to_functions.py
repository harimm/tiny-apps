from mbti_utils import *


# Returns a tuple of lists - first list is ego functions, second list is shadow functions
def get_function_stack(mbti_type):
    judging_functions_copy = list(JUDGING_FUNCTIONS)
    perceiving_functions_copy = list(PERCEIVING_FUNCTIONS)
    judging_function = mbti_type[2]
    judging_functions_copy.remove(judging_function)
    perceiving_function = mbti_type[1]
    perceiving_functions_copy.remove(perceiving_function)
    secondary_judging_function = judging_functions_copy[0]
    secondary_perceiving_function = perceiving_functions_copy[0]
    is_extraverted = mbti_type[0] == EXTRAVERTED_FOCUS
    is_judging = mbti_type[3] == JUDGING_TACTICS
    f_1, f_2, f_3, f_4 = None, None, None, None
    if is_judging:
        # Primary Judging function is extraverted
        # Judging, Perceiving, Perceiving, Judging
        f_1 = judging_function
        f_2 = perceiving_function
        f_3 = secondary_perceiving_function
        f_4 = secondary_judging_function
    else:
        # Primary Perceiving     function is extraverted
        # Perceiving, Judging, Judging, Perceiving
        f_1 = perceiving_function
        f_2 = judging_function
        f_3 = secondary_judging_function
        f_4 = secondary_perceiving_function

    # if focus is introverted, then swap functions
    if not is_extraverted:
        f_1, f_2 = f_2, f_1
        f_3, f_4 = f_4, f_3

    functions = [f_1, f_2, f_3, f_4]
    ego_functions = []
    shadow_functions = []

    # Default primary focus is extraverted and secondary focus is intraverted
    # If MBTI type has introverted focus, this is reversed
    primary_focus, secondary_focus = EXTRAVERTED_SUFFIX, INTROVERTED_SUFFIX
    if not is_extraverted:
        primary_focus, secondary_focus = secondary_focus, primary_focus

    # Populate ego and shadow functions
    # Shadow functions have same order as ego functions, but opposite focus
    for i in range(0, 4):
        if i % 2 == 0:
            ego_functions.append(functions[i] + primary_focus)
            shadow_functions.append(functions[i] + secondary_focus)
        else:
            ego_functions.append(functions[i] + secondary_focus)
            shadow_functions.append(functions[i] + primary_focus)

    return ego_functions, shadow_functions


def print_function_stack(mbti_type):
    print mbti_type
    if (validate_mbti_type(mbti_type)):
        function_stack = get_function_stack(mbti_type)
        print_function_stack_details(function_stack)
    else:
        print 'Invalid type entered! ' + mbti_type + ' is not a valid MBTI type.'
    print_section_separator()


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


# main block
print_section_separator()
print_function_stack('INTP')
print_function_stack('INTJ')
print_function_stack('ENTP')
print_function_stack('ENTJ')
print_function_stack('INFP')
print_function_stack('INFJ')
print_function_stack('ENFP')
print_function_stack('ENFJ')
print_function_stack('ISTP')
print_function_stack('ISTJ')
print_function_stack('ESTP')
print_function_stack('ESTJ')
print_function_stack('ISFP')
print_function_stack('ISFJ')
print_function_stack('ESFP')
print_function_stack('ESFJ')
