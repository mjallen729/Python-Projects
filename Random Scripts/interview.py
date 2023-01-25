min_length = 6
max_length = 10

while True:
    print('Enter password: ', end='')
    password = input()
    passlen = len(password)

    if min_length > passlen or max_length < passlen:
        print('Password must be between 6-10 characters!')
        continue

    if password.isalpha() or password.isnumeric():
        print('Password must contain both letters and numbers!')
        continue

    print('Password strong! (' + str(passlen) + ' characters)')
    break

