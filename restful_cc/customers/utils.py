def issuer_check(param):

    issuers = {
        "Visa": [40,41,42,43,44,45,46,47,48,49],
        "MasterCard": [51,52,53,54,55],
        "AmeicanExpress": [34,37],
        "Diners": [36,38],
        "Discover": [65]
    }
    
    if type(param) == str:
        # Equivalent leading 2 digits
        for name, nums in issuers.items():
            if param == name:
                return nums
        
    elif type(param) == int:
        # Card issuer name
        for name, nums in issuers.items():
            if param in nums:
                return name

    return None
            
