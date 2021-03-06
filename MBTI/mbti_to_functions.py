from print_utils import *


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


def print_function_stackf_for_mbti(mbti_type):
    print mbti_type
    if (validate_mbti_type(mbti_type)):
        function_stack = get_function_stack(mbti_type)
        print_function_stack_details(function_stack)
    else:
        print 'Invalid type entered! ' + mbti_type + ' is not a valid MBTI type.'
    print_section_separator()


# main block
