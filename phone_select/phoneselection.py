class PhoneSelection(object):
    # create a method to ask if user owns phone 
    # or will be buying a new one
    def ownorbuying(self, answer):
        if answer == 'Own' or answer == 'own':
            return 0
        elif answer == 'Buy' or answer == 'buy':
            return 1
        #else:
            #raise ("Invalid ")

if __name__ == '__main__':
    phone = PhoneSelection()
    answer1 = input("Do You Own A Phone or Buying a New One? Answer Own or Buy: ")
    response1 = phone.ownorbuying("Own")
