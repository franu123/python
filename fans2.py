import time

fm='fan is moving'
fn='fan is not moving'
fd='something went wrong'
def fan(ps,generator,switch):
    msg=""
    if (ps == "yes" or generator=="on") and switch == "on":
        msg=fm
    elif ps == "yes" and switch == "off":
        msg=fn
    elif ps == "no" and switch == "off":
        msg=fn
    elif ps == "no" and switch == "on":
        msg=fn
    else:
        msg=fd

    displaymsg(msg)

def regulator(position):

    match position:
        case 1:
            print("slow speed 1")
            rs=fanrotationspeed(1)
            fanmoment(rs)
        case 2:
            print("medium speed 2")
            rs = fanrotationspeed(2)
            fanmoment(rs)
        case 3:
            print("fast speed")
            rs = fanrotationspeed(3)
            fanmoment(rs)
            fanmoment1(50,rs)
        case 4:
            print("fast speed")
            rs = fanrotationspeed(4)
            fanmoment(rs)
        case 0:
            print("no speed")
            rs=fanrotationspeed(0)
            fanmoment(rs)
        case _:
            print("regulator in working")

def fanrotationspeed(position):
    rotationspeed=""
    match position:
        case 1:
            rotationspeed=20
        case 2:
            rotationspeed=50
        case 3:
            rotationspeed=70
        case 4:
            rotationspeed =100
        case 0:
            rotationspeed=0
        case _:
            print("regulator in working")

    return rotationspeed

def fanmoment(rotationspeed):
    for i in range(rotationspeed):
        print(i)

def fanmoment1(rotationspeed,timer):
    for i in range(rotationspeed):
        time.sleep(timer/200)
        print(i)

def displaymsg(msg):
    print(f"alert : ",msg)

fan("yes","on","off")
regulator(3)
