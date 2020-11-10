# understanding the problem  -
# maybe iterate over the list of list
# place the number in the dict
# if one list has a number that equals a number in another list
# if a number in one list is in the other list return that number a
# as results


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create a dict
    intersect_dict = {}
    results = []

    # loop through array
    for numberlist in arrays:
        for nums in numberlist:
            if nums not in intersect_dict:
                intersect_dict[nums] = 0
            else:
                intersect_dict[nums] += 1
                # print(intersect_dict)
    for key in intersect_dict:
        # print(intersect_dict)
        if intersect_dict[key] == len(arrays) - 1:
            results.append(key)
            # print(intersect_dict)

    return results

    # without hash table
    # results = arrays[0]
    # output = []

    # # loop through list
    # for array in arrays:
    #     for number in array:
    #         if number in results:
    #             output.append(number)
    #     results = output
    #     output = []

    # check to see if a number exist in between multiple list of intergers
    #
    #


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    # arrays.append([5, 7, 8] + [1, 2, 3])
    # arrays.append([8, 3, 6] + [1, 2, 3])
    # arrays.append([9, 8, 4] + [1, 2, 3])

    print(intersection(arrays))
