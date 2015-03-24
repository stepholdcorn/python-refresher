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