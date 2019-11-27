#----------------------------------------------
# ITEC 3250 Software Engineering
# Automated Test Code
# William Wiggins, Nasir Martin, Marques Wright
#----------------------------------------------

import unittest
import datetime
import phoneselection

# Defining a class that will test different cases for the 
# different functions with the program
class TestPhoneSelection(unittest.TestCase):

    def test_inhouse(self):
        """This function checks if the customer is buying a phone"""
        choice = phoneselection.inhouse()
        self.assertIs(choice, 0)

    def test_owns(self):
        """This function checks if the customer owns their phone"""
        choice = phoneselection.owns()
        self.assertIs(choice, 1)

    def test_numOlines(self):
        """This function checks for how many lines a customer is requesting"""
        result = phoneselection.numOlines()
        self.assertGreater(result, 0)
        self.assertLess(result, 9)
