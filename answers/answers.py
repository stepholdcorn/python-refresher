def select_elements_starting_with_a(my_list):
  result = []
  for item in my_list:
    if item.startswith('a'): result.append(item)
  return result

def select_elements_starting_with_vowel(my_list):
  result = []
  vowel = list('aeiou')
  for item in my_list:
    for letter in vowel:
      if item.startswith(letter): result.append(item)
  return result

def remove_nils_from_array(my_list):
  result = []
  for item in my_list:
    if item != None: result.append(item)
  return result

def remove_nils_and_false_from_array(my_list):
  result = []
  for item in my_list:
    if item != None and item != False: result.append(item)
  return result

def reverse_every_element_in_array(my_list):
  result = []
  for item in my_list: result.append(item[::-1])
  return result

def all_elements_except_first_3(my_list):
  return my_list[3:]

def add_element_to_beginning_of_array(my_list, element):
  my_list.insert(0, element)
  return my_list

def array_sort_by_last_letter_of_word(my_list):
  result = []
  backwards = []
  for item in my_list: backwards.append(item[::-1])
  sorted_backwards = sorted(backwards)
  for item in sorted_backwards: result.append(item[::-1])
  return result

def get_first_half_of_string(string):
  half_way = int(round(len(string)*0.5))
  return string[0:half_way]

def make_numbers_negative(integer):
  return -abs(integer)

def separate_array_into_even_and_odd_numbers(my_list):
  result= []
  even = my_list[1::2]
  odd = my_list[0::2]
  result.append(even)
  result.append(odd)
  return result

def number_of_elements_that_are_palindromes(my_list):
  count = 0
  for word in my_list:
    if word == word[::-1]:
      count +=1
  return count


