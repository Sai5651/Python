# list comprehesions

''' List comprehesions is a concise way to create a new list from the existing list  '''

print('list comprehensions ')

# 1 even numbers by using functions

def even_numbers_printing():
    a = [i for i in range(1,51) if i%2==0]
    return a
even = even_numbers_printing()
#print(even)

'''-----------------------------------------------------------------------------------------'''

# 2 odd numbers by using functions

def odd_number_printing():
    x = [j for j in range(50) if j%2!=0]
    return x
odd = odd_number_printing()
#print(odd)

'''----------------------------------------------------------------------------------------'''

# 3 getting the required elements from the old_list

old_list = ['apple','mango','banana','jackfruti','papaya']
def Required_elements(old_list):
    # need only banana jackfruit
    new_list = [old_list[2:4]]
    return new_list
required = Required_elements(old_list)
#print(required)

'''----------------------------------------------------------------------------------------'''

# 4 seperating the data types in the list by using functions

old_list = ['chandu','sai',123,47677,6,78,84,57,6767,6,7,567,4,7,56,7,46,45.46,56356.6378,47.567655,5667855.878,58456.454756,4.6,4766576345.457,True,False]

def Seperating_the_elements(old_list):
    strings = [i for i in old_list if type(i) == str]
    ints = [i for i in old_list if type(i) == int]
    floats = [i for i in old_list if type(i) == float]
    print(f'stings in the list are {strings}')
    print(f'integer in the list are {ints}')
    print(f'floats in the list are {floats}')
#Seperating_the_elements(old_list)
'''--------------------------------------------------------------------------------------------'''

# 5 Count the number of spaces in a string by using the functions
name = 'sandeep kumar reddy'

def finding_the_spaces(name):
    count = 0
    for i in name:
        if i=='':
            count = count + 1
    print(count)
#finding_the_spaces(name)

'''----------------------------------------------------------------------------------'''
# 6 Create a list of all the consonants in the string

data = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'

def finding_consonents(data):
    consonents = [i for i in data if i not in 'a,e,i,o,u']
    print(consonents)
#finding_consonents(data)

'''----------------------------------------------------------------------------------'''

# 7 Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
# Result would look like (index, value), (index, value)

story = ['hi',4,8.99,'apple',('t,b','n')]

def story_func(story):
    index_and_values = [i for i in range(len(story))]
    for i in index_and_values:
        print(i,story[i])
# story_func(story)

'''----------------------------------------------------------------------------------'''
# 8 Find all of the words in a string that are less than 4 letters

problem = 'abcd efghij kl m nopqrst u vwxy z'

def finding(problem):
    spliting_the_stirng = problem.split()
    seperate_list = [i for i in spliting_the_stirng if len(i)<=4]
    print(seperate_list)
#finding(problem)
'''-----------------------------------------------------------------------------'''





