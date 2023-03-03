def get_numbers(quantity):
    numbers = []
    for i in range(quantity):
        numbers.append(input(f"Type the number {i+1}: "))


def calculate_circle_area(r):
    return 3.14 * r * r


def calculate_circle_area_procedure(r):
    print(3.14 * r * r)


def calculate_square_area(s):
    return s * s


def calculate_area(values, calculator):
    return calculator(values)


def get_calculator_function():
    return calculate_circle_area


def main():
    # a function saves time when having repetitive tasks
    # numbers = get_numbers(3)

    # a function returns a value
    #value = calculate_circle_area(12)
    #print(value)

    # a procedure doesn't return any value but in python always returns None
    #value = calculate_circle_area_procedure(12)
    #print(value)

    # All items can be the actual parameters of functions
    print(calculate_area(10, calculate_square_area))

    # All items can be returned as results of functions
    f = get_calculator_function()
    print(f(5))

    # All items can be the subject of assignment statements
    g = get_calculator_function()
    print(g)

    # All items can be tested for equality.[5]
    h = get_calculator_function()
    i = get_calculator_function()
    print(h == i)



if __name__ == "__main__":
    main()
