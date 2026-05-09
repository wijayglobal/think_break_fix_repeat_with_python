# palning
# - - - - - -
# available function
# * Addition
# * Substraction
# * Multipilicatiom
# * Division
# * Power
#
# + check  input validation
# + check input oparands validation
# + output int or float

import sys


def addition(num_a: float, num_b: float) -> float:
    return num_a + num_b


def substraction(num_a: float, num_b: float) -> float:
    return num_a - num_b


def multipilication(num_a: float, num_b: float) -> float:
    return num_a * num_b


def division(num_a: float, num_b: float) -> float:
    return num_a / num_b


def power(num_a: float, num_b: float) -> float:
    return num_a**num_b


AVAILABLE_OPERATION = {
    "1": addition,
    "2": substraction,
    "3": multipilication,
    "4": division,
    "5": power,
}


def greeting():
    print(
        f" {'#' * 60} \n {'    Welcome to two number calculator!    ':#^60} \n {f'#' * 60} \n\n {' Available Options ':-^59}\n"
    )

    for key, value in AVAILABLE_OPERATION.items():
        print(f"        {key}. {value.__name__.capitalize()}")
    print("        Enter Any key to exit...")


def get_operator():
    user_option = input("Enter your option : ")
    if user_option not in AVAILABLE_OPERATION:
        return False
    return user_option


def get_oparands() -> tuple:
    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")
    return num_1, num_2


def validate_oparands(operator: str, num_1: str, num_2: str) -> bool:
    if num_1.isnumeric() and num_2.isnumeric():
        if operator == "4" and num_2 == "0":
            raise ZeroDivisionError("Can't divide by zero. please check your inputs")
        return True
    raise ValueError("please check your inputs")


def close_calculator():
    print(f"{' Bye bye. see you soon!!! ':#^60} \n")
    sys.exit()


def do_calculation(operator: str, num_1: str, num_2: str) -> float:
    func = AVAILABLE_OPERATION.get(operator)
    result = func(float(num_1), float(num_2))
    return result


def display_result(result: float):
    if float(result) - int(result) == 0:
        print(f"result : {result:.0f}")
    else:
        print(f"result : {result} \n")


def calculator():
    greeting()
    operator = get_operator()
    if not operator:
        close_calculator()

    num_a, num_b = get_oparands()
    try:
        validate_oparands(operator, num_a, num_b)
    except Exception as e:
        print("Some error found -> ", e)
    else:
        result = do_calculation(operator, num_a, num_b)
        display_result(result)


if __name__ == "__main__":
    while True:
        calculator()
