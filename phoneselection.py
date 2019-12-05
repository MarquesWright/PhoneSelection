ans = str(input("Are you bring over your own phone?"))
gbans = int(input("How many gigabytes are you planning to use?"))
numofpho = int(input("How many lines are you planning to add? "))
if gbans >= 5 and numofpho == 4:
    cricketpho = 100
    verizonpho = 140
    sprintpho = 100
elif gbans > 5 and numofpho >= 4:
    cricketpho = 25 * numofpho
    verizonpho = 35 * numofpho
    sprintpho = 100
elif gbans < 5 and gbans >= 2  and numofpho == 4:
    cricketpho = 90
    verizonpho = 140
    sprintpho = 100
elif gbans < 2 and numofpho == 4:
    cricketpho = 100
    verizonpho = 140
    sprintpho = 100
elif gbans >= 5 and numofpho == 3:
    cricketpho = 90
    verizonpho = 135
    sprintpho = 100
elif gbans < 5 and gbans >= 2 and numofpho == 3:
    cricketpho = 90
    verizonpho = 135
    sprintpho = 100
elif gbans < 2 and numofpho == 3:
    cricketpho = 90
    verizonpho = 135
    sprintpho = 100
elif gbans >= 5 and numofpho == 2:
    cricketpho = 90
    verizonpho = 120
    sprintpho = 100
elif gbans < 5 and gbans >= 2 and numofpho == 2:
    cricketpho = 80
    verizonpho = 120
    sprintpho = 100
elif gbans < 2 and numofpho == 2:
    cricketpho = 75
    verizonpho = 120
    sprintpho = 100 
elif gbans > 5 and numofpho == 1:
    cricketpho = 55
    verizonpho = 60
    sprintpho = 70
elif gbans < 5 and gbans >= 2 and numofpho == 1:
    cricketpho = 40
    verizonpho = 70
    sprintpho = 60
elif gbans < 2 and numofpho == 1:
    cricketpho = 30
    verizonpho = 70
    sprintpho = 60 
if ans == "Yes" or ans == "yes":
    phoprice = float(input("What is the cost of the phone you will be using?"))
    
else:
    phoprice = 0
    
def feature():
    Hotspot = str(input("Do you want to include Hotspot? "))
    if Hotspot == "Yes" or Hotspot == "yes":
        crickethotprice = 10 * numofpho
        verizonhotprice = 10 * numofpho
        sprinthotprice = 0
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


feature()


