# Only IF
# def main():
#     condition = True
#
#     if condition:
#         print("The condition is True")
#
#     print("Hello World!")


# IF - ELSE
# def main():
#     condition = False
#
#     if condition:
#         print("The condition is True")
#     else:
#         print("The condition is False")
#
#     print("Hello World!")


# IF - ELIF - ELSE
def main():
    records_count = 5

    if records_count > 5:
        print("Records count are > 5")

        if records_count <= 25:  # nested conditional
            print("Records count are <= 22")
    else:
        print("Records count are > 22 and <= 5")

    print("Hello World!")


if __name__ == "__main__":
    main()
