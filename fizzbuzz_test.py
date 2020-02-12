#pylint: disable=unused-variable 
"""Unit tests for Fizzbuzz"""

#import the code to be tested
from fizzbuzz1 import fizz

def describe_a_fizzbuzz_program():
    """A program to play the FizzBuzz game."""

    def test_it_can_blow_smoke():
        """Make sure our testing infrastructure is working"""
        assert True == True
        
        def can_determine_if_a_number_is_a_multiple_of_3():
            """Checks to see if a given number is a multiple of 3."""
            assert fizz(3) == True
            assert fizz(2) == False