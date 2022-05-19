'''operators in python
        Arithamatic operators'''
import time

'''+ operator
current_balance = 200
amount_to_be_enter  = int(input('enter the amount: '))
print('amount rupees ',amount_to_be_enter,'deposited succesfully')

def deposite(amount_to_be_enter,current_balance):
    print('your old balance is  ',current_balance)
    current_balance = current_balance + amount_to_be_enter
    return 'your new updated balance is now ',current_balance
d = deposite(amount_to_be_enter,current_balance)
print(d)'''


'''---------------------------------------------------------------------------------------------------------'''

# - operator
'''current_balance = 500
thumb = input('please put your thumb here : ')
print('please wait we are reading your finger print ')
time.sleep(3)
withdraw_amount = int(input('enter the amount to withdraw  : '))
time.sleep(2)
print(f'amount rupees {withdraw_amount} witdrawn succesfully ')
time.sleep(1)
print(f'your current balance is {current_balance}')

def with_draw_amount(current_balance,withdraw_amount):
    current_balance = current_balance - withdraw_amount
    time.sleep(1)
    print(f'your updated balance is now {current_balance}')

    print('thanku')

with_draw_amount(current_balance,withdraw_amount)'''

'''-------------------------------------------------------------------------------------------------------'''

# * multiplication operator
# creating a table

'''number = int(input('enter the table number : '))
count = int(input('enter the table end number : '))

for i in range(1,count+1):
    print(number,'*',i,'=',number*i)
    count = count + 1'''

'''-----------------------------------------------------------------------------------------'''

# % operator
# modulas operator

'''mobiles = int(input('enter the mobile phones count : '))
persons = int(input('how many members are there: '))

def distributing(mobiles,persons):
    distribute = mobiles % persons * 100
    return 'for each person they get ',distribute,'mobiles'
d = distributing(mobiles,persons)
print(d)'''


'''-----------------------------------------------------------------------------------------'''

# / divided by operator
'''maths_marks = int(input('enter the maths marks : '))
social_marks = int(input('enter the social marks: '))
sanskrit_marks = int(input('ente the sanskrit marks : '))
total_marks = 300

def finding_percentage(maths_marks,social_marks,sanskrit_marks):
    results = maths_marks + social_marks + sanskrit_marks / 300
    return 'you got ',results,'in all this sem '
f = finding_percentage(maths_marks,social_marks,sanskrit_marks)
print(f)'''

'''------------------------------------------------------------------------------------------'''
# // operator
# will get ground value with out decimal values

'''maths_marks = int(input('enter the maths marks : '))
social_marks = int(input('enter the social marks: '))
sanskrit_marks = int(input('ente the sanskrit marks : '))
total_marks = 300

def finding_percentage(maths_marks,social_marks,sanskrit_marks):
    results = maths_marks + social_marks + sanskrit_marks // 300
    return 'you got ',results,'in all this sem '
f = finding_percentage(maths_marks,social_marks,sanskrit_marks)
print(f)'''

'''-------------------------------------------------------------------------------------------------'''
# ** power operator
# will get like 2 square or 3 square like this

'''number = int(input('enter the number : '))

def power_operator(number):
    for i in range(1,number+1):
        print(i,'power of',i,'=',i**2)

power_operator(number)'''

'''------------------------------------------------------------------------------------------------'''

''' this are called the arithamatical operator '''





