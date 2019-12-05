#----------------------------------------------
# ITEC 3250 Software Engineering
# Automated Test Code
# William Wiggins, Nasir Martin, Marques Wright
#----------------------------------------------

import unittest
import phoneselection


class TestPhoneSelection(unittest.TestCase):
    
    # Test Query 1: Test ownorbuying() for whether they own a phone
    #               or if they are buying a phone
    def test_ownorbuying(self):
        # Capture the results of the function
        result1 = phoneselection.ownorbuying('Buy')
        result2 = phoneselection.ownorbuying('Own')
        # Check for expected ouput
        buying = 0
        owns = 1
        self.assertEqual(buying, result1, msg="Customer is buying a new phone")
        self.assertEqual(owns, result2, msg="Customer owns the phone")

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
    # Test Query 2: Test numoflines() to see if the value falls
    #               within a valid range
    def test_numOflines(self):
        # Capture the results from the user input
        result1 = phoneselection.numOflines(1)
        result2 = phoneselection.numOflines(2)
        result3 = phoneselection.numOflines(3)
        result4 = phoneselection.numOflines(4)
        result5 = phoneselection.numOflines(5)
        result6 = phoneselection.numOflines(6)
        result7 = phoneselection.numOflines(7)
        result8 = phoneselection.numOflines(8)
        # Check for expected output
        """Checking to see if the result is greater than 0"""
        self.assertGreater(result1, 0)
        self.assertGreater(result2, 0)
        self.assertGreater(result3, 0)
        self.assertGreater(result4, 0)
        self.assertGreater(result5, 0)
        self.assertGreater(result6, 0)
        self.assertGreater(result7, 0)
        self.assertGreater(result8, 0)
        """Checking to see if the result is less than 9"""
        self.assertLess(result1, 9)
        self.assertLess(result2, 9)
        self.assertLess(result3, 9)
        self.assertLess(result4, 9)
        self.assertLess(result5, 9)
        self.assertLess(result6, 9)
        self.assertLess(result7, 9)
        self.assertLess(result8, 9)
        
    # Test Query 3: Test phonetype() for the correct spelling
    #               of the phone type
    def test_phonetype(self):
        style1 = phoneselection.phonetype('Smartphone')
        style2 = phoneselection.phonetype('Basic')
        smart = 'Smartphone'
        base = 'Basic'
        self.assertEqual(style1, smart, msg="Customer chose a smartphone")
        self.assertEqual(style2, base, msg="Customer chose a basic phone")
        
    # Test Query 4: Test features() for incompatible features
    def test_features(self):
        feature1 = 'International Calling'
        feature2 = 'HotSpot'
        feature3 = 'Metered Data'
        feature4 = 'Unlimited Data'
        self.assertEqual(feature1, phoneselection.features('International Calling'))
        self.assertEqual(feature2, phoneselection.features('HotSpot'))
        self.assertEqual(feature3, phoneselection.features('Metered Data'))
        self.assertEqual(feature4, phoneselection.features('Unlimited Data'))

class TestHandlingImproperCases(unittest.TestCase):

    # Test Query 1: Test correctformat() to see if the numbers entered
    #               are in the correct format
    def test_correctnumberformat(self, price):
        self.price = price
        self.assertIs(type(self.price), float)

    # Test Query 2: Test validrange() to see if the plan price and
    #               features are within the correct range
    def test_validrange(self, val_range):
        self.val_range = val_range
        for i in range(7.99, 160):
            self.assertEqual(self.val_range, i)

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
