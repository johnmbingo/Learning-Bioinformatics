values_given_integers = "11 17 95 100"

string_of_letters = "7Exo0wQ3pVrCalotestH1L4CeIW7BcrEdA8tH17lFrLV41DhBPr6yuKpb1ScazmwDzmcNQ8BR4VL0pu4X32YAOtGxuaOLYKedulisDontm29HDTfiGNykUNFqVmpxoWuSZa8mPqbM4a8X6WCEPzs5W8G8xVxVaYbQJekHkhUy1gr97os8VLqx."

key_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def string_of_integers_into_list_of_integers(specified_string):
    list_of_integers = [int(num) for num in specified_string.split()]
    return list_of_integers 

list_of_integers = string_of_integers_into_list_of_integers(values_given_integers)
splice_positions = dict(zip(key_alphabet,list_of_integers))

for i, key in enumerate(splice_positions):
    if i % 2 == 1:
        splice_positions[key] += 1 

spliced_string_of_letters_A_to_B = string_of_letters[splice_positions['A']:splice_positions['B']]
spliced_string_of_letters_C_to_D = string_of_letters[splice_positions['C']:splice_positions['D']]

#-------------------LOOPS-------------------    