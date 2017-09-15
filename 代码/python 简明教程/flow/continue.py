while True:
    s = input('enter sth: ')
    if s == 'quit': 
        break
    if len(s) < 3:
        print('too small')
        continue
    print('Input is of sufficient length')
