def constraint_check(keys, values):
    constraints = {
        'PlaneID':              '',
        'DepartureAirportID':   '',
        'ArrivalAirportID':     '',
        'FlightTime':           '',
        'Duration':             '',
        'BaseTicketPrice':      'BaseTicketPrice > 0'
    }
    vals = dict(zip(keys, values))
    for k, v in constraints.items():
        if vals[k] is None or (v and not eval(v.replace(k, str(vals[k])))):
            return False
    return True
