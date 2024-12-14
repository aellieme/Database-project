def constraint_check(keys, values):
    constraints = {
        'AirlineName':  '',
        'IATACode':     'IATACode in (2, 3)'
    }
    vals = dict(zip(keys, values))
    for k, v in constraints.items():
        if vals[k] is None or (v and not eval(v.replace(k, str(vals[k])))):
            return False
    return True
