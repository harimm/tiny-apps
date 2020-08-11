EXTRAVERTED_FOCUS = 'E'
INTROVERTED_FOCUS = 'I'
INTUITIVE_PERCEIVING = 'N'
SENSING_PERCEIVING = 'S'
FEELING_JUDGING = 'F'
THINKING_JUDGING = 'T'
JUDGING_TACTICS = 'J'
PERCEIVING_TACTICS = 'P'
EXTRAVERTED_SUFFIX = 'e'
INTROVERTED_SUFFIX = 'i'

FOCUS_SUFFIXES = {EXTRAVERTED_SUFFIX, INTROVERTED_SUFFIX}
FOCUS_SUFFIX_DICT = {EXTRAVERTED_SUFFIX: EXTRAVERTED_FOCUS, INTROVERTED_SUFFIX: INTROVERTED_FOCUS}

FOCUS = {EXTRAVERTED_FOCUS, INTROVERTED_FOCUS}
PERCEIVING_FUNCTIONS = {INTUITIVE_PERCEIVING, SENSING_PERCEIVING}
JUDGING_FUNCTIONS = {FEELING_JUDGING, THINKING_JUDGING}
TACTICS = {JUDGING_TACTICS, PERCEIVING_TACTICS}

FOCUS_NAME_DICT = {EXTRAVERTED_SUFFIX: 'Extraverted', INTROVERTED_SUFFIX: 'Introverted'}
FUNCTION_NAME_DICT = {INTUITIVE_PERCEIVING: 'iNtuiting', SENSING_PERCEIVING: 'Sensing', FEELING_JUDGING: 'Feeling',
                      THINKING_JUDGING: 'Thinking'}

EGO_FUNCTION_ORDER_NAMES = ('Leading', 'Supporting', 'Relief', 'Aspirational')
SHADOW_FUNCTION_ORDER_NAMES = ('Opposing', 'Critical Parent', 'Deceiving', 'Devilish')


# Check if function is a valid cognitive function Ne, Ni, Se, Si, Fe, Fi, Te, Ti
def validate_function(function_str):
    if type(function_str) != str or len(function_str) != 2:
        return False
    if function_str[1] in FOCUS_SUFFIXES and (
            function_str[0] in PERCEIVING_FUNCTIONS or function_str[0] in JUDGING_FUNCTIONS):
        return True
    return False


# Check if value is valid MBTI type
# Length should be equal to 4 and each letter should be valid
def validate_mbti_type(mbti_type):
    if (len(mbti_type) != 4):
        return False
    if (mbti_type[0] not in FOCUS):
        return False
    if (mbti_type[1] not in PERCEIVING_FUNCTIONS):
        return False
    if (mbti_type[2] not in JUDGING_FUNCTIONS):
        return False
    if (mbti_type[3] not in TACTICS):
        return False
    return True


# One function should be Perceiving and the other Judging
def validate_function_types(function_1, function_2):
    if function_1[0] in PERCEIVING_FUNCTIONS and function_2[0] in JUDGING_FUNCTIONS:
        return True
    if function_1[0] in JUDGING_FUNCTIONS and function_2[0] in PERCEIVING_FUNCTIONS:
        return True
    return False


def invert_focus(focus):
    if focus == EXTRAVERTED_SUFFIX:
        return INTROVERTED_SUFFIX
    if focus == INTROVERTED_SUFFIX:
        return EXTRAVERTED_SUFFIX
    return None


# Find opposite function under same tactics
def find_opposite_function(function_symbol):
    if function_symbol == THINKING_JUDGING:
        return FEELING_JUDGING
    if function_symbol == FEELING_JUDGING:
        return THINKING_JUDGING
    if function_symbol == INTUITIVE_PERCEIVING:
        return SENSING_PERCEIVING
    if function_symbol == SENSING_PERCEIVING:
        return INTUITIVE_PERCEIVING
    return None


# Find mirror position ego/shadow
def find_mirror_position(position):
    return (position + 4) % 8


# Find position of opposite function
def find_opposite_position(position):
    mod_value = position % 4
    if mod_value == 0:
        return position + 3
    if mod_value == 1:
        return position + 1
    if mod_value == 2:
        return position - 1
    if mod_value == 3:
        return position - 3


def get_function_order_name(position):
    if position in range(0, 4):
        return EGO_FUNCTION_ORDER_NAMES[position]
    if position in range(4, 8):
        return SHADOW_FUNCTION_ORDER_NAMES[position - 4]
    return None
