def createGenerator():
    mylist = range(4)
    print(mylist)
    for i in mylist:
        print(i)
        yield i*i

# mygenerator = createGenerator()
# print('what1')
# print(mygenerator.next())
# print('what2')
# print(mygenerator.next())
# print('what3')
# print(mygenerator.next())
#

class Bank(): # let's create a bank, building ATMs
    crisis = False
    def create_atm(self):
        if self.crisis:
            while True:
                yield "$0"
        else:
            while True:
                yield "$100"
        # while not self.crisis:
        #     yield "$100"
        # while


hsbc = Bank() # when everything's ok the ATM gives you as much as you want

corner_street_atm = hsbc.create_atm()

print(corner_street_atm.next())
print(corner_street_atm.next())
print([corner_street_atm.next() for cash in range(5)])
hsbc.crisis = True # crisis is coming, no more money!
print(corner_street_atm.next())
wall_street_atm = hsbc.create_atm() # it's even true for new ATMs
print(wall_street_atm.next())
hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty
print(corner_street_atm.next())
brand_new_atm = hsbc.create_atm() # build a new one to get back in business
# for cash in brand_new_atm:
#    print cash