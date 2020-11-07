# understanding the problem  -
# maybe iterate over the list of list
# place the number in the dict
# if one list has a number that equals a number in another list
# if a number in one list is in the other list return that number a
# as results

dict = {}


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
