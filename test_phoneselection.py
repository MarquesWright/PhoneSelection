#----------------------------------------------
# ITEC 3250 Software Engineering
# Automated Test Code
# William Wiggins, Nasir Martin, Marques Wright
#----------------------------------------------

import unittest
import phoneselection


class TestPhoneSelection(unittest.TestCase):

    # def test_inhouse(self):
        """This function checks if the customer is buying a phone"""
        #choice = phoneselection.inhouse()
        #self.assertIs(choice, 0)
    
    # Test Query 1: Test ownorbuying() for whether they own a phone
    #               or if they are buying a phone
    def test_ownorbuying(self):
        # Capture the results of the function
        result = phoneselection.ownorbuying()
        # Check for expected ouput
        owns = 0
        buying = 1
        self.assertEqual(owns, result, "Customer owns the phone")
        self.assertEqual(buying, result, "Customer is buying a new phone")
    
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
        
    # Test Query 2: Test numoflines() to see if the value falls
    #               within a valid range
    def test_numOlines(self):
        result = phoneselection.numOlines()
        self.assertGreater(result, 0)
        self.assertLess(result, 9)
        
    # Test Query 3: Test listofvendors() for the correct spelling
    def test_phonetype(self):
        style = phoneselection.phonetype()
        self.assertEqual()
        
    # Test Query 4: Test
    def test_features(self):
        service = phoneselection.features()
        self.assertEqual()

# class TestHandlingImproperCases(unittest.TestCase):

    # Test Query 1: Test correctformat() to see if the numbers entered
    #               are in the correct format
    # def test_correctnumberformat(self):
        """Test to determine if inputs are in the required numeral format"""

    # Test Query 2: Test validrange() to see if the plan price and
    #               features are within the correct range
    # def test_validrange(self):

    # Test Query 3: Test finalprice() to ensure the price equals
    #               the total of all inputs
    # def test_costoffeatures(self):


# class TestTimeToAnswer(unittest.TestCase):

    # Test Query 1: Test timeforresults() to see if the program is given
    #               one minute to show results
    # def test_timegivenforresults(self):


# class TestReliability(unittest.TestCase):

    # Test Query 1: Test matchingprices() to ensure all prices match the
    #               corresponding price the vendor is providing
    # def test_matchingprices(self):



if __name__ == '__main__':
    unittest.main()
