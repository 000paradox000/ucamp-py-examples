def print_client_data(**client_data):
    """Loop a client record and print the keys and values."""
    pass


#def sum_all(*numbers):
#    """Sum all the elements and return result."""
#    pass


#def sum_all_3(*args):
#    """Sum all the elements and return result."""
#    return x + y + z

#def sum_all(l):
#    """Sum all the elements and return result."""
#    total = 0
#    for i in l:
#        total += i
#    
#    return total

def sum_all(*l):
    """Sum all the elements and return result."""
    total = 0
    for i in l:
        total += i
    
    return total


def main():
    print(sum_all(5, 6, 7))
    #print(sum_all([5, 7]))
    #print(sum_all([5, 7, 5, 6, 7, 8]))


if __name__ == "__main__":
    main()
