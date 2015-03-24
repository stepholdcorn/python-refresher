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