def create_sen_list(*args):
    """
    argument: takes a string
    returns: a list
    """
    li = []
    for i in args:
        if ' ' in i:
            si = i.split()
            for j in si:
                li.append(j)
        else:
            li.append(i)
    return li


def num_list(*args):
    """
    argument: takes an integer
    returns: a list
    """
    for i in args:
        yield int(i)
