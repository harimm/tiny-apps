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
