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
        buy = 0
        own = 1
        self.assertEqual(buy, phoneselection.ownorbuying("Buy"))
        self.assertEqual(own, phoneselection.ownorbuying("Own"))

   # Test Query 2: Test numoflines() to see if the value falls
   #               within a valid range
   def test_numOflines(self):
       # Check for expected output
       """Checking to see if the result is greater than 0"""
       self.assertGreaterEqual(phoneselection.numOflines(1), 1)
       self.assertGreaterEqual(phoneselection.numOflines(2), 1)
       self.assertGreaterEqual(phoneselection.numOflines(3), 1)
       self.assertGreaterEqual(phoneselection.numOflines(4), 1)
       self.assertGreaterEqual(phoneselection.numOflines(5), 1)
       self.assertGreaterEqual(phoneselection.numOflines(6), 1)
       self.assertGreaterEqual(phoneselection.numOflines(7), 1)
       self.assertGreaterEqual(phoneselection.numOflines(8), 1)
       """Checking to see if the result is less than 9"""
       self.assertLessEqual(phoneselection.numOflines(1), 8)
       self.assertLessEqual(phoneselection.numOflines(2), 8)
       self.assertLessEqual(phoneselection.numOflines(3), 8)
       self.assertLessEqual(phoneselection.numOflines(4), 8)
       self.assertLessEqual(phoneselection.numOflines(5), 8)
       self.assertLessEqual(phoneselection.numOflines(6), 8)
       self.assertLessEqual(phoneselection.numOflines(7), 8)
       self.assertLessEqual(phoneselection.numOflines(8), 8)
        
    # Test Query 3: Test phonetype() for the correct spelling
    #               of the phone type
    def test_phonetype(self):
        smart = 'Smartphone'
        base = 'Basic'
        self.assertEqual(phoneselection.phonetype('Smartphone'), smart)
        self.assertEqual(phoneselection.phonetype('Basic'), base)
        
    # Test Query 4: Test features() for incompatible features
    def test_features(self):
        feature1 = 'International Calling'
        feature2 = 'HotSpot'
        feature3 = 'Metered Data'
        feature4 = 'Unlimited Data'
        self.assertEqual(phoneselection.features('International Calling'), feature1)
        self.assertEqual(phoneselection.features('HotSpot'), feature2)
        self.assertEqual(phoneselection.features('Metered Data'), feature3)
        self.assertEqual(phoneselection.features('Unlimited Data'), feature4)
