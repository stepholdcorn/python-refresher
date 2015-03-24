from nose.tools import *
from answers import answers

def test_select_elements_starting_with_a():
  assert_equal(answers.select_elements_starting_with_a(['bananas', 'apples', 'pears', 'avocados']), ['apples', 'avocados'])

def test_select_elements_starting_with_vowel():
  assert_equal(answers.select_elements_starting_with_vowel(['john', 'david', 'omar', 'fred', 'idris', 'angela']), ['omar', 'idris', 'angela'])

def test_remove_nils_from_array():
  assert_equal(answers.remove_nils_from_array(['a', 'b', None, None, False, 'c', None]), ['a', 'b', False, 'c'])