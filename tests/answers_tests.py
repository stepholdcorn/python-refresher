from nose.tools import *
from answers import answers

def test_select_elements_starting_with_a():
  assert_equal(answers.select_elements_starting_with_a(['bananas', 'apples', 'pears', 'avocados']), ['apples', 'avocados'])
