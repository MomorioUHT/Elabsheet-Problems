IP = str(input()).split(".")

def isValidIpAddress(context: list):
    if len(context) != 4 : return "No"
    for i in context:
        if (not i.isdigit()): return "No"
        if len(i) == 0 or int(i) > 255 or int(i) < 0: return "No"
    return "Yes"

print(isValidIpAddress(IP))