''' in python we have data structures which was also called as non-primitable data taypes
which is storing multiple elements it is called the non-primitive data types and we have few data types
like '''

# list
# tuple
# set
# dictionari
# string

# TOPIC - 1 = LIST
'''print('list')

cars_list = ['skoda','BMW','suzuki','honda','minicooper']
name = input('enter name : ')
names_data = [i for i in name]
names_data = ''.join(names_data)
print(names_data)
def cars_owners(cars_list):
    if name =='chandu':
        print(f'your car is {cars_list[2]}')
    elif name  == 'arjun':
        print(f'your car name is {cars_list[1]}')
    elif name == 'kishore':
        print(f'your car is {cars_list[3]}')
    elif name == 'gawtham':
        print(f'your car is {cars_list[0]}')
    else:
        print(f'your car is {cars_list[4]}')

cars_owners(cars_list)'''

'''-----------------------------------------------------------------------------------------'''
# TOPIC - 2 = TUPLE

'''names = ('chandu','sai',)
print(type(names))
print('its a tuple data type ')'''

'''----------------------------------------------------------------------------------------------'''
# TOPIC - 3 = DICTIONARIES

'''details  = {'name':input('name: '),'age':int(input('enter age : ')),'addresss':input('anter address : ')}
print(details)

kishore_balance = 500
arjun_balance = 1000
gawtham_balance = 2000

def bank(details):
    if details['name'] == 'kishore':
        print(f'kishore balance is{kishore_balance}')
        details['status'] = 'active'
    elif details['name'] == 'arjun':
        print(f'arjun balance is {arjun_balance}')
        details['status'] = 'temporarily blocked'
    elif details['name'] == 'gawtham':
        details['name'] = 'chandu'
        print(" name changed from gawtham to",details['name'])
        details['status'] = 'active'
    else:
        print('close')

bank(details)
print(f'updated details are {details}') '''

'''--------------------------------------------------------------------------------------'''
# TOPIC - 4 = SET

'''numbers = {7,5,5,4,5,6,7,6,5,8,6,5,9,8,7,3,2,4,6,9,8,5,6,4,9,8,5,6,3,4,7,8,9,5,6,2,9,8,7,4,6,5,7,8,3,4,6,9,8,2,5,6}
print(numbers)
# output = {2, 3, 4, 5, 6, 7, 8, 9}
#it wont allow duplicate values and its sorted list '''

'''-----------------------------------------------------------------------------------------------------'''
# TOPIC - 5 = STRING

'''name = 'chandu'
a = name.split() # list
a.extend(['arjun','kishore','gawtham'])
name = str(a)
print(type(name),name)'''

'''--------------------------------------------------------------------------------------'''













