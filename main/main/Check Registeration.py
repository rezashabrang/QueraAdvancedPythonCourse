def check_registration_rules(**kwargs):
    import re
    import copy
    ans = copy.deepcopy(kwargs)
    for user, passw in kwargs.items():
        situation = re.search('[^\d]', passw)
        situation2 = re.search('[\s]',passw)
        situation3 = re.search('[\s]', user)
        if user == 'quera' or user == 'codecup' or len(user) < 4 or len(passw) < 6 or not situation or situation2 or situation3:
            del ans[user]
    return list(ans)


print(check_registration_rules(ussdssdq123123e='1313213', codecusp='Hesfsdfsa', qua='kLS45@l$'))
