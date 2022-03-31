def inputs():
    Name = input('Enter your name :')
    Surname = input('Enter your surname :')
    Mob_No = input('Enter the mobile number :')
    if len(Mob_No) == 10:
        Birth_Date = input('Enter your birth date in dd-mm-yyyy format:')
        Age = float(input('Enter your age with months after decimal point :'))
        #Convert the input such that it can accept float value
        print('Form is submitted')
    else:
        print('Not a valid number. Please enter a valid number')
        (inputs())
    print('''
    The details of the person are :
    ''', '''
    The name is :	''', Name, '''
    The surname is :	''', Surname, '''
    The mobile number is :	''', Mob_No, '''
    The birth date is :	''', Birth_Date, '''
    The age is :	''', int(Age))

inputs()