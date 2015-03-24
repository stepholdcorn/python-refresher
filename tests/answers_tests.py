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