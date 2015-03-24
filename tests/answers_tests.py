from nose.tools import *
from answers import answers

def test_select_elements_starting_with_a():
  assert_equal(answers.select_elements_starting_with_a(['bananas', 'apples', 'pears', 'avocados']), ['apples', 'avocados'])

def test_select_elements_starting_with_vowel():
  assert_equal(answers.select_elements_starting_with_vowel(['john', 'david', 'omar', 'fred', 'idris', 'angela']), ['omar', 'idris', 'angela'])

def test_remove_nils_from_array():
  assert_equal(answers.remove_nils_from_array(['a', 'b', None, None, False, 'c', None]), ['a', 'b', False, 'c'])

def test_remove_nils_and_false_from_array():
  assert_equal(answers.remove_nils_and_false_from_array(['a', 'b', None, None, False, 'c', None]), ['a', 'b', 'c'])

def test_reverse_every_element_in_array():
  assert_equal(answers.reverse_every_element_in_array(['dog', 'monkey', 'elephant']), ['god', 'yeknom', 'tnahpele'])

def test_all_elements_except_first_3():
  assert_equal(answers.all_elements_except_first_3([1, 2, 3, 4, 5, 6, 7]), [4, 5, 6, 7])

def test_add_element_to_beginning_of_array():
  assert_equal(answers.add_element_to_beginning_of_array([2, 3, 4, 5], 1), [1, 2, 3, 4, 5])

def test_array_sort_by_last_letter_of_word():
  assert_equal(answers.array_sort_by_last_letter_of_word(['sky', 'puma', 'maker']), ['puma', 'maker', 'sky'])

def test_get_first_half_of_string():
  assert_equal(answers.get_first_half_of_string('banana'), 'ban')
  assert_equal(answers.get_first_half_of_string('apple'), 'app')

def test_make_numbers_negative():
  assert_equal(answers.make_numbers_negative(5), -5)
  assert_equal(answers.make_numbers_negative(-7), -7)

def test_separate_array_into_even_and_odd_numbers():
  assert_equal(answers.separate_array_into_even_and_odd_numbers([1, 2, 3, 4, 5, 6, 7]), [[2, 4, 6], [1, 3, 5, 7]])

def test_number_of_elements_that_are_palindromes():
  assert_equal(answers.number_of_elements_that_are_palindromes(['bob', 'radar', 'alex', 'noon', 'banana']), 3)

def test_shortest_word_in_array():
  assert_equal(answers.shortest_word_in_array(['here', 'is', 'a', 'bunch', 'of', 'words', 'of', 'different', 'lengths']), 'a')

def test_longest_word_in_array():
  assert_equal(answers.longest_word_in_array(['here', 'is', 'a', 'bunch', 'of', 'words', 'of', 'different', 'lengths']), 'different')

def test_total_of_array():
  assert_equal(answers.total_of_array([1, 3, 5, 6, 2, 8]), 25)

def test_double_array():
  assert_equal(answers.double_array([1, 2, 3]), [1, 2, 3, 1, 2, 3])

def test_average_of_array():
  assert_equal(answers.average_of_array([10, 15, 25]), 17)

def test_get_elements_until_greater_than_five():
  assert_equal(answers.get_elements_until_greater_than_five([1, 3, 5, 4, 1, 2, 6, 2, 1, 3, 7]), [1, 3, 5, 4, 1, 2])

def test_get_all_letters_in_array_of_words():
  assert_equal(answers.get_all_letters_in_array_of_words(['cat', 'dog', 'fish']), ['a', 'c', 'd', 'f', 'g', 'h', 'i', 'o', 's', 't'])
  
def test_remove_capital_letters_from_string():
  assert_equal(answers.remove_capital_letters_from_string('Hello JohnDoe'), 'ello ohnoe')

def test_round_up_number():
  assert_equal(answers.round_up_number(3.142), 4)

def test_round_down_number():
  assert_equal(answers.round_down_number(4.9), 4)

def test_get_domain_name_from_email_address():
  assert_equal(answers.get_domain_name_from_email_address('alex@makersacademy.com'), 'makersacademy')

def test_titleize_a_string():
  assert_equal(answers.titleize_a_string('the lion the witch and the wardrobe'), 'The Lion the Witch and the Wardrobe')



