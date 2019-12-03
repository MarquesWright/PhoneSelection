cricketpho = float(input("What is the current price of monthly service at cricket?"))
verizonpho = float(input("What is the current price of monthly service at verizon?"))
sprintpho  = float(input("What is the current price of monthly service at sprint?"))
ans = str(input("Are you bring over your own phone?"))
gbans = int(input("How many gigabytes are you planning to use?"))
def phoneprice():
    if ans == "Yes" or ans == "yes":
        phoprice = float(input("What is the cost of the phone you will be using?"))
    else:
        phoprice = 0
def feature():
    Hotspot = str(input("Do you want to include Hotspot? "))
    if Hotspot == "Yes" or Hotspot == "yes":
        crickethotprice = float(input("What is the cost of cricket Hotspot feature? "))
        verizonhotprice = float(input("What is the cost of verizon Hotspot feature? "))
        sprinthotprice = float(input("What is the cost of sprint Hotspot feature? "))
        crickettotal = crickethotprice + phoprice + cricketpho
        verizontotal = verizonhotprice + phoprice + verizonpho
        sprinttotal  = sprinthotprice + phoprice + sprintpho
        if crickettotal <= verizontotal and crickettotal <= sprinttotal:
                print("Cricket has the lowest total cost with the low total price of " + str(crickettotal))
        if verizontotal <= crickettotal and verizontotal <= sprinttotal:
                print("Verizon has the lowest total cost with the low total price of " + str(verizontotal))
        if sprinttotal <= crickettotal and sprinttotal <= verizontotal:
                print("Sprint has the lowest total cost with the low total price of " + str(sprinttotal))
    else:
        crickethotprice = 0
        verizonhotprice = 0
        sprinthotprice = 0
        crickettotal= crickethotprice + phoprice + cricketpho
        verizontotal= verizonhotprice + phoprice + verizonpho
        sprinttotal = sprinthotprice + phoprice + sprintpho
        if crickettotal <= verizontotal and crickettotal <= sprinttotal:
                print("Cricket has the lowest total cost with the low total price of " + str(crickettotal))
        if verizontotal <= crickettotal and verizontotal <= sprinttotal:
                print("Verizon has the lowest total cost with the low total price of " + str(verizontotal))
        if sprinttotal <= crickettotal and sprinttotal <= verizontotal:
                print("Sprint has the lowest total cost with the low total price of " + str(sprinttotal))
phoneprice()
feature()


