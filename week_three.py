"""Below, we have provided a list of tuples that consist of student names, final exam scores, and whether or
not they will pass the class. For some students, the tuple does not have a third element because it is unknown
whether or not they will pass. Currently, the for loop does not work.
Add a try/except clause so the code runs without an error - if there is no third element in the tuple,
no changes should be made to the dictionary. """

passing = {'Will pass': 0, 'Will not pass': 0}

for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1

    except Exception as e:
        print("got an error")

"""Below, we have provided code that does not run. Add a try/except clause so the code runs without errors. 
If an element is not able to undergo the addition operation, the string ‘Error’ should be appended to plus_four."""

nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3,
        2, 5, 6, '9', 2, 3, 4, 5, 1]

plus_four = []

for num in nums:
    try:
        plus_four.append(num + 4)
    except Exception as e:
        plus_four.append('Error')
        print('Error with:', num)


"""The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 divided 
by each number in numb. For example, the first element should be 0, because 36/6 has no remainder. 
If there is an error, have the string “Error” appear in the remainder."""

numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
remainder = []

for x in numb:
    try:
        c = 36 % x
        remainder.append(c)
    except:
        remainder.append('Error') #error when try to divide by zero - ZeroDivisionError


"""Provided is buggy code, insert a try/except so that the code passes."""

lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except Exception as e:
        pass

print(lst_three)

"""Write code so that the buggy code provided works using a try/except. 
When the codes does not work in the try, have it append to the list attempt the string “Error”."""

full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
    except:
        attempt.append('Error')


"""The following code tries to append the third element of each list in conts to the new list third_countries. 
Currently, the code does not work. Add a try/except clause so the code runs without errors, 
and the string ‘Continent does not have 3 countries’ is appended to countries instead of producing an error."""


conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'],
         ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], ['Argentina', 'Chile', 'Brazil', 'Ecuador',
                                                              'Uruguay', 'Venezuela'], ['Australia'],
         ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except:
        third_countries.append('Continent does not have 3 countries')


"""The buggy code below prints out the value of the sport in the list sport. 
Use try/except so that the code will run properly. 
If the sport is not in the dictionary, ppl_play, add it in with the value of 1."""


sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except:
        ppl_play[x] = 1


"""Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. 
Insert a try/except so that the code passes. 
If the key is not there, initialize it in the dictionary and set the value to zero."""


di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0

for diction in di:
    try:
        total = total + diction['Puppies']
    except:
        diction['Puppies'] = 0

print("Total number of puppies:", total)


