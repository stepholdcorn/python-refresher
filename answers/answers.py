import math

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

def shortest_word_in_array(my_list):
  length = 100
  for word in my_list:
    if len(word) < length: 
      length = len(word)
      shortest = word
  return shortest

def longest_word_in_array(my_list):
  length = 0
  for word in my_list:
    if len(word) > length:
      length = len(word)
      longest = word
  return longest

def total_of_array(my_list):
  count = 0
  for item in my_list:
    count += item
  return count 

def double_array(my_list):
  return my_list + my_list

def average_of_array(my_list):
  count = 0
  for item in my_list:
    count += item
  return int(round(float(count)/len(my_list)))

def get_elements_until_greater_than_five(my_list):
  location = my_list.index(6)
  return my_list[:location]

def get_all_letters_in_array_of_words(my_list):
  result = []
  for item in my_list:
    item = list(item)
    for i in item:
      result.append(i)
  return sorted(result)

def remove_capital_letters_from_string(string):
  return string.translate(None, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def round_up_number(number):
  return math.ceil(number)

def round_down_number(number):
  return math.floor(number)

def get_domain_name_from_email_address(email_address):
  location1 = email_address.index('@') + 1
  location2 = email_address.index('.')
  return email_address[location1:location2]

def titleize_a_string(string):
  result = []
  string_list = string.capitalize().split(' ')
  for item in string_list:
    if len(item) > 3:
      result.append(item.capitalize())
    else:
      result.append(item)
  return ' '.join(result)

def square_root_of(number):
  return number**0.5



