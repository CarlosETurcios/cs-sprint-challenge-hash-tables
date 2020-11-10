def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # make a has table
    # loop through the list of number to find the number with negetives in it
    # put those numbers in the dict
    # return results
    negative_number_dict = {}
    found_pairs = []

    for number in a:
        if number < 0:
            negative_number_dict[number] = number
    for number in negative_number_dict:
        if abs(number) in a:
            found_pairs.append(abs(number))

    return found_pairs


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
