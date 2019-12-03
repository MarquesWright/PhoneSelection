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

        # Psuedocode for the Boolean combining the above functions
        """ Psuedocode Boolean combining above processes
        
        Assign variable 'inHouse' to 0
        Ask if the user is buying the phone at the provider
        Use 0 for yes and 1 for no
        Program tests if input == 0
        Provider discount is added to background total, if relevant
        """
        
    def test_numOlines(self):
        """This function checks for how many lines a customer is requesting"""
        result = phoneselection.numOlines()
        self.assertGreater(result, 0)
        self.assertLess(result, 9)

class TestHandlingImproperCases(unittest.TestCase):

    def test_correctnumberformat(self):
        """Test to determine if inputs are in the required numeral format"""


    def test_validrange(self):


    def test_costoffeatures(self):


class TestTimeToAnswer(unittest.TestCase):

    def test_timegivenforresults(self):


class TestReliability(unittest.TestCase):

    def test_matchingprices(self):



if __name__ == '__main__':
    unittest.main()
