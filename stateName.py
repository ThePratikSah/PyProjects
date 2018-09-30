while True:
    state = 'Bihar'
    if state == 'Bihar':
        print('The capital of {} is Patna.'.format(state))
    else:
        print('Invalid choice!')
    opt = input('Do you want to continue(y/n): ')
    if opt == 'n':
        break
