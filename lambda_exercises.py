''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
from tkinter.tix import CheckList


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenfiltered_list = list(filter(lambda num: (num % 2 == 0),list1))
print(evenfiltered_list)

oddfiltered_list = list(filter(lambda num: (num % 2 == 1),list1))
print(oddfiltered_list)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = list(filter(lambda x: (len(x) == 6), weekdays))
print(days)


''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
wordlist = ['orange', 'red', 'green', 'blue', 'white', 'black']

words = list(filter(lambda x: x != 'orange' and x != 'black',wordlist))
print(words)


''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 =  [2, 4, 6, 8]

clear_list = list(filter(lambda x: (x not in list2), list1))
print(clear_list)

''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:

['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

list5 = ['red', 'black', 'white', 'green', 'orange']

sub = 'ack'

strings = list(filter(lambda x: sub in x,list5))
print(strings)

sub2 = 'abc'
strings2 = list(filter(lambda x: sub2 in x,list5))

print(strings2)





''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

example = input('Enter a Password: ')

rules = [lambda x: any(x.isupper() for x in example),
        lambda x: any(x.islower() for x in example),
        lambda x: any(x.isdigit() for x in example),
        lambda x: len(example) >= 8]
if all(rule(example) for rule in rules):
    print("Valid Password")
else:
    print("Invalid Password")

''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

filterlist = sorted(original_scores,key=lambda x: x[1])
print(filterlist)