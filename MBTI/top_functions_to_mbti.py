from mbti_utils import *
from print_utils import print_line_separator


def validate_functions(dominant_function, secondary_function):
    if not (validate_function(dominant_function) and validate_function(
            secondary_function)):
        return False
    # One of the functions should be extroverted and the other introverted
    has_both_focus = dominant_function[1] in FOCUS_SUFFIXES and secondary_function[1] in FOCUS_SUFFIXES and \
                     dominant_function[1] != secondary_function[1]
    # Should have one perceiving function and one judging function
    has_perceiving_function = dominant_function[0] in PERCEIVING_FUNCTIONS or secondary_function[
        0] in PERCEIVING_FUNCTIONS
    has_judging_function = dominant_function[0] in JUDGING_FUNCTIONS or secondary_function[0] in JUDGING_FUNCTIONS
    return has_both_focus and has_judging_function and has_perceiving_function


def get_mbti_type(dominant_function, secondary_function):
    if validate_functions(dominant_function, secondary_function):
        # Focus of dominant function determines if MBTI type's focus
        focus = FOCUS_SUFFIX_DICT[dominant_function[1]]
        extraverted_function, introverted_function = None, None
        isExtraverted = focus == EXTRAVERTED_FOCUS
        if isExtraverted:
            # Dominant function is extraverted and Secondary function is intraverted
            extraverted_function = dominant_function[0]
            introverted_function = secondary_function[0]
        else:
            # Dominant function is introverted and Secondary function is extraverted
            extraverted_function = secondary_function[0]
            introverted_function = dominant_function[0]
        perceiving_function, judging_function, tactics = None, None, None
        if extraverted_function in JUDGING_FUNCTIONS:
            # For Judging types, the judging function is extraverted and perceiving function is introverted
            judging_function = extraverted_function
            perceiving_function = introverted_function
            tactics = 'J'
        else:
            # For Perceiving types, the perceiving types is extraverted and judging function is introverted
            perceiving_function = extraverted_function
            judging_function = introverted_function
            tactics = 'P'
        return focus + perceiving_function + judging_function + tactics
    else:
        return None


def print_mbti_type(dominant_function, secondary_function):
    print 'Dominant Function: ' + dominant_function
    print 'Secondary Function: ' + secondary_function
    mbti_type = get_mbti_type(dominant_function, secondary_function)
    if mbti_type == None:
        print dominant_function + ' and ' + secondary_function + ' is not part of a valid cognitive function stack.'
    else:
        print 'MBTI Type: ' + mbti_type
    print_line_separator()
