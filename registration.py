from messages import *

name = input(MSG_INPUT_NAME)
name = name.strip()
is_contains_only_lettres = name.isalpha()

if is_contains_only_lettres:
    name = name.title()
    print(MSG_NAME_OK.format(name=name))

age = input(MSG_INPUT_AGE)
age = age.strip()
age = age.lstrip('0')
has_only_digits = age.isdigit()

if has_only_digits:
    print(MSG_AGE_OK.format(age=age))

phone = input(MSG_INPUT_PHONE)
phone = phone.strip()
has_only_digits_phone = phone.isdigit()

if has_only_digits_phone:
    print(MSG_PHONE_OK.format(phone=phone))

print(MSG_FINISH)