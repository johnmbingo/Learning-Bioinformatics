values_given_integers = "1 2 3 4"

string_of_letters = ""

key_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def string_of_integers_into_list_of_integers(specified_string):
    list_of_integers = [int(num) for num in specified_string.split()]
    return list_of_integers 

#learning point, use int to conver strings to integers, split to add commas between numbers, list comprehension with a four loop
#1st turning strings into integers, 2nd creating a dictionary with the zip function

list_of_integers = string_of_integers_into_list_of_integers(values_given_integers)
splice_positions = dict(zip(key_alphabet,list_of_integers))

for key in list(splice_positions.keys()):
    if key >= 'B':
        splice_positions[key] += 1

print(splice_positions)