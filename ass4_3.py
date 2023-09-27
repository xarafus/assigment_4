def num_divide3(num):
    try:
        num = int(num)
        if num < 0:
            print('please enter a positive number')
        else:
            cnt = 0
            for i in range(1,num +1):
                if i % 3 == 0:
                    cnt += 1
        print('numbers divisible by 3 among numbers from 1 to ', num, ': ', cnt)                   
    except:
        print('please enter a positive number')
while True:
    x = input('Enter a positive integer : ')
    if x == 'done':
        break
    else:
        num_divide3(x)
