# This should maybe be in the root.


def dates_in_order(lst, key):
    # Check to make sure that all dates are in order.
    # It's pretty unlikely this wouldn't be the case for the
    # kinds of results we're processing.
    l2 = zip(lst, lst[1:])
    for lt, gt in l2:
        if lt[key] > gt[key]:
            return False
    return True


def compare_dicts(d, e, keys=None):
    # Compare only certain keys in a dict to 
    # Make sure they're the same.

    if keys is None:
        return d == e
    else:
        for key in keys:
            if key not in d:
                return False
            if key not in e:
                return False
            if d[key] != e[key]:
                return False
        return True
            

def compare_lists(l, m, keys=None):
    for d, e in zip(l,m):
        if not compare_dicts(d, e, keys):
            return False
    return True

