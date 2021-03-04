def list_digits(number):
    digits = []
    number = str(number)
    for digit in number:
        digits.append(int(digit))
    return digits


def digit_of_life(digits):
    total = 0
    for number in digits:
        total += number
    if total > 9:
        result = list_digits(total)
        total = digit_of_life(result)
    return total


date = input("Type Date birthday in format YYYYMMDD: ")
list_number = list_digits(date)
digit = digit_of_life(list_number)
print(digit)

"""Versión con la función sum"""


def list_digits_two(number):
    digits = []
    result = 0
    for digit in number:
        digits.append(int(digit))
    if sum(digits) > 9:
        result = str(sum(digits))
        result = list_digits_two(result)
    else:
        result = sum(digits)
    return result


date = input("Type Date birthday in format YYYYMMDD: ")
list_number = list_digits_two(date)
print(list_number)


