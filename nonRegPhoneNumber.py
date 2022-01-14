def isPhoneNumber(text):
    if len(text) != 12:
        return False # Not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash 
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # missing digits
    if text[7] != '-':
        return False # missing dash 
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing digits        
    
    return True
    

print(isPhoneNumber('111-222-3456'))