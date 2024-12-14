def constraint_check(keys, values):
    constraints = {
        'AirportName':  '',
        'City':         ''
    }
    vals = dict(zip(keys, values))
    for k, v in constraints.items():
        if vals[k] is None:
            return False
    return True
