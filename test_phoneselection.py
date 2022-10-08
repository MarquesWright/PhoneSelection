#----------------------------------------------
# ITEC 3250 Software Engineering
# Automated Test Code
# William Wiggins, Nasir Martin, Marques Wright
#----------------------------------------------

import unittest
from phoneselection import PhoneSelection


class TestPhoneSelection(unittest.TestCase):

    # Create the setUp to intitialize object
    def setUp(self):
        self.phoneT = PhoneSelection()
    
    # Test Query 1: Test ownorbuying() for whether they own a phone
    #               or if they are buying a phone
    def test_ownorbuying(self):
        own = 0
        buy = 1
        self.assertEqual(own, self.phoneT.ownorbuying())
        self.assertEqual(buy, self.phoneT.ownorbuying(self.phone))

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
    #def test_numOflines(self, num):
        #self.num = num

        #self.assertGreaterEqual(phoneselection.numOflines(self.num), 1)
        #self.assertLessEqual(phoneselection.numOflines(self.num), 8)
        
    # Test Query 3: Test phonetype() for the correct spelling
    #               of the phone type
    #def test_phonetype(self, typeOfphone):
        #self.typeOfphone = typeOfphone
        #smart = 'Smartphone'
        #base = 'Basic'
        #self.assertEqual(phoneselection.phonetype(self.typeOfphone), smart)
        #self.assertEqual(phoneselection.phonetype(self.typeOfphone), base)
        
    # Test Query 4: Test features() for incompatible features
    #def test_feature(self, feature):
        #self.feature = feature
        #feature1 = 'International Calling'
        #feature2 = 'Hotspot'
        #feature3 = 'Metered Data'
        #feature4 = 'Unlimited Data'
        #self.assertEqual(phoneselection.feature(self.feature), feature1)
        #self.assertEqual(phoneselection.feature(self.feature), feature2)
        #self.assertEqual(phoneselection.feature(self.feature), feature3)
        #self.assertEqual(phoneselection.feature(self.feature), feature4)

#class TestHandlingImproperCases(unittest.TestCase):

    # Test Query 1: Test correctformat() to see if the numbers entered
    #               are in the correct format
    #def test_correctnumberformat(self, price):
        #self.price = price
        #self.assertIs(phoneselection.correctformat(self.price), float)

    # Test Query 2: Test validrange() to see if the plan price and
    #               features are within the correct range
    #def test_validrange(self, val_range):
        #self.val_range = val_range
        #for i in range(7.99, 160):
            #self.assertEqual(phoneselection.validrange(self.val_range), i)

    # Test Query 3: Test finalprice() to ensure the price equals
    #               the total of all inputs
    #def test_totalcost(self, phonePrice, featurePrice, priceOfplan, total):
        #self.phonePrice = phonePrice
        #self.featurePrice = featurePrice
        #self.priceOfplan = priceOfplan
        #self.total = total

        #subtotal = self.phonePrice + self.featurePrice + self.priceOfplan
        #self.assertEqual(phoneselection.totalcost(self.total), subtotal)


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
