STEP_MAXIMUM = 10000


def collatz_algorithm(number: int) -> int:
    if number % 2 == 0:
        return int(number / 2)
    else:
        return (number * 3) + 1


def process_number_list(number: int) -> list:
    step_count = 1
    number_list = list()

    while number > 1 and step_count < STEP_MAXIMUM:
        number = collatz_algorithm(number)
        number_list.append(number)
        step_count += 1

    return number_list
