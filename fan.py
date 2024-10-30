def fan(command):
    res=powerup("yes")
    if check(res)==True and command=="on":
        print('fan is moving')
    elif check(res)==True and command=="off":
        print('fan is not moving')
    else:
        print('let the power come')

def moter(command):
    if command=="working":
        print("moter is working")
    if command=="not":
        print("please repair the machine")

def powerup(command):
    if command=="yes":
        print('supply is on')
    if command=="no":
        print('supply is off')
    return command

def check(powerup):
    if powerup=="yes":
        return True
    if powerup=="no":
        return False


fan("on")