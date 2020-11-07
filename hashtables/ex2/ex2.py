#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # understanding the problem
    # hash the tickets
    #
# the hahs dict

    hash = {}
    route = []

# gotta loop throught the tickets to set from source to destination
    for ticket in tickets:
        hash[ticket.source] = ticket.destination


#  source string represents the starting and the destination represenst the destination
# first flight source == None
    destination = hash["NONE"]
    while destination != "NONE":
        route.append(destination)
        destination = hash[destination]
    route.append("NONE")

    return route
