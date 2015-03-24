def select_elements_starting_with_a(my_list):
  result = []
  for item in my_list:
    if item.startswith('a'): result.append(item)
  return result