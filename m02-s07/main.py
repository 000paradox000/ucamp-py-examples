import sys

def main():
    can_exit = False
    while not can_exit:
        msg = (
            "Soy una AI ¿qué deseas consultar?, " 
            "puedes escribir la palabra salir para "
            "finalizar el programa: "
        )
        query = input(msg)

        if query == "salir":
            print("Chao que descanses")
            sys.exit(0)

        if not query.isnumeric():
            continue

        number1 = int(query)

        msg = (
            "Bueno ya que me diste un número, "
            "digitame otro. Puedes escribir la "
            "palabra salir para finalizar el programa: "
        )
        query = input(msg)

        if query == "salir":
            print("Chao que descanses")
            sys.exit(0)

        if not query.isnumeric():
            print("Chao que descanses")
            sys.exit(0)

        number2 = int(query)

        median = (number1 + number2) / 2
        sum = number1 + number2
        print(f"The median is: {median}")
        print(f"The sum is: {sum}")
        


if __name__ == "__main__":
    main()
