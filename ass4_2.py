def computepay(hours, rate):
    try:
        if hours > 0 and rate > 0:
            if hours <= 40:
                salary = float(hours * rate)
                print("Pay : ", salary)
            else:
                xhours = hours - 40
                salary = (xhours * 1.5 * rate) + (40 * rate)
                print("Pay : ", salary)
        else:  
            print('Error, please enter numeric input')
    except:
        print('Error, please enter numeric input')
try:
    hours = int(input("Enter hours : "))
    rate = int(input("Enter rate: "))
    work = computepay(hours, rate)
except:
    print('Error, please enter numeric input')
