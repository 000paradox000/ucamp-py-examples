#def print_client_data(**client_data):
#    """Loop a client record and print the keys and values."""
#    pass

#def print_client_data(name, address, email):
#    """Loop a client record and print the keys and values."""
#    print("Name:", name)
#    print("Address:", address)
#    print("Email:", address)

def print_client_data(**kwargs):
    """Loop a client record and print the keys and values."""
    for k, v in kwargs.items():
        print(f"{k}: {v}")


def main():
    print_client_data(name="UCAMP", address="ucamp.io", email="info@ucamp.io")
    print_client_data(name="UCAMP", email="info@ucamp.io", center="12345")

    data = {
        "Name": "UCAMP", 
        "Email": "info@ucamp.io", 
        "Center": "12345"
    }
    print_client_data(**data)


if __name__ == "__main__":
    main()
