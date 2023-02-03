# def main():
#     counter = 5
#
#     while counter >= 0:
#         print("Counter:", counter)
#         # counter = counter - 1
#         counter -= 1  # shortcut, sugar syntax
#
#     print("Hello World!")


def main():
    user_id = ""

    while not user_id.isnumeric():
        user_id = input("Type your user id: ")

    print("The user has id:", user_id)


if __name__ == "__main__":
    main()
