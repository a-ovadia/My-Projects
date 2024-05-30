# Functions that validate input

# case 1: Validate phone number is numeric and has 2 hyphens

def valid_p_number_2_hyphens(p_number):
    p_number_format = str(p_number).split('-')
    for entry in p_number_format:
        if not entry.isnumeric() or not len(p_number_format) == 3 :
            return False

    return True


# case 2: Validate length of phone resulting from case 1
def valid_p_number_length_2_hypens(p_number):
    valid_length = [3, 3, 4]
    p_number_format = str(p_number).split('-')
    for entry in range(3):
        if not valid_length[entry] == len(p_number_format[entry]):
            return False
    return True
 # if both case 1 and 2 are true, we validated number is numeric with 2 hyphens and appropriate size

 # Covert to phone -> if number was entered as a string
# Assume valid phone number in string
def convert_string_to_p_number(p_number_str):
    area_code = p_number_str[:3]
    first_part = p_number_str[3:6]
    last_part = p_number_str[6:10]
    return "{}-{}-{}".format(area_code, first_part, last_part)

def check_valid_p_number_no_hyphens(p_number):
    if not str(p_number).isnumeric(): return False
    if len(p_number) == 11 and p_number[0] == "1":
        return True
    elif len(p_number) == 10:
        return True
    return False

def convert_string_p_name(p_number):
    if valid_p_number_2_hyphens(p_number) and valid_p_number_length_2_hypens(p_number):
        return p_number
    p_format = ""
    if len(p_number) == 11:
        p_number = p_number[1:]
    if len(p_number) == 10:
        p_format += p_number[:3]
        p_format += "-"
        p_format += p_number[3:6]
        p_format += "-"
        p_format += p_number[6:10]
    return p_format

def validate_p_number(p_number):
    phone = p_number
    if check_valid_p_number_no_hyphens(phone):
        phone = convert_string_p_name(p_number)
    return valid_p_number_2_hyphens(phone) and valid_p_number_length_2_hypens(phone)


