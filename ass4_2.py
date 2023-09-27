def computepay(hours, rate):
    try:
        if 0 < (hours, rate) <= 40:
            salary = float(hours * rate)
            print("Pay : ", salary)
        elif (hours, rate) > 40 :
            xhours = hours - 40
            salary = (xhours * 1.5 * rate) + (40 * rate)
            print("Pay : ", salary)
        elif (hours or rate) < 0:
            print('Error, please enter numeric input')   
    except:
        print('Error, please enter numeric input')
try:
    hours = int(input("Enter hours : "))
    rate = int(input("Enter rate: "))
    work = computepay(hours, rate)
    print(work)
except:
    print('Error, please enter numeric input')
